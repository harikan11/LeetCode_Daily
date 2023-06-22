class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            
            freq[num] = freq.get(num, 0) + 1
            
        heap=[]
        for num,count in freq.items():
            if len(heap)<k:
                heapq.heappush(heap,(count,num))
        
            elif count > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))
        
        # Step 3: Return the elements in the heap
        return [num for count, num in heap]

        heap=[]
        
        for i in range(k):
            heapq
