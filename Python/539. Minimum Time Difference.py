class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins = [0] * 1440

        for t in timePoints:
            h = int(t[:2])
            m = int(t[3:])

            if mins[h * 60 + m]:
                return 0
            mins[h * 60 + m] = 1

        ans = float('inf')
        pre = -1
        s = float('inf')
        e = -float('inf')

        for i in range(len(mins)):
            if mins[i]:
                if pre == -1:
                    pre = i
                else:
                    ans = min(ans, i - pre)
                    pre = i

                s = min(s, i)
                e = max(e, i)

        return min(ans, 1440 - (e - s))
