/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// 트리 탐색하며 parent 관계 세팅
// p, q 각각 부모 탐색하며 visited 체크. 이미 방문한 노드 갈시 여기가 답
class Solution {
public:
    unordered_map<TreeNode*, TreeNode*> parent;

    void SetParent(TreeNode* node, TreeNode* pare) {
      parent[node] = pare;
      
      if (node->left) {
        SetParent(node->left, node);
      }
      if (node->right) {
        SetParent(node->right, node);
      }
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
       SetParent(root, nullptr); 

       unordered_set<TreeNode*> s;

       TreeNode* temp1 = p;
        s.insert(temp1);

       while (parent[temp1]) {
         temp1 = parent[temp1];
         
         s.insert(temp1);
        }

       temp1 = q;
       
       while (s.find(temp1) == s.end()) {
         temp1 = parent[temp1];
       }

       return temp1;
};
