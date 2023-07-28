class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater={} #output, stores the next greater ele of eles in nums2
        stack=[] #to store the numbers whose next greater ele is not found
        for num in nums2:
            while stack and num>stack[-1]: #stack is not empty and some ele(num) is greater than top ele in stack
                next_greater[stack.pop()]=num
            stack.append(num)
            
        res=[]
        for num in nums1:
            if num in next_greater:
                res.append(next_greater[num])
            else:
                res.append(-1)
        return res