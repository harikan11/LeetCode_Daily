# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        
        grouprev=dummy
        
        while True:
            kth=self.getKth(grouprev,k)
            if not kth:
                break
            groupNext=kth.next
            
            
            prev,curr=kth.next,grouprev.next
            
            while curr!=groupNext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
                
            tmp=grouprev.next
            grouprev.next=kth
            grouprev=tmp
            
        return dummy.next
            
                
        
            
    
    def getKth(self, curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
    
    
        