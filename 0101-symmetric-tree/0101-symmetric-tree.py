class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def number(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and number(left.left, right.right) and number(left.right, right.left)
        
        return number(root.left, root.right)
