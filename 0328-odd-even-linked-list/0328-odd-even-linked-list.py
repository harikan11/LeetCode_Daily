# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd=head
        evenhead=even=head.next #evenhead is used to connect last odd node with even node
        while even and even.next: #odd always exists since first node, and next odd node is even.next
            odd.next=odd.next.next #old odd connected to new odd
            odd=odd.next
            
            even.next=even.next.next #old even connected to new even
            even=even.next
        odd.next=evenhead #last odd node connected to evenhead
        
        return head