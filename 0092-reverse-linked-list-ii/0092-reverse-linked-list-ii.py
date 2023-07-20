# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        start = prev.next
        end = start.next
        # Reverse the nodes
        for i in range(right - left):
            start.next = end.next
            end.next = prev.next
            prev.next = end
            end = start.next
        return dummy.next
        