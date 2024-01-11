class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        hash = [0] * 26
        check = [0] * 26

        for i in s1:
            check[ord(i) - ord('a')] += 1

        i = 0
        j = 0

        while i < len(s1):
            hash[ord(s2[i]) - ord('a')] += 1
            i += 1

        if hash == check:
            return True

        while i < len(s2):
            hash[ord(s2[j]) - ord('a')] -= 1
            j += 1
            hash[ord(s2[i]) - ord('a')] += 1
            i += 1

            if hash == check:
                return True

        return False