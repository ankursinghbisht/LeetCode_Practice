#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int totalSteps(vector<int>& nums) {
        stack<pair<int, int>> st;
        int n = nums.size();
        int ans = 0;

        st.push({ nums[n - 1],0 });

        for (int i = n - 2;i >= 0;i--) {
            int cnt = 0;
            while (!st.empty() && nums[i] > st.top().first) {
                cnt = max(cnt + 1, st.top().second);
                st.pop();
            }
            ans = max(ans, cnt);
            st.push({ nums[i],cnt });
        }
        return ans;
    }
};
