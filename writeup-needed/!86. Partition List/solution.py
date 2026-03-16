# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: 
            return head
        
        smaller = ListNode(0, None)
        bigger = ListNode(0, None)
        
        while head:
            n = head.next
            if head.val < x:
                head.next = smaller.next
                smaller.next = head
            else:
                head.next = bigger.next
                bigger.next = head
                
            head = n
        
        result = ListNode(0, None)
        while bigger.next:
            n = bigger.next.next
            bigger.next.next = result.next
            result.next = bigger.next
            bigger.next = n

        smaller = smaller.next
        while smaller:
            n = smaller.next
            smaller.next = result.next
            result.next = smaller
            smaller = n

        return result.next