#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool mutualDiff(int a, int b, int c, int k)
    {
        if (a - b > k || b - c > k || a - c > k)
            return true;
        return false;
    }
    vector<vector<int>> divideArray(vector<int>& nums, int k)
    {
        vector<vector<int>>ans;
        sort(nums.begin(), nums.end());
        for (int i = 0;i < nums.size();i += 3)
            if (mutualDiff(nums[i + 2], nums[i + 1], nums[i], k))
                return ans;

        for (int i = 0;i < nums.size();i += 3)
            ans.push_back({ nums[i],nums[i + 1],nums[i + 2] });
        return ans;
    }
};