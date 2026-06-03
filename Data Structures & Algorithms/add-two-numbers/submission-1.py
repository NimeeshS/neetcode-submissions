# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = "", ""
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next

        s = int(n1[::-1]) + int(n2[::-1])
        s = str(s)[::-1] if s != 0 else "0"

        head = ListNode(int(s[0])) if len(s) >= 1 else None
        curr = head
        for i in range(1, len(s)):
            curr.next = ListNode(int(s[i]))
            curr = curr.next

        return head