#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPathCrossing(string path)
    {
        set<string>hash;
        int x = 0, y = 0;
        hash.insert("0-0");
        for (int i = 0;i < path.size();++i)
        {
            if (path[i] == 'N')
                ++y;
            else if (path[i] == 'S')
                --y;
            else if (path[i] == 'E')
                ++x;
            else
                --x;

            string temp = to_string(x) + '-' + to_string(y);
            if (hash.find(temp) != hash.end())
                return true;
            else
                hash.insert(temp);
        }
        return false;

    }
};