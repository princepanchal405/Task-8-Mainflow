# ---------- Serialization ----------
def serialize(data):
    if isinstance(data, dict):
        items = []
        for k, v in data.items():
            items.append(f"{k}={serialize(v)}")
        return "{" + ";".join(items) + ";}"
    elif isinstance(data, list):
        items = [serialize(x) for x in data]
        return "[" + ",".join(items) + "]"
    else:
        return str(data)

# ---------- Deserialization ----------
def deserialize(s):
    s = s.strip()
    if s.startswith("{") and s.endswith("}"):
        s = s[1:-1]
        result = {}
        if not s:
            return result
        parts = s.split(";")
        for part in parts:
            if not part:
                continue
            k, v = part.split("=", 1)
            result[k] = deserialize(v)
        return result
    elif s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
        if not s:
            return []
        return [deserialize(x) for x in s.split(",")]
    else:
        # Try convert to int/float else return string
        if s.isdigit():
            return int(s)
        try:
            return float(s)
        except:
            return s

# ---------- Example Usage ----------
if __name__ == "__main__":
    data = {
        "name": "John",
        "age": 30,
        "skills": ["Python", "JS", "SQL"],
        "projects": {"AI": "Done", "Web": "In Progress"}
    }

    serialized = serialize(data)
    print("Serialized:", serialized)

    deserialized = deserialize(serialized)
    print("Deserialized:", deserialized)
