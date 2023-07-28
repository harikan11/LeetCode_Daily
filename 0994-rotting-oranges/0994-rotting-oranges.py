class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        n,m = len(grid),len(grid[0])
        count, time = 0, -1
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    count+=1
                elif grid[i][j]==2:
                    queue.append((i,j))
        while len(queue)>0:
            rotten = []
            while len(queue)>0:
                rotten.append(queue.popleft())
            for orange in rotten:
                i,j = orange
                for a,b in dirs:
                    new_i, new_j = i+a, j+b
                    if 0<=new_i<n and 0<=new_j<m and grid[new_i][new_j]==1:
                        count-=1
                        grid[new_i][new_j]=2
                        queue.append((new_i,new_j))
            time+=1
        if not count:
            return max(time,0)
        else:
            return -1