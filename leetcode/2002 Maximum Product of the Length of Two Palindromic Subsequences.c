// maximum product 구하기

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int maxLenPalindrome(char*s)  {
    int s_len = strlen(s);
    if (s_len < 2) {
        return s_len;
    }

    int dp[12][12] = {0};
    // 최소 삭제 index 개수 담기
    for (int i=0; i<s_len-1; i++){
        if (s[i] != s[i+1]) {
            dp[i][i+1] = 1;
        }
    }

    // 3글자 이상 볼 때 최소 삭제 인덱스
    for (int window = 3; window < s_len+1; window++) {
        for (int i=0; i<s_len-window+1; i++){
            int j = i + window -1;
            if (s[i] == s[j]) {
                dp[i][j] = dp[i+1][j-1];
            }
            else {
                dp[i][j] = (dp[i][j-1] < dp[i+1][j]) ? dp[i][j-1]+1 : dp[i+1][j]+1; 
            }
        }
    }

    return s_len - dp[0][s_len-1];
}

int dfs(int idx, int* visited, char*s, int ans) {
    // left와 right 동적 할당
    char *left = (char *)malloc((strlen(s) + 1) * sizeof(char));
    char *right = (char *)malloc((strlen(s) + 1) * sizeof(char));
    int l = 0;
    int r = 0;

    for (int i = 0; i < strlen(s); i++) {
        if (visited[i] == 1) {
            left[l] = s[i];
            l++;
        } else {
            right[r] = s[i];
            r++;
        }
    }
    left[l] = '\0';
    right[r] = '\0';

    // 각 substring 마다 max palidrome 길이 구하기
    int left_pal = maxLenPalindrome(left);
    int right_pal = maxLenPalindrome(right);

    // 두 개 곱이 ans보다 크면 ans 갱신
    if(left_pal * right_pal > ans) {
        ans = left_pal * right_pal;
    } 

    // 그 다음 left, right 탐색 위해 dfs (backtracking)
    for (int j = idx+1; j < strlen(s); j++) {
        visited[j] = 1;
        ans = dfs(j, visited, s, ans);
        visited[j] = 0;
    }

    // 동적 할당 해준 것은 해제
    free(left);
    free(right);
    return ans;
}

int maxProduct(char* s) {
    // s 로 만들 수 있는 substring left와 right로 나누기
    // permutation 으로 조합 가능 -> backtracking과 dfs로 가능
    int ans = 0;
    int s_len = strlen(s);
    int visited[12] = {0};
    // int *visited = (int *)malloc(s_len * sizeof(int));
    
    for (int i=0; i<s_len; i++) {
        visited[i] = 1;
        ans = dfs(i, visited, s, ans);
        visited[i] = 0;
    }

    return ans;
}

int main() {
    char s[] = "ellellllltll";
    int answer = maxProduct(s);
    return 0;
}