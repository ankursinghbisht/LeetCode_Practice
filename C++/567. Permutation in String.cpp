class Solution {

public:
    bool checkInclusion(string s1, string s2)
    {
        if (s2.size() < s1.size())
            return false;
        vector<int>hash(26, 0), check(26, 0);

        for (char i : s1)
            ++check[i - 'a'];

        int i = 0, j = 0;

        while (i < s1.size())
            ++hash[s2[i++] - 'a'];
        if (hash == check)
            return true;

        while (i < s2.size())
        {
            --hash[s2[j++] - 'a'];
            ++hash[s2[i++] - 'a'];
            if (hash == check)
                return true;
        }
        return false;
    }
};