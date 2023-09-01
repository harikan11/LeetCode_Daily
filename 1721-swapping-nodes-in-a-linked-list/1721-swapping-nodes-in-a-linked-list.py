# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        def getlength(node):
            length=0          #calc the length of the LL
            while node:
                length+=1
                node=node.next
            return length
        length=getlength(head)
        
        if k<=0 or k>length:
            return head        #checking k is not out of bounds
        
        #find kth from the start
        kth_fromstart=head
        for _ in range(k-1):
            kth_fromstart=kth_fromstart.next
        
        #find kth from the end
        kth_fromend=head
        for _ in range(length-k):
            kth_fromend=kth_fromend.next
            
        kth_fromstart.val,kth_fromend.val=kth_fromend.val,kth_fromstart.val
        
        return head
        