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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
      if (!root) return {};

       queue<TreeNode*> q;
       q.push(root);

       vector<vector<int>> answer;
       int level = 0;

       while (!q.empty()) {
         int n = q.size();
         
         answer.push_back(vector<int>{});
         TreeNode* p;

         for (int i = 0; i < n; ++i) {
           p = q.front(); q.pop();

           answer[level].push_back(p->val);

           if (p->left) q.push(p->left);
           if (p->right) q.push(p->right);
         }
         level++;
       }

       for (int i = 1; i < answer.size(); i += 2) {
         reverse(answer[i].begin(), answer[i].end());
       }

       return answer;
    }
};
