# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.nums = []

    def solve(self, a, b):
        if a == b:
            return None
        mid = (a + b) // 2
        root = TreeNode(self.nums[mid])
        root.left = self.solve(a, mid)
        root.right = self.solve(mid + 1, b)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.solve(0, len(nums))