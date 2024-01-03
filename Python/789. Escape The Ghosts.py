class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])

        for it in ghosts:
            if abs(it[0] - target[0]) + abs(it[1] - target[1]) <= dist:
                return False

        return True
