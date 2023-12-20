#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    // Function to calculate the minimum number of flips required
    int minFlips(int a, int b, int c) {
        int ans = 0;

        // Iterate through each bit of a, b, and c
        while (a || b || c)
        {
            // Extract the least significant bits
            int bitA = a & 1;
            int bitB = b & 1;
            int bitC = c & 1;

            // Check if the current bit in c is the result of OR operation on bits from a and b
            if ((bitA | bitB) != bitC)
            {
                // If not, increment the answer based on the specific conditions
                if (bitC == 1)
                    ans += 1;  // Flip from 0 to 1 in c
                else
                    ans += (bitA + bitB);  // Flip from 1 to 0 in c

            }

            // Right shift to process the next bit
            a >>= 1;
            b >>= 1;
            c >>= 1;
        }

        return ans;
    }
};
