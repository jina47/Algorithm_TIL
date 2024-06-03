#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isPalindrome(int x) {
    char buffer[20];
    sprintf(buffer,"%d",x);
    // char *itoa(int value, char *str, int radix(진수));
    // char *itoa(int x, char *buffer, int 10);
    // itoa(x, buffer, 10);
    // itoa는 compiler에 따라 안 돌아갈 수 있음
    // c++에서는 <string>에서 std::to_string() 쓸 수 있음

    int s_len = strlen(buffer);
    int i = 0;
    int j = s_len-1;
    bool answer = true;
    while (i < j){
        if (buffer[i] != buffer[j]) {
            answer = false;
            break;
        }
        i++;
        j--;
    }
    free(buffer);
    return answer;
}


// solution version
// bool isPalindrome(int x){
//     if(x<0 || x!=0 && x%10 ==0 ) return false;
//     int check=0;
//     while(x>check){
//         check = check*10 + x%10;
//         x/=10;
//     }
//     return (x==check || x==check/10);
// }