class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        res = sumi = sum(cardPoints[:k])
        left = k-1
        right = n-1
        while(left>=0):
            sumi-=cardPoints[left]
            sumi+=cardPoints[right]
            res = max(res,sumi)
            left-=1
            right-=1
        return res