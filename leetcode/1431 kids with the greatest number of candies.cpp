#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        int maxNum = *max_element(candies.begin(), candies.end());
        for (int i=0; i < candies.size(); i++) {
            if (candies[i] + extraCandies >= maxNum) {
                result.push_back(true);
            }
            else {
                result.push_back(false);
            }
        }
        return result;
    }
};