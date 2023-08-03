class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = [0]*len(nums)
        min_prod = [0]*len(nums)
        max_prod[0] = nums[0]
        min_prod[0] = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                max_prod[i] = max(nums[i], max_prod[i-1]*nums[i])
                min_prod[i] = min(nums[i], min_prod[i-1]*nums[i])
            else:
                max_prod[i] = max(nums[i], min_prod[i-1]*nums[i])
                min_prod[i] = min(nums[i], max_prod[i-1]*nums[i])
            result = max(result, max_prod[i])

        return result

        
        