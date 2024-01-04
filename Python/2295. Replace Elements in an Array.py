class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {}

        # Initialize dict with initial positions
        for i in range(len(nums)):
            mp[nums[i]] = i

        for op in operations:
            pos = mp[op[0]]
            nums[pos] = op[1]
            mp[op[1]] = pos

        return nums