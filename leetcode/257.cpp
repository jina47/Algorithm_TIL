#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void dfs(TreeNode* curnode, string path, vector<string>& answer) {
        if (curnode->left == nullptr and curnode->right == nullptr){
            answer.push_back(path);
            return ;
        }
        for (int i=0; i < 2; i++){
            if (i == 0 && curnode->left!=nullptr){
                dfs(curnode->left, path+"->"+to_string(curnode->left->val), answer);
            }
            else if (i == 1 && curnode->right!=nullptr) {
                dfs(curnode->right, path+"->"+to_string(curnode->right->val), answer);
            }
        }

    }

    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> answer;
        dfs(root, to_string(root->val), answer);
        return answer;
    }
};