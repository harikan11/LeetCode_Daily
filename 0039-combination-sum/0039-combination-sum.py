class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return
            
            
            if i>=len(candidates) or total>target: #impossible condition
                return
            #to select an element
            
            
            curr.append(candidates[i])
            dfs(i,curr,total+candidates[i])
            curr.pop()
            
            
            #to not select an element
            dfs(i+1,curr,total) #element is not added so the total is left the same
            
        dfs(0,[],0)
        return res