class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1 #empty string can be decoded in one way onlu
        dp[1]=1 if s[0]!='0' else 0 #single char string can be decoded in one way only too
        for i in range(2, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:  # Update the comparison here
                dp[i] += dp[i-2]

        return dp[n]