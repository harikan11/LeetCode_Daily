class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrace(cur, ind):
            if ind == len(s):
                result.append(cur)
                return
            
            temp = ""

            for i in range(ind, len(s)):
                temp += s[i]
                if temp == temp[::-1]:
                    backtrace(cur + [temp], i + 1)
        backtrace([], 0)
        return result