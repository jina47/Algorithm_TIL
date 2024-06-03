#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int findCenter(int** edges, int edgesSize, int* edgesColSize) {
    int u1 = **edges;
    int v1 = *(*edges+1);
    // printf("%d, %d\n", u1, v1); // 1, 10

    int u2 = **(edges+1);
    int v2 = *(*(edges+1)+1);
    // printf("%d, %d\n", u2, v2); // 2. 11

    int ans = -1;
    if (u1 == u2 || u1 == v2) {
        ans = u1;
    } 
    else if (v1 == u2 || v1 == v2) {
        ans = v2;
    }
    return ans;
}

int main() {
    // 예시로 사용할 edges 배열 생성
    int edgesSize = 4;
    int edgesColSize[edgesSize];
    for (int i = 0; i < edgesSize; i++) {
        edgesColSize[i] = 2; // 모든 엣지의 크기는 2입니다.
    }

    int** edges = malloc(edgesSize * sizeof(int*));
    for (int i = 0; i < edgesSize; i++) {
        edges[i] = malloc(2 * sizeof(int));
    }

    // 예시로 사용할 edges 배열 초기화
    edges[0][0] = 1; edges[0][1] = 10;
    edges[1][0] = 2; edges[1][1] = 11;
    edges[2][0] = 3; edges[2][1] = 4;
    edges[3][0] = 4; edges[3][1] = 1;

    // findCenter 함수 호출
    int answer = findCenter(edges, edgesSize, edgesColSize);

    // 메모리 해제
    for (int i = 0; i < edgesSize; i++) {
        free(edges[i]);
    }
    free(edges);

    return 0;
}