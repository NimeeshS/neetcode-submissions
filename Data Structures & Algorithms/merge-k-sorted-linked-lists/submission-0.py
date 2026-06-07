# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        n = head
        check = True
        
        while check:
            check = False
            m = ListNode(1001)
            idx = -1
            for i in range(len(lists)):
                if lists[i]:
                    check = True
                    if lists[i].val < m.val:
                        m = lists[i]
                        idx = i

            if idx != -1:
                n.next = m
                n = n.next
                lists[idx] = lists[idx].next

        return head.next