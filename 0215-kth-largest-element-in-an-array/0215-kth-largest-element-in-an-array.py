class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in range(k):
            heapq.heappush(heap,nums[i])
        for i in range(k,len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]
                    