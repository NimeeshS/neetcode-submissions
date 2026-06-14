# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev, curr = None, head

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, curr

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0)
        tail = dummy

        i = 0
        while length - i >= k:
            group_head = head
            new_head, next_group = reverse(head, k)
            tail.next = new_head
            tail = group_head
            head = next_group
            i += k

        tail.next = head

        return dummy.next