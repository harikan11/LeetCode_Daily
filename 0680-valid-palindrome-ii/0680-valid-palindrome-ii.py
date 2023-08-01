class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validPal(s, flag):
            if len(s) < 2: return True
            if s[0] == s[-1]: return validPal(s[1:-1], flag)
            if flag: return validPal(s[1:], False) or validPal(s[:-1], False)
            return False
        return validPal(s, True)