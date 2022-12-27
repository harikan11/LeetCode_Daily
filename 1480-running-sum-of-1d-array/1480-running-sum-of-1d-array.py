class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp=0
        res=[]
        
        for i in nums:
            temp+=i
            res.append(temp)

        return res