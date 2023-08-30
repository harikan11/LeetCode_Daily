class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n=len(nums)
        i=nums.index(1)
        j=nums.index(n)
        ans=i+n-1-j-(i>j)
        return ans
        