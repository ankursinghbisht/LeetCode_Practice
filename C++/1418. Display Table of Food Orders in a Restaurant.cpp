#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    vector<vector<string>> displayTable(vector<vector<string>>& orders) {
        map<int, map<string, int>> tableMap;
        set<string> dishSet;

        for (const vector<string>& order : orders) {
            int tableNumber = stoi(order[1]);
            string dish = order[2];

            dishSet.insert(dish);
            tableMap[tableNumber][dish]++;
        }

        vector<vector<string>> result;

        // Prepare headings
        vector<string> headings = { "Table" };
        for (const string& dish : dishSet) {
            headings.push_back(dish);
        }
        result.push_back(headings);

        // Fill the table
        for (const auto& entry : tableMap) {
            int tableNumber = entry.first;
            const map<string, int>& dishCount = entry.second;

            vector<string> row = { to_string(tableNumber) };
            for (const string& dish : dishSet) {
                if (dishCount.count(dish)) {
                    row.push_back(to_string(dishCount.at(dish)));
                }
                else {
                    row.push_back("0");
                }
            }
            result.push_back(row);
        }

        return result;
    }
};