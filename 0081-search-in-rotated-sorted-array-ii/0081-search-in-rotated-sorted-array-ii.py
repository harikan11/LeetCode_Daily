class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target or nums[l] == target or nums[r] == target:
                return True
            elif nums[mid] == nums[l] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]: #to check if left half is sorted
                if nums[l] <= target <nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False