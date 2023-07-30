class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap={}
        for i,v in enumerate(nums):
            if v not in hashmap:
                hashmap[v]=1
            else:
                hashmap[v]+=1
        for key,value in hashmap.items():
            if value>1:
                return key
                