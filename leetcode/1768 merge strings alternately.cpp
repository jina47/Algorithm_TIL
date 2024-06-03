#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int a = word1.length();
        int b = word2.length();
        int c = min(a, b);
        string answer = "";

        for (int i=0; i<c; i++) {
            answer += word1[i];
            answer += word2[i];
        }
        if (a > c){
            for (int i=c; i<a; i++) {
                answer += word1[i];
            }
        }
        else if (b > c) {
            for (int i=c; i<b; i++) {
                answer += word2[i];
            }
        }
        return answer;
    }
};