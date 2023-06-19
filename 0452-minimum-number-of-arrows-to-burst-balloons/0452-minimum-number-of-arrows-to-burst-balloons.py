class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
         # sort by end point   
        points.sort(key = lambda x: x[1])
        end = points[0][1]
        count = 1
        # iterate and count arrows
        for s,e in points[1:]:
            if s > end:
                count += 1
                end = e
        
        return count