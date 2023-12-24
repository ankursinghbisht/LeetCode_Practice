from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        vec = [(nums[i], i) for i in range(n)]
        vec.sort()

        ans = 0

        for value, index in vec:
            if nums[index] > 0:
                ans += nums[index]
                nums[index] *= -1
                if index - 1 >= 0:
                    nums[index - 1] = abs(nums[index - 1]) * -1
                if index + 1 < n:
                    nums[index + 1] = abs(nums[index + 1]) * -1

        return ans
