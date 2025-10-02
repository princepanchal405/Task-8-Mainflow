# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# ---------- Serialize Function ----------
def serialize(root):
    """Encodes a tree to a single string."""
    if not root:
        return "#,"  # Use # for null
    return str(root.val) + "," + serialize(root.left) + serialize(root.right)

# ---------- Deserialize Function ----------
def deserialize(data):
    """Decodes your encoded data to tree."""
    def helper(nodes):
        val = next(nodes)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node

    node_iter = iter(data.split(","))
    return helper(node_iter)

# ---------- Example Usage ----------
if __name__ == "__main__":
    # Create sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Serialize
    serialized = serialize(root)
    print("Serialized:", serialized)

    # Deserialize
    deserialized_root = deserialize(serialized)
    print("Deserialized Root Value:", deserialized_root.val)
