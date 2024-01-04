from typing import List
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        st = []
        n = len(nums)
        ans = 0

        st.append((nums[n - 1], 0))

        for i in range(n - 2, -1, -1):
            cnt = 0

            while st and nums[i] > st[-1][0]:
                cnt = max(cnt + 1, st.pop()[1])

            ans = max(ans, cnt)
            st.append((nums[i], cnt))

        return ans