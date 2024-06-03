#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result1(nums1.size());
        vector<int> result2(nums2.size());

        set<int> num1(nums1.begin(), nums1.end());
        set<int> num2(nums2.begin(), nums2.end());

        auto iter1 = set_difference(num1.begin(), num1.end(), num2.begin(), num2.end(), result1.begin());
        result1.erase(iter1, result1.end());

        auto iter2 = set_difference(num2.begin(), num2.end(), num1.begin(), num1.end(), result2.begin());
        result2.erase(iter2, result2.end());

        vector<vector<int>> answer = {result1, result2};
        return answer;
    }
};