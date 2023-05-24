class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        count=1
        n=len(b)
        t=str(a)
        while b!=t and len(t)<=n:
            count+=1
            t=a*count
        if b in t:
            return count
        if b in a*(count+1):
            return count+1
            
        return -1

                
        