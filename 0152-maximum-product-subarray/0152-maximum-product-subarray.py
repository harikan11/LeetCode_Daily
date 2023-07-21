class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums) #cant be 0
        curr_min=1
        curr_max=1 #since 1 is a neutral val
        for n in nums:
            if n==0: #you dont want 0, you dont multiply a number with 0 because then everything will be 0 only
                curr_min,curr_max=1,1
                continue
            temp=curr_max*n #to reuse curr_max's original value before computation
            curr_max=max(temp,n*curr_min,n)
            curr_min=min(temp,n*curr_min,n)
            res=max(res,curr_max)
        return res
            
        #O(n)=TC
            
            
        
        