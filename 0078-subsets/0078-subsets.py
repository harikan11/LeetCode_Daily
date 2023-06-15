class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(i,subset):
            if i==len(nums):
                res.append(subset[::])
                return
            
            #to select an element in the subset
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()
            
            
            
            
            #to not select an element in the subset
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1,subset)
        backtrack(0,[])
        return res