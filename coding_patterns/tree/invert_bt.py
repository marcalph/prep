class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def invert_binary_tree(root: TreeNode | None) -> TreeNode | None:
    # Write your code gere
    if root is None:
        return None

    # swap children
    root.left, root.right = root.right, root.left

    # recurse
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root
