# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check for empty lists
        if list1 is None and list2 is None:
            return None
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is not None:
            return list2

        # Create a dummy head node
        dummy = ListNode()
        tail = dummy

        # Iterate while both lists have elements
        while list1 and list2: # only runs when both have elements remaining
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Append remaining elements
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # Return the actual list (excluding dummy head)
        return dummy.next
        '''
        time : O(n)
        space: O(n)
        '''