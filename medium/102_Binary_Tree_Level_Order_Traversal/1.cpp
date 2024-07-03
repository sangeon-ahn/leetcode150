#include <vector>
#include <iostream>
#include <queue>

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> answer;
        
        if (!root) return answer;

      queue<TreeNode*> q;
      q.push(root);
      
      
      int level = 0;
      while (!q.empty()) {
        answer.push_back(vector<int>{});
        int n = q.size();
        
        TreeNode* p;
        for (int i = 0; i < n; ++i) {
          p = q.front();

          answer[level].push_back(p->val);
          q.pop();
          if (p->left) q.push(p->left);
          if (p->right) q.push(p->right);
        }
        level++;
      }

      return answer;
    }
};

