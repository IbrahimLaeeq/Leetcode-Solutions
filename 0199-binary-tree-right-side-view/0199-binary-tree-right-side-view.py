# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        # intializing queue with the root for the while loop
        ans = [root.val]
        # the first ele will be in the answer regardless
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                #pop the first ele from the queue
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                # append the left and right children fo the popped node

            if queue:
                ans.append(queue[-1].val)
            # append the value of the right most ele in the queue
            # our queue consists of nodes here
        return ans

        