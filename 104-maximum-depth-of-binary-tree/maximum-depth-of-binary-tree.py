# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 

        '''
        the main tirck here is that we need to add one bc at teh 
        base case when a node has no further children , then  , 
        the depth will be reuturned as zero wheras we want to return it 
        as one , this realtes to the conept where the start counting the 
        depth from 1 other-wise if they counted the root node from zero , then , 
        we would not need to add this "1" , but , genereally we start 
        counting depth from 1 

        we take the max bc the depth of a sub tree is the height esentially and 
        we consider the longest path to the leafnode we coudl also rebrand this
        problem of find nf the maximum dpeth as findiing hte longest paht 
        from the root node to the leaf node

        tricks:
        1. if a tree with no children exists then the depth of that tree is one
        bc we still count the root node other-wise if we dont count the root node
        then the depth would be zero but in this case even if we have a singel node
        then we count the depth as one whereas this is a bit confusing at first 
        becuase we thnk of this problmem as determining the longest path 
        from the root node to the leaf nodes so in this case if we have no 
        leaf nodes then , the , length of teh path will still be one bc we do 
        have a root node 

        2. the base or termination case here would be that if we call this 
        function on a "null" node , tehn, it would ntermiaton and at this
        poit when the root node is null then we can say that the depth of 
        that sub-tree whose root is "null" is zero 

        VISUAL TRICK:
        FOLLOW TEH BOTTOM TO TOP APPROACH AND GO FROM THE BOTTOM TO 
        THE TOP AND CREATE SUB-TREES FOR EACH NODE BY MAMKING SURE THAT 
        EACH NODE HAS TWO CHILDREN AND MAKE SURE TO ADD THE "NULL" NODES
        AS CHILDREN AND TEHN GO FROM TEH BOTTOM TO THE TOP CHECKING TEH 
        DEPTH OF EACH OF TEH SUB-TRESS BC THIS IS HOW RECUSRION WORK S
        I.E. WE STOP THE RECURSING WHEN WE RAECH THE BASE CASE AND TEHN 
        WE GO TO THE TOP RESOLVING THE CALL-STACK AT EACH ITERAION 
        SO TO SPEAK 

        ALSO HERE WHEN VISUALIXING MAKE A SUBTREE WHOSE PARENT NODE IS 
        A "NULL" NODE TO BETTER UNDERSTAND THE PART WHERE WE CALL THIS 
        FUNCTIN ON A "NULL " NODE 
        '''
