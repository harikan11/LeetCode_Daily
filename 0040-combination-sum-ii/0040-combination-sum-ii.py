class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return
            if i==len(candidates) or total>target: #impossible condition
                return
            
            #to select an element
            
            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])
            curr.pop()
            
            #to not select an element
            j=i+1
            
            while j<len(candidates) and candidates[j]==candidates[i]:
                j+=1
            dfs(j,curr,total)
        dfs(0,[],0)
        return res
            