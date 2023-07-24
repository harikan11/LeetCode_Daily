class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp=[False]*(len(s)+1) #cache
        dp[len(s)]=True #base case
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if (i+len(word)<=len(s) and s[i:i+len(word)]==word): #checking that there are enough characters in s to compare with word
                    dp[i]=dp[i+len(word)]
                if dp[i]:
                    break
        return dp[0]
                    