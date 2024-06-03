#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct TreeNode {
     int val;
     struct TreeNode *left;
     struct TreeNode *right;
 };


void dfs(struct TreeNode* curnode, char* path, char** answer, int* answerSize){
    if (curnode->left == NULL && curnode->right == NULL) {
        // path를 복사해서 새로운 메모리 공간에 저장
        answer[*answerSize] = strdup(path);
        (*answerSize)++;
        return;
    }

    if (curnode->left){
        char *left_path = (char*)malloc(100 * sizeof(char));
        sprintf(left_path, "%s->%d", path, curnode->left->val);
        dfs(curnode->left, left_path, answer, answerSize);
        free(left_path);
    }
    if (curnode->right){
        char *right_path = (char*)malloc(100 * sizeof(char));
        sprintf(right_path, "%s->%d", path, curnode->right->val);
        dfs(curnode->right, right_path, answer, answerSize);
        free(right_path);
    }
}

char** binaryTreePaths(struct TreeNode* root, int* returnSize) {
    // ans는 포인터를 담는 메모리가 할당되는 것, 일반적으로 포인터의 크기는 4 또는 8바이트임
    char** answer = (char**)malloc(100 * sizeof(char*));
    // 경로들의 개수를 저장할 변수 초기화
    *returnSize = 0;
    // 이진 트리가 비어있는 경우, 빈 배열 반환
    if (root == NULL) return answer;
    
    char path[1000];
    // 정수를 str로 변환 저장
    sprintf(path, "%d", root->val);
    dfs(root, path, answer, returnSize);
    return answer;
}


// void DFS(struct TreeNode* node, char **strArray, int *strIndex, int length, char *buffer){
//     length += sprintf(buffer+length, "%d", node->val);
//     if(!node->left && !node->right){
//         *(strArray+*strIndex) = malloc(600*sizeof(char));
//         strcpy(*(strArray+*strIndex), buffer);
//         (*strIndex)++;
//     } else {
//         length += sprintf(buffer+length, "->");
//         if(node->left){
//             DFS(node->left, strArray, strIndex, length, buffer);
//         }
//         if(node->right){
//             DFS(node->right, strArray, strIndex, length, buffer);
//         }
//     }
// }
// char ** binaryTreePaths(struct TreeNode* root, int* returnSize){
//     char **ans = malloc(50*sizeof(char *));
//     int strIndex = 0;
//     char buffer[600];
//     DFS(root, ans, &strIndex, 0, buffer);
//     *returnSize = strIndex;
//     return ans;
// }

