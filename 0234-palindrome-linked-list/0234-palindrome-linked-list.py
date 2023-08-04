# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        #to find middle node(slow)
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        #to reverse
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow  #slow is curr in reversal of LL problem
            slow=temp
        
        #to check if palindrome
        left=head
        right=prev  #slow is Null and prev is just one node behind it
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True