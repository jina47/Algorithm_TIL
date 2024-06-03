#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int cnt = 0;
        int i = 0; 
        while (cnt < nums.size()) {
            if (nums[i] == 0) {
                nums.erase(nums.begin()+i);
                nums.push_back(0);
            }
            else {
                i += 1;
            }
            cnt += 1;
        }
    }
};