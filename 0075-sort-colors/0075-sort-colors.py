class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt0=0
        cnt1=0
        cnt2=0
        n=len(nums)
        for i in range(n):
            if nums[i] == 0:
                cnt0 += 1
            elif nums[i] == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        i = 0
        while cnt0 > 0:
            nums[i] = 0
            i += 1
            cnt0 -= 1
        while cnt1 > 0:
            nums[i] = 1
            i += 1
            cnt1 -= 1
        while cnt2 > 0:
            nums[i] = 2
            i += 1
            cnt2 -= 1
            
                
            
        