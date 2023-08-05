# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head) # dummy node is initially 0 and the next node to it is head
        leftprev=dummy
        curr=head                        ## consider left and right pointers to where the reversal starts and ends
        
        for i in range(left-1): #step1 to reach the left ptr
            leftprev=curr
            curr=curr.next
            #prev and curr iterate until you reach the right pointer i.e right-left+1
            
            
            #curr=left and leftprev=node before left
            #step2 to reverse from left to right
        prev=None
        for i in range(right-left+1):
            temp=curr.next
            
            curr.next=prev
            prev=curr
            
            curr=temp
        #to update the ptrs of right and left using leftprev
        leftprev.next.next=curr #left pointer after reversal points to curr which is at the end of the ll or Null
        leftprev.next=prev #right pointer after reversal points to leftnode's next node
        return dummy.next