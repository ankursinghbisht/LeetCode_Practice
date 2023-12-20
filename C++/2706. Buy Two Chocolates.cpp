#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int buyChoco(vector<int>& prices, int money)
    {
        int a = 0, b = 1;
        for (int i = 2; i < prices.size(); ++i)
        {
            if (prices[b] >= prices[i])
            {
                if (prices[a] > prices[b])
                    a = b;

                b = i;
            }
            else if (b != i && prices[a] > prices[i])
                a = i;

        }

        if (prices[a] + prices[b] <= money)
            return money - (prices[b] + prices[a]);
        return money;
    }
};
