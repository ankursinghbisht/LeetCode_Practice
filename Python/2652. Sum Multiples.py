class Solution:
    def cal(self, n, k):
        return k * (n // k) * (n // k + 1) // 2

    def sumOfMultiples(self, n: int) -> int:
        return (
            self.cal(n, 3)
            + self.cal(n, 5)
            + self.cal(n, 7)
            - self.cal(n, 3 * 5)
            - self.cal(n, 5 * 7)
            - self.cal(n, 3 * 7)
            + self.cal(n, 3 * 5 * 7)
        )