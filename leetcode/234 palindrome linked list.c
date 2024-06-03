#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};


struct ListNode* reverse(struct ListNode* mid){
    struct ListNode* head = mid;
    struct ListNode* prev = NULL;
    struct ListNode* temp = NULL;

    while (head) {
        temp = head->next;
        head->next = prev;
        prev = head;
        head = temp;
    }
    return prev;
}

bool isPalindrome(struct ListNode* head) {
    // mid 찾기
    struct ListNode* slow = head;
    struct ListNode* fast = head;

    int cnt = 0;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        cnt++;
    }
    // mid 는 slow -> mid 부터 reverse
    struct ListNode* right = reverse(slow);
    int i = 0;
    bool flag = true;
    while (i < cnt) {
        if (head->val != right->val) {
            flag = false;
            break;
        }
        head = head->next;
        right = right->next;
        i++;
    }
    return flag;
}

