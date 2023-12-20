class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0

        # Iterate through each bit of a, b, and c
        while a or b or c:
            # Extract the least significant bits
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            # Check if the current bit in c is the result of OR operation on bits from a and b
            if (bit_a | bit_b) != bit_c:
                # If not, increment the answer based on the specific conditions
                if bit_c == 1:
                    ans += 1  # Flip from 0 to 1 in c
                else:
                    ans += bit_a + bit_b  # Flip from 1 to 0 in c

            # Right shift to process the next bit
            a >>= 1
            b >>= 1
            c >>= 1

        return ans