# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        len, tail=1,head
        while tail.next:
                tail=tail.next
                len+=1
        k=k%len
        if k==0:
            return head
        
        curr=head
        for i in range(len-k-1):
            curr=curr.next
        newHead=curr.next
        curr.next=None
        tail.next=head
        
        return newHead
            
        
        
        