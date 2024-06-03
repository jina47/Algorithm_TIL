#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string reverseVowels(string s) {
        string vowel = "aeiouAEIOU";
        
        int i = 0;
        int j = s.size()-1;
        while (j > i) {
            if (vowel.find(s[i]) != string::npos) {
                while (j > i) {
                    if (vowel.find(s[j]) != string::npos) {
                        swap(s[i++], s[j--]);
                        break;
                    }
                    else {
                        j -= 1;
                    }
                }
            }
            else {
                i += 1;
            }
        } 
        return s;
    }
};