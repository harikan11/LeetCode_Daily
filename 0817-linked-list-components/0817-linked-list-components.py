# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums=set(nums)
        curr=head
        res=0
        connected=False
        
        while curr:
            if curr.val in nums:
                if not connected:
                    res+=1
                    connected=True
            else:
                connected=False
            curr=curr.next
        return res