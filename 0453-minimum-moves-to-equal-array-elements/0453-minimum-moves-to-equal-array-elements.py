class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count=0
        min_num=min(nums)
        for num in nums:
            count+=abs(min_num-num)
        return count
            