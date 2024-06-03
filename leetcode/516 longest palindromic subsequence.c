#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int longestPalindromeSubseq(char* s) {
    //삭제는 할 수 있는데 order는 바꾸면 안됨
    int dp[1000][1000] = {0};
    int s_len = strlen(s);

    // 연속된 문자열(2글자)의 경우 값이 다르면 1개 삭제
    for (int i=0; i < s_len-1; i++){
        if (s[i] != s[i+1]){
            dp[i][i+1] = 1;
        }
    }

    // 3글자 이상의 문자열을 볼 때 최소로 삭제해야 하는 숫자를 담기
    for (int len = 3; len < s_len + 1; len++) {
        for (int i=0; i < s_len - len + 1; i++) {
            int j = i + len - 1;
            if (s[i] == s[j]){
                dp[i][j] = dp[i+1][j-1];
            }
            else if (s[i] != s[j]){
                dp[i][j] = (dp[i][j-1] < dp[i+1][j]) ? dp[i][j-1] + 1 : dp[i+1][j] + 1; 
            }
        }
    }
    return s_len - dp[0][s_len-1];
}