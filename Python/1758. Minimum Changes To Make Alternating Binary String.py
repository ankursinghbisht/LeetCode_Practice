class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        operations = 0
        for i in range(n):
            if (i % 2 == int(s[i])):
                operations += 1
        return min(operations, n - operations)
