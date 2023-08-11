class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniquenum=0
        for index in nums:
            uniquenum^=index
        return uniquenum