class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        heap=[(-v,k) for k,v in c.items()]
        heapq.heapify(heap)
        output=[]
        while heap:
            v,k=heapq.heappop(heap)
            output += [k] * -v
            
        return output
        