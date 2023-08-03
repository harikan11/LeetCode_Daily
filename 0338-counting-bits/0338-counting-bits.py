class Solution:
    def countBits(self, n: int) -> List[int]:
        
        counts=[]
        for i in range(n+1):
            binary=bin(i)
            count=binary.count("1")
            counts.append(count)
        return counts
            
            