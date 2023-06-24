class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=min(strs)
        last=max(strs)
        
        prefix=''
        for string in range(min(len(first),len(last))):
                            
            if first[string]!=last[string]:
                break
            else:
                prefix+=first[string]
        return prefix
        
            