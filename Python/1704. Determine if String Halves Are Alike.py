class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        i, j, val = 0, half, 0

        for _ in range(half):
            if s[i] in 'aeiouAEIOU':
                val += 1

            if s[j] in 'aeiouAEIOU':
                val -= 1

            i += 1
            j += 1

        return val == 0