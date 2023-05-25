class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n>=k-1+maxPts:
            return 1
        
        dp=[0]*(n+1)
        dp[0],curSum=1,0
        
        for i in range(1,n+1):
            if i-1<k:
                curSum+=dp[i-1]
            if i-1>=maxPts:
                curSum-=dp[i-1-maxPts]
            dp[i]=curSum/maxPts
        return sum(dp[k:])
        