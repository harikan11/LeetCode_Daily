class Solution:
    def primePalindrome(self, n: int) -> int:
        
        def isPali(x):
            return str(x)==str(x)[::-1]
        def isprime(x):
            if x<2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        while True:
            if isPali(n) and isprime(n):
                return n
            n+=1
            if 10**7<n<10**8:
                n=10**8
            
            