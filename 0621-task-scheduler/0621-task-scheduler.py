class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks) #Counter() is a hashmap to count elements inbuilt in python
        maxHeap=[-cnt for cnt in count.values()] #-cnt is because max heap in python is done by negating min heap
        heapq.heapify(maxHeap) #creating a heap
        
        time=0
        q=deque() #pair of values [-cnt, idleTime]
        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n]) #n=idletime
            if q and q[0][1]==time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
               
                
                
        
        