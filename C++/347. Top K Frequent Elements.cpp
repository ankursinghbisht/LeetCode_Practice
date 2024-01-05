class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k)
    {
        map<int, int>hash;

        vector<int>ans;

        for (auto it : nums)
            ++hash[it];

        priority_queue<pair<int, int>>q;

        for (auto it : hash)
        {
            q.push({ it.second,it.first });
            if (q.size() > hash.size() - k)
            {
                ans.push_back(q.top().second);
                q.pop();
            }
        }



        return ans;
    }
};