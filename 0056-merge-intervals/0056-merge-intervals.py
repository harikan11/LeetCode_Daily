class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        res = [sorted_intervals[0]]
        for interval in sorted_intervals[1:]:
            #the next node's smallest value is smaller than the prev node's largest value, then overlapping
            if interval[0] <= res[-1][1]:
                #left boundary is the largest value
                res[-1][1]=max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res
            
        
        
        
        