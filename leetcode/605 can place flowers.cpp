#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        for (int i=0; i < flowerbed.size(); i++){
            if (i == 0) {
                if (flowerbed.size() == 1 && flowerbed[0] == 0) {
                    n -= 1;
                }
                else {
                    if (flowerbed[0] == 0 && flowerbed[1] == 0) {
                        flowerbed[0] = 1;
                        n -= 1;
                    }
                }
            }
            else if (i == flowerbed.size()-1) {
                if (flowerbed[i-1] == 0 && flowerbed[i] == 0) {
                    flowerbed[i] = 1;
                    n -= 1;
                }
            }
            else if (0 < i < flowerbed.size()-1) {
                if (flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0) {
                    flowerbed[i] = 1;
                    n -= 1;
                }
            }
 
            if (n <= 0) {
                return true;
            }
        }
        return false;
    }
};