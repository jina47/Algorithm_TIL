#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 로컬에서는 답이 잘 나오는데 리트코드에서 틀리는 이유? -> dp 배열 초기화 문제!
// int dp[size][size];는 되는데 초기화가 안되고 int dp[size][size] = {0};은 안됨
// int dp[size][szie];처럼 하려면 for문 두번 써서 0으로 값을 다 초기화해야함
// int dp[1000][1000] = {0}; 으로 하면 가장 최대 길이로 설정해서 메모리 많이 써서 초기화 가능
char* longestPalindrome(char* s) {
    int size = strlen(s); 
    int dp[1000][1000] = {0};
    
    int left = 0;
    int right = 0;
    char* substart = s;

    for (int i=0; i<size; i++){
        dp[i][i] = 1;

        if (i < size-1 && s[i] == s[i+1]) {
            dp[i][i+1] = 1;
            left = i;
            right = i+1;
            substart = (s+i);
        }
    }

    for (int len = 3; len < size+1; len++){
        for (int i=0; i < size-len+1; i++){
            int j = i + len - 1;
            if (s[i] == s[j] && dp[i+1][j-1] == 1){
                dp[i][j] = 1;
                left = i;
                right = j;
                substart = (s+i);
            }
        }
    }

    int ans_size = right - left + 1;
    char* ans = (char*)malloc((ans_size + 1)*sizeof(char));
    
    // for문, memcpy, strncpy 다 가능

    // for (int i=0; i < ans_size; i++){
    //     ans[i] = s[left+i];
    // }
    
    // memcpy(ans, &s[left], (right - left + 1) * sizeof(char));
    
    strncpy(ans, substart, ans_size);
    ans[ans_size] = '\0';
    return ans;
}

// 개인적으로는 이 버전이 더 좋음
// char* longestPalindrome(char* s) {
//     int size = strlen(s); 
//     int dp[1000][1000] = {0};
    
//     int left = 0;
//     int right = 0;

//     for (int i=0; i<size; i++){
//         dp[i][i] = 1;

//         if (i < size-1 && s[i] == s[i+1]) {
//             dp[i][i+1] = 1;
//             left = i;
//             right = i+1;
//         }
//     }

//     for (int len = 3; len < size+1; len++){
//         for (int i=0; i < size-len+1; i++){
//             int j = i + len - 1;
//             if (s[i] == s[j] && dp[i+1][j-1] == 1){
//                 dp[i][j] = 1;
//                 left = i;
//                 right = j;
//             }
//         }
//     }

//     int ans_size = right - left + 1;
//     char* ans = (char*)malloc((ans_size + 1)*sizeof(char));
//     for (int i=0; i < ans_size; i++){
//         ans[i] = s[left+i];
//     }
//     // memcpy(ans, &s[left], (right - left + 1) * sizeof(char));

//     ans[ans_size] = '\0';
//     return ans;
// }


int main(){
    char s[] = "bacabab";
    char* answer = longestPalindrome(s);
    printf("%s\n", answer);
    free(answer);
    return 0;
}

// solution 
// char* longestPalindrome(char* s) {
//     char *start, *end;
//     char *p = s, *subStart = s;
//     int maxLen = 1;
//     while(*p){
//         start = p; end = p;
        
//         while(*(end+1) && *(end+1) == *end){
//             end++; // skip duplicates
//         }
//         p = end + 1;
        
//         while(*(end + 1) && (start > s) && *(end + 1) == *(start - 1)){
//             start--;
//             end++;
//         }
//         if(end - start + 1 > maxLen){
//             maxLen = end - start + 1;
//             subStart = start;
//         }
//     }
    
//     char *rst = (char *) calloc(maxLen + 1, sizeof(char));
//     strncpy(rst, subStart, maxLen);
//     return rst;
// }

//python 버전
// class Solution:
//     def longestPalindrome(self, s: str) -> str:
//         if len(s) <= 1:
//             return s
//         i,l=0,0
//         for j in range(len(s)):
//             if s[j-l: j+1] == s[j-l: j+1][::-1]:
//                 i, l = j-l, l+1
//                 # print(s[i: i+l])
//             elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
//                 i, l = j-l-1, l+2
//                 # print(s[i: i+l])
//         return s[i: i+l]