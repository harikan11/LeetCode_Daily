class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        num=0
        p=Counter(s).values()
        for i in p:
            if i%2==1: #if odd
                num=num+1
        if num<=k:
            return True
        return False
                
                
                