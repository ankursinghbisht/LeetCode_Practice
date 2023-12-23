from collections import defaultdict


class Solution:
    def countCompleteSubarrays(self, nums):
        mp = defaultdict(int)
        all_counts = defaultdict(int)

        for n in nums:
            all_counts[n] += 1

        front, back, ans = 0, 0, 0

        while front < len(nums):
            mp[nums[front]] += 1

            while back <= front and len(mp) == len(all_counts):
                if mp[nums[back]] - 1 == 0:
                    del mp[nums[back]]
                else:
                    mp[nums[back]] -= 1

                back += 1
                ans += len(nums) - front

            front += 1

        return ans