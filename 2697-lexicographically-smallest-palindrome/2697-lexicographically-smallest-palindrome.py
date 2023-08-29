class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        r=len(s)-1
        l=0
        s=list(s)
        
        while r>l:
            if s[r]>s[l]:
                s[r]=s[l]
            else:
                s[l]=s[r]
            r-=1
            l+=1
        return ''.join([i for i in s])
                
                
                