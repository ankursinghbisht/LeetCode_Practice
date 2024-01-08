class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        my_set = set()
        for num in arr:
            if 2 * num in my_set or (num % 2 == 0 and num // 2 in my_set):
                return True
            my_set.add(num)
        return False