class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=''
        for i in s.lower():
            if i.isnumeric() or i.isalpha():
                string+=i
        if string==string[::-1]:
            return True
        return False