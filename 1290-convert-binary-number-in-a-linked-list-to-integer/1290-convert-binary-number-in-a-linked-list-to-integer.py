class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = head.val

        while head.next:
            result = result * 2 + head.next.val
            head = head.next

        return result
