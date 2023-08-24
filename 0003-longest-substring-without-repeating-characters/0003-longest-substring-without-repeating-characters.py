class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        hash_set = {}
        max_len = 0
        for r in range(len(s)):
            
            if s[r] in hash_set:

                # changes l only if its greater than current l
                # for test case such as abba
                if hash_set[s[r]]+1>l: 
                    l = hash_set[s[r]]+1
            
            hash_set[s[r]] = r 
            max_len = max(max_len, r-l+1)

        return max_len