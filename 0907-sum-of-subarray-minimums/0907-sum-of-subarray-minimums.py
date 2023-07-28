class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod=10**9+7
        stack=[]
        dp=[0]*len(arr)
        
        for i,n in enumerate(arr):
            while stack and arr[stack[-1]]>=n:
                stack.pop()
            if stack:
                dp[i]=dp[stack[-1]]+(n*(i-stack[-1]))
            else:
                dp[i]=n*(i+1)
            stack.append(i)
        return sum(dp)%mod
        