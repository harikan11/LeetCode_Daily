class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        path=set() #to makesure we dont revisit the same node again
        
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r<0 or c<0) or (r>=rows or c>=cols) or (word[i]!=board[r][c]) or (r,c) in path: #out of bound conditions
                return False
            
            path.add((r,c))
            res=(dfs(r+1,c,i+1) or 
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1))
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False #did not find the word
        