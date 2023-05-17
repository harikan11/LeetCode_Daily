class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax=nums[0]
        currmin=nums[0]
        res=nums[0]
        for i in nums[1:]:
            maxtemp=max(i*currmax,i,i*currmin)
            currmin=min(i*currmin,i,i*currmax)
            currmax=maxtemp
            res=max(currmax,res)
        return res
        
   
    
        
