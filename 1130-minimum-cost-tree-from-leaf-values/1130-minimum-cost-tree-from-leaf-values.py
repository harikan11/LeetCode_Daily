class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        res = 0
        for num in arr:
            while stack and stack[-1] <= num:
                abon = stack.pop()
                if stack:
                    res += abon * min(stack[-1], num)
                else:
                    res += abon * num
            stack.append(num)
        while len(stack) > 1:
            res += stack.pop() * stack[-1]
        return res
                