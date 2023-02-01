class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing=len(nums)
        for i in range(len(nums)):
            missing^=i^nums[i]
        return missing
        