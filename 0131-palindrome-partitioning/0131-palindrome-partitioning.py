class Solution:
    def partition(self, s: str) -> List[List[str]]:

        @cache

        def dfs(s):

            if not s:
                return [[]]
            res=[]

            for i in range(len(s)):
                sub=s[:i+1]
                if sub==sub[::-1]:
                    l=dfs(s[i+1:])
                    res+=[[sub]+sl for sl in l]

            
            return res

        
        
        return dfs(s)
        