class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares=[]
        min_index=0
        max_index=len(nums)-1
        
        while min_index<=max_index:
            if nums[min_index]**2<nums[max_index]**2:
                squares.insert(0,nums[max_index]**2)
                max_index-=1
            else:
                squares.insert(0,nums[min_index]**2)
                min_index+=1
        return squares
        