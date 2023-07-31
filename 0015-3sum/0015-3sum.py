class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        #every number in the array is a possible first value
        for i,a in enumerate(nums):
            #you dont want to use the same value in the same pos of the res twice
            if i>0 and a==nums[i-1]:  #a==nums[i-1] checks if the next value is same as the nums[i-1]
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                threeSum=a+nums[l]+nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
                    
                    
                
                    