class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        first, last = -1, -1

        for i in range(len(nums_sorted)):
            if target == nums_sorted[i] and (i == 0 or (i > 0 and nums_sorted[i - 1] != target)):
                first = i
            if target == nums_sorted[i] and (i == len(nums_sorted) - 1 or (i < len(nums_sorted) - 1 and nums_sorted[i + 1] != target)):
                last = i

        return [first, last]