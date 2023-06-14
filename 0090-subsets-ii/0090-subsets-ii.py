class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(i,subset):
            if i==len(nums): #this is basecase
                res.append(subset[::])
                return 
            #creating a copy of subset
                
            #all subsets that include nums[i]s
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()
            
            #all subsets that do not inclue nums[i]
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1,subset)
            
        backtrack(0,[])
        return res
            
            
                
        
                
            