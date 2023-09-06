# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # root of a binary tree 
        # post order traversal 
        # first traverse left subtree
        # then traverse right subtree
        # return node.val

        # Steps
        # create an array - result 
        result = []
        # create post order traversal function 
        def post_order(root):
            if root:
            #   traverse left subtree 
                post_order(root.left) 
            #   traverse right subtree  
                post_order(root.right)  
            #   current node 
                result.append(root.val)
        # call post order function(root)
        post_order(root)
        # return result
        return result

# Time Complexity -> O(n)
# Space Complexity -> O(n) 