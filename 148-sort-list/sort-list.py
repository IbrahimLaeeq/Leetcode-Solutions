# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # split list in two equal portions
        l = head
        r = self.getMid(head)
        temp = r.next
        r.next = None
        r = temp

        l = self.sortList(l)
        r = self.sortList(r)
        return self.merge(l,r)
    
    def getMid(self, head):
        slow , fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow # returns the middle value
    
    def merge(self, l , r):
        curr = dummy = ListNode()
        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        if l : 
            curr.next = l
        else:
            curr.next = r
        return dummy.next


        