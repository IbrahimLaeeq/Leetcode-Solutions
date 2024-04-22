# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first count the no of nodes

        count = 0 
        current = head

        while current:
            count+=1
            current = current.next
        
        # now traverse again only till the half of the linked list

        # utlize the fact that you know the no of nodes in the list
        middle = head 

        for i in range ( count // 2):
            middle = middle.next
        
        return middle 
        