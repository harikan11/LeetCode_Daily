class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        nums.sort()
        
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            #decision to not include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
            