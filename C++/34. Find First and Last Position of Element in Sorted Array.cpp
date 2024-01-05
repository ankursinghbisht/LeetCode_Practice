class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target)
    {
        sort(nums.begin(), nums.end());
        int first = -1, last = -1;
        for (int i = 0;i < nums.size();++i)
        {
            if (target == nums[i] && (i == 0 || (i > 0 && nums[i - 1] != target)))
                first = i;
            if (target == nums[i] && (i == nums.size() - 1 || (i < nums.size() - 1 && nums[i + 1] != target)))
                last = i;
        }
        return vector<int>({ first,last });
    }
};