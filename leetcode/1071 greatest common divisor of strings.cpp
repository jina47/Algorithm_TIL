#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 == "" && str2 == "") {
            return "";
        }
        else if (str1 == "" ) {
            return str2;
        }
        else if (str2 == "") {
            return str1;
        }
        else {
            if (str1.size() < str2.size()) {
                string temp = str1;
                str1 = str2;
                str2 = temp;
            }

            int len = str2.size();

            if (str1.substr(0,len) == str2) {
                return gcdOfStrings(str1.substr(len), str2);
            }
            else {
                return "";
            }
        }
    }
};