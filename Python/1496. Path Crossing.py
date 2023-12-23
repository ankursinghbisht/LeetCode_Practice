class Solution:
    def isPathCrossing(self, path: str) -> bool:
        hash_set = set()
        x, y = 0, 0
        hash_set.add("0-0")

        for move in path:
            if move == 'N':
                y += 1
            elif move == 'S':
                y -= 1
            elif move == 'E':
                x += 1
            else:
                x -= 1

            temp = f"{x}-{y}"
            if temp in hash_set:
                return True
            else:
                hash_set.add(temp)

        return False
