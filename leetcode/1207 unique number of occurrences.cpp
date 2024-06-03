#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> check;
        for (int key : arr){
            if (check.count(key)) {
                check[key] += 1;
            }
            else {
                check[key] = 1;
            }
        }
        set<int> isUnique;
        for (auto &elem : check) {
            isUnique.insert(elem.second);
        }
        if (isUnique.size() == check.size()) {
            return true;
        }
        else {
            return false;
        }
    }
};