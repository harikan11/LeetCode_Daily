class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = sorted(Counter(s).values(), reverse=True)
        
        tot_deletions = 0
        next_unused_freq = len(s)
        for freq in frequencies:
            # It is impossible for the frequency to be higher
            next_unused_freq = min(next_unused_freq, freq)
            tot_deletions += freq - next_unused_freq

            # We cannot have another character with this frequency,
            # so decrement next_unused_freq
            if next_unused_freq > 0:
                next_unused_freq -= 1

        return tot_deletions
        