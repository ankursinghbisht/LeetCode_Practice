#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(string s)
    {
        int n = s.size(), operations = 0;
        for (int i = 0; i < n; ++i) {
            if ((i & 1) == (s[i] - '0')) {
                ++operations;
            }
        }
        return min(operations, n - operations);
    }
};