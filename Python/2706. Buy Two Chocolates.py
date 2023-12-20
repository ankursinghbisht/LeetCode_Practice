class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        a = 0
        b = 1
        for i in range(2, len(prices)):
            if prices[b] >= prices[i]:
                if prices[a] > prices[b]:
                    a = b
                b = i
            elif b != i and prices[a] > prices[i]:
                a = i

        if prices[a] + prices[b] <= money:
            return money - (prices[b] + prices[a])
        return money
