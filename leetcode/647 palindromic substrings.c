#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int countSubstrings(char* s) {
    int answer = 0;
    int len = strlen(s);
    int dp[1000][1000] = {{0}}; // 중괄호 하나해도 됨

    // 1글자나 2글자는 모두 palindrome
    for (int i=0; i < len; i++) {
        // 1글자인 경우
        dp[i][i] = 1;
        answer++;

        // 2글자인 경우 (첫 글자와 마지막 글자가 다른 경우)
        if (i < len-1 && s[i] == s[i+1]) {
            dp[i][i+1] = 1;
            answer++;
        }
    }

    // 3글자 이상인 경우 palindrome 확인
    // 첫 글자와 마지막 글자가 같으면 dp[i+1][j-1] = 1 인지 확인
    // 인덱스 범위 주의
    for (int length=3; length < len+1; length++) {
        for (int i=0; i < len - length + 1; i++) {
            int j = i + length - 1;
            if (s[i] == s[j] && dp[i+1][j-1] == 1) {
                dp[i][j] = 1;
                answer++;
            }
        }
    }


    return answer;
}   


// c++ 버전
// class Solution {
// public:
//     int countSubstrings(string s) {
//         int n = s.length();
//         vector<vector<bool>> dp(n, vector<bool>(n, false));
//         int count = 0;
//         for (int i = n - 1; i >= 0; i--) {
//             for (int j = i; j < n; j++) {
//                 if (i == j) {
//                     dp[i][j] = true;
//                 } else if (j == i + 1) {
//                     dp[i][j] = (s[i] == s[j]);
//                 } else {
//                     dp[i][j] = (s[i] == s[j]) && dp[i + 1][j - 1];
//                 }
//                 if (dp[i][j]) {
//                     count++;
//                 }
//             }
//         }
//         return count;
//     }
// };


// 더 빠르고 메모리 덜 쓰는 방법
// class Solution {
// private:
//     int count = 0;
// public:
//     int countSubstrings(string s) {
//         if (s.length() == 0) {
//             return 0;
//         }
//         for (int i = 0; i < s.length(); i++) {
//             help(s, i, i); // 홀수 길이의 팰린드롬 검사 
//             help(s, i, i + 1); // 짝수 길이의 팰린드롬 검사
//         }
//         return count;
//     }
// private:
//     void help(string& s, int left, int right) {
//         while (left >= 0 &&  s[left] == s[right] && right < s.size() ) {
//             count++;
//             left--;
//             right++;
//         }
//     }
// };