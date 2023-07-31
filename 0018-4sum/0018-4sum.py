class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[] #final res of quadruplets
        quad=[] #curr quadruplets that we're building on
        def kSum(k,start,target): #nums is not gonna change so we dont have to define it in the helper function but target is defined because its changing 
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1,i+1,target-nums[i])
                    quad.pop()
                return
            
            #base case
            l=start
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    res.append(quad+[nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        kSum(4,0,target)
        return res
                
                
            