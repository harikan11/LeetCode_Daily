class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        m=300 #some random big number
        dp=[[0 for j in range(k+1)] for i in range(n+1)]
        for i in range(1, m+1):
            for j in range(1, k+1):
                dp[i][j] = 1 + dp[i-1][j] + dp[i-1][j-1]
                if dp[i][j] >= n:
                    return i