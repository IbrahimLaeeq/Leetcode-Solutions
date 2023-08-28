# Definition of ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA and headB:
            A, B = headA, headB
            while A != B:
                A = A.next if A else headB
                B = B.next if B else headA
            return B

# Create linked list 1: 1 -> 9 -> 1 -> 2 -> 4
headA = ListNode(1)
headA.next = ListNode(9)
headA.next.next = ListNode(1)
headA.next.next.next = ListNode(2)
headA.next.next.next.next = ListNode(4)

# Create linked list 2: 3 -> 2 -> 4
headB = ListNode(3)
headB.next = headA.next.next.next

# Create an instance of the Solution class
solution = Solution()

# Call the getIntersectionNode function
intersection_node = solution.getIntersectionNode(headA, headB)

if intersection_node:
    print("Intersection node value:", intersection_node.val)
else:
    print("No intersection node found")