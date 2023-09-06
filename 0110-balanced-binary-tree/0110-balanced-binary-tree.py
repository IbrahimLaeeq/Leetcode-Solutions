# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # find depths of left subtree , right subtree
    # compare both -- diff <= 1

        # find depth 
        # Define a function depth
        # if root is empty -> return 0
        # return max(depth(root.right), depth(root.left)) + 1

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.right), self.depth(root.left)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if root is empty -> return True 
        if not root: return True  
        # find depth of left subtree
        left = self.depth(root.left)
        # find depth of right subtree 
        right = self.depth(root.right)
        # compare both -> (left - right) <= 1 
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# Time Complexity -> O(n)
# Space Complexity -> O(n) 