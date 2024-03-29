class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1 for i in range(len(nums))]
        right=[1 for i in range(len(nums))]
        for i in range(1,len(left)):
            left[i]=left[i-1]*nums[i-1]
        for i in range(len(left)-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        output=[1 for i in range(len(nums))]
        for i in range(len(nums)):
            output[i]=left[i]*right[i]
        return output
        