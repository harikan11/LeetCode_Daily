class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)): #starting at i+1 amd going till end of the array
                if nums[i]<nums[j]: #this has to be true for increasing subsequence
                    LIS[i]=max(LIS[i],1+LIS[j])
        return max(LIS)