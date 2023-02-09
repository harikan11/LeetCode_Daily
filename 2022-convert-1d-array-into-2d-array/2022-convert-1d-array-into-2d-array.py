class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        i, output=0,[]
        if m*n!=len(original):
            return []
        else:
            while i<len(original):
                output.append(original[i:(i:=i+n)])
            return output
       
            