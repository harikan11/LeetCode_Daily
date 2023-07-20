# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = ''
        itr = l1
        while itr:
            val1 += str(itr.val)
            itr = itr.next
        val2 = ''
        itr = l2
        while itr:
            val2 += str(itr.val)
            itr = itr.next
        SUM = str(int(val1) + int(val2))

        head = ListNode()
        curr = head
        for i in range(len(SUM)):
            curr.next = ListNode(SUM[i])
            curr = curr.next
        return head.next
            
            