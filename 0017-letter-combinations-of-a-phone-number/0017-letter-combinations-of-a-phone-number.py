class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if not digits:
            return []
        mapping={'2':'abc',
                 '3':'def',
                 '4':'ghi',
                 '5':'jkl',
                 '6': 'mno',
                 '7':'pqrs',
                 '8':'tuv',
                 '9':'wxyz'}
        def backtrack(i,curr_string): #i to show which index we're at and curr_string to show the string we're building rn
            #base case
            if len(curr_string)==len(digits): #reached end of the digits so append the current string to res
                res.append(curr_string)
                return 
            for char in mapping[digits[i]]:
                backtrack(i+1,curr_string+char)
        if digits:
            backtrack(0,"")
            return res
                
            
            

            
             