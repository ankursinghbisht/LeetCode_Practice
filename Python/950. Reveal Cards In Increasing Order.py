from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        ans = [0] * n
        deck.sort()
        indices = deque(range(n))

        for card in deck:
            ans[indices.popleft()] = card
            if indices:
                indices.append(indices.popleft())

        return ans
