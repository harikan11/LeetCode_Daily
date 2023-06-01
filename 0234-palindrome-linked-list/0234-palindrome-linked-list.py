# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        pcounter=head
        countNodes=0
        while (pcounter):
            countNodes+=1
            pcounter = pcounter.next
            
        p1=head
        p2=head
        elements=[]
        for i in range(countNodes//2):
            elements.append(p2.val)
            p2=p2.next
         
        if (countNodes%2!=0):
            p2=p2.next
            
        while(p2):
            if (not elements or p2.val!=elements.pop()):
                return False
            p2=p2.next
        return True
            
        

            
        
            
            
            
            
        