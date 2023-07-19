class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas=0
        curr_gas=0
        start_index=0
        for i in range(len(gas)):
            curr_gas+=gas[i]-cost[i]
            total_gas+=gas[i]-cost[i]
            
            if curr_gas<0:
                curr_gas=0
                start_index=i+1
                
        if total_gas<0:
            return -1
        else:
            return start_index