class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        words = sorted(words, key = len)
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    if words[i] not in result:
                        result.append(words[i])

        return result
        