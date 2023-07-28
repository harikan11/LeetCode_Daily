class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[] #stores letter and freq
        for letter in s:
            if stack and letter==stack[-1][0]:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([letter,1])
        return "".join(str(letter * count) for letter,count in stack)
            