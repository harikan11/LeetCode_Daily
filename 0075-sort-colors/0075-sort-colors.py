class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0=0
        count1=0
        count2=0
        for i in range(len(nums)):
            nums.sort()