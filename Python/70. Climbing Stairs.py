class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        prev, current = 1, 1

        for i in range(2, n + 1):
            next_val = prev + current
            prev, current = current, next_val

        return current