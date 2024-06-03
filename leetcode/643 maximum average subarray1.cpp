#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sumNum = std::accumulate(nums.begin(), nums.begin() + k, 0.0);
        double maxNum = sumNum;
        
        for (int i=1; i<nums.size()-k+1; i++) {
            sumNum = sumNum - nums[i-1] + nums[i-1+k];
            if (maxNum < sumNum) {
                maxNum = sumNum;
            }
        }
        return (maxNum / k) ;
    }
};