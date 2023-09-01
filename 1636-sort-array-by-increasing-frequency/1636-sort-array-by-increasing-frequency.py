class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        di=Counter(nums)
        li=list(di.items())
        
        li.sort(key=lambda x:(x[1],-x[0])) #val, freq 
        
        #largest number is smallest negative num
        res=[]
        for val,freq in (li):
            res+=[val]*freq
        return res