class Solution {
public:
    bool halvesAreAlike(string s)
    {
        int half = s.size() / 2, i = 0, j = half, val = 0;


        for (;i < half;++i, ++j)
        {
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')
                ++val;

            if (s[j] == 'a' || s[j] == 'e' || s[j] == 'i' || s[j] == 'o' || s[j] == 'u' || s[j] == 'A' || s[j] == 'E' || s[j] == 'I' || s[j] == 'O' || s[j] == 'U')
                --val;
        }

        if (val != 0)
            return false;
        return true;

    }
};