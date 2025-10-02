# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def kth_smallest(root, k):
    """Returns the K-th smallest element in BST"""
    res = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    inorder(root)
    return res[k-1]  # K-th smallest (1-indexed)

# ---------- Example Usage ----------
if __name__ == "__main__":
    # Create BST
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    k = 3
    print(f"{k}-th Smallest Element:", kth_smallest(root, k))
