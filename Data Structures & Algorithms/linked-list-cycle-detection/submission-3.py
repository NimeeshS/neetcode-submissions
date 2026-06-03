# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        head1, head2 = head, head.next if head else None
        while head1 and head2:
            if head1 == head2: return True
            head1 = head1.next
            head2 = head2.next.next if head2.next else None

        return False