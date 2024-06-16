/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
/*
 * dfs 돌면서 다음 노드 없을 때 지금까지 건너온 노드 밸류로 숫자 만들어 result에 추가
 * value는 전역 벡터에 집어넣어서 push pop 하기
 */

  #include <vector>
  using namespace std;

  class Solution {
  public:
        int GetNum(vector<int>& values) {
            int result = 0;
            for (int i = 0; i < values.size(); ++i) {
                result = (10 * result) + values[i];
            }
            return result;
        }
      void dfs(vector<int>& values, TreeNode* node, int& ssum) {
        // leaf 노드 도달
        if (!(node->left) && !(node->right)) {
          ssum += GetNum(values);
          return;
        }

        if (node->left) {
          values.push_back(node->left->val);
          dfs(values, node->left, ssum);
          values.pop_back();
        }
        if (node->right) {
          values.push_back(node->right->val);
          dfs(values, node->right, ssum);
          values.pop_back();
        }
      }

      int sumNumbers(TreeNode* root) {
         vector<int> values;
         int ssum = 0;

         values.push_back(root->val);
         dfs(values, root, ssum);

         return ssum;

       }
  };

