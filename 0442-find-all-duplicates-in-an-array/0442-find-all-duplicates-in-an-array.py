class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap={}
        duplicate=[]
        for v in nums:
            if v not in hashmap:
                hashmap[v]=1
            else:
                hashmap[v]+=1
        for key,value in hashmap.items():
            if value>1:
                duplicate.append(key)
        return duplicate
        