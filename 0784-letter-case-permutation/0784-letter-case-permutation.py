class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output=[""]
        
        for c in s:
            temp=[]
            if c.isalpha():
                for o in output:
                    temp.append(o+c.lower())
                    temp.append(o+c.upper())
            else:
                 for o in output:
                    temp.append(o+c)
            output=temp
        return output
                
                    