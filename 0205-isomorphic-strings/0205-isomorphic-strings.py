class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        dict2 = {}
        
        if len(s)==0 or len(t)==0:
            return False
        if len(s)!= len(t):
            return False
        for a,b in zip(s,t):
            if a not in dict:
                dict[a]=b
            else:
                if dict[a]!=b:
                    return False
            if b not in dict2:
                dict2[b] = a
            else:
                if dict2[b]!=a:
                    return False
        return True