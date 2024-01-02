class Solution:
    def mutualDiff(self, a, b, c, k):
        if a - b > k or b - c > k or a - c > k:
            return True
        return False

    def divideArray(self, nums, k):
        ans = []
        nums.sort()

        for i in range(0, len(nums), 3):
            if self.mutualDiff(nums[i + 2], nums[i + 1], nums[i], k):
                return ans

        for i in range(0, len(nums), 3):
            ans.append([nums[i], nums[i + 1], nums[i + 2]])

        return ans