class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                count += 1
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if (s[i] == ')' and ch == '(') or (s[i] == ']' and ch == '[') or (s[i] == '}' and ch == '{'):
                    pass
                else:
                    return False
                count -= 1
        return count == 0
                
            