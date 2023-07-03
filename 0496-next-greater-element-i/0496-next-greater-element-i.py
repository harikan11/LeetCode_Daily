class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                d[stack.pop()] = num

            stack.append(num)
        
        res = []
        for num in nums1:
            if num not in d:
                res.append(-1)
            else:
                res.append(d[num])
        return res