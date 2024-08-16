# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = collections.deque([root])
        
        ans = [[root.val]]
        
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right.val)
                    
            if temp != []:
                ans.append(temp)
        
        return ans