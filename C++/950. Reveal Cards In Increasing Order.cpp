#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck)
    {
        vector<int> ans(deck.size(), 0);
        sort(deck.begin(), deck.end());
        queue<int> q;

        for (int i = 0; i < deck.size(); i++)
            q.push(i);

        for (int i = 0; i < deck.size(); i++)
        {
            ans[q.front()] = deck[i];
            q.pop();
            q.push(q.front());
            q.pop();
        }

        return ans;
    }
};