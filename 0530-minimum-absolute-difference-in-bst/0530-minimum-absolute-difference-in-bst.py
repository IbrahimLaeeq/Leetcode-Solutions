class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inOrderTraversal(node):
            nonlocal prev, min_diff
            if node is None:
                return

            # Recursively traverse the left subtree
            inOrderTraversal(node.left)

            # Calculate the absolute difference between the current node's value and the previous node's value
            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev))

            # Update the previous node
            prev = node.val

            # Recursively traverse the right subtree
            inOrderTraversal(node.right)

        prev = None  # To keep track of the previous node's value during traversal.
        min_diff = float('inf')  # Initialize the minimum difference to positive infinity.
        inOrderTraversal(root)  # Start the in-order traversal from the root.
        return min_diff

# Example usage:
# root = TreeNode(4)
# root.left = TreeNode(2, TreeNode(1), TreeNode(3))
# root.right = TreeNode(6)
# print(Solution().getMinimumDifference(root))  # Output: 1
