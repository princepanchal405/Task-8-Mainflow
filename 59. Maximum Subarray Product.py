def max_product(nums):
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod  # swap
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)

    return result

# ---------- Example Usage ----------
if __name__ == "__main__":
    nums1 = [2, 3, -2, 4]
    print("Maximum Subarray Product:", max_product(nums1))  # Output: 6

    nums2 = [-2, 0, -1]
    print("Maximum Subarray Product:", max_product(nums2))  # Output: 0

