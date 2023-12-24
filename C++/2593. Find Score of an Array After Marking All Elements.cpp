#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long findScore(vector<int>& nums)
    {
        vector<pair<int, int>>vec;
        for (int i = 0;i < nums.size();++i)
            vec.push_back({ nums[i],i });

        sort(vec.begin(), vec.end());

        long long ans = 0;

        for (auto it : vec)
        {
            if (nums[it.second] > 0)
            {
                ans += nums[it.second];
                nums[it.second] *= -1;
                if (it.second - 1 >= 0)
                    nums[it.second - 1] = abs(nums[it.second - 1]) * -1;
                if (it.second + 1 < nums.size())
                    nums[it.second + 1] = abs(nums[it.second + 1]) * -1;
            }
        }
        return ans;
    }
};