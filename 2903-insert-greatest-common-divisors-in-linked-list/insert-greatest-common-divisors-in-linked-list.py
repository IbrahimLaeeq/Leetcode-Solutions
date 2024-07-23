# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        ans = temp
        while temp and temp.next:
            gcd_val = math.gcd(temp.val,temp.next.val)
            gcd_node = ListNode(gcd_val)
            gcd_node.next = temp.next
            temp.next = gcd_node
            temp = gcd_node.next
        return ans


