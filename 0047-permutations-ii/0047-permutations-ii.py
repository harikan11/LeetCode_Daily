class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(list(permutations(nums)))
            