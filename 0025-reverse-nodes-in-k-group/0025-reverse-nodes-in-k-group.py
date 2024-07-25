class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head 
        prev_tail = None

        new_head = None

        while current:

            kth_node = self.find_kth_node(current, k)
            if not kth_node:
                break
            
            next_group_head = kth_node.next

            new_group_head = self.reverse_nodes(current, kth_node.next)

            if not new_head:
                new_head = new_group_head

            if prev_tail:
                prev_tail.next = new_group_head

            
            prev_tail = current

            current  = next_group_head

        return new_head or head
  




    def find_kth_node(self, node, k):
        while node and k > 1:
            node = node.next
            k -= 1
        return node

    
    
    def reverse_nodes(self, start, end):
        prev, current = end, start
        while current != end:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev