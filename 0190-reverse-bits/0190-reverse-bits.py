class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num=0
        
        for i in range(32):
            reversed_num=(reversed_num<<1) | (n&1)  #the | means it is a bitwise OR operation
            n>>=1
        return reversed_num