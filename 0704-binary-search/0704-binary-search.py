class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        
        index=0
        while nums[index]!=target:
            index+=1
        return index
            