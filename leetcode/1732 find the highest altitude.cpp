#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int cur = 0;
        int max_al = 0;
        for (int i=0; i<gain.size(); i++) {
            cur = cur + gain[i];
            if (cur > max_al) {
                max_al = cur;
            }
        }
        return max_al;
    }
};