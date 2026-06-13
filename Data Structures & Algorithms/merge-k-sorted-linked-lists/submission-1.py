# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode()
        head = root
        while lists:
            min = ListNode(1001)
            idx = -1
            i = 0
            while i < len(lists):
                if not lists[i]:
                    lists.pop(i)
                else:
                    if lists[i].val < min.val:
                        min = lists[i]
                        idx = i
                    i += 1
            if idx != -1:
                head.next = ListNode(min.val)
                head = head.next
                lists[idx] = lists[idx].next

        return root.next