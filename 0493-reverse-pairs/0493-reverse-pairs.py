class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergesort(nums,start,end):
            if start>=end:
                return 0
            mid=(start+end)//2
            count = mergesort(nums, start, mid) + mergesort(nums, mid + 1, end)
            
            j=mid+1
            for i in range(start,mid+1):
                while j<=end and nums[i]>2*nums[j]:
                    j+=1
                count+=j-(mid+1)
            nums[start:end+1] = sorted(nums[start:end+1])
            return count

        return mergesort(nums, 0, len(nums) - 1)