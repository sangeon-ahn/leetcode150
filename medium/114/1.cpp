struct TreeNode {
  int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode() : val(0), left(nullptr), right(nullptr) {}
   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
   TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
/*
 * 일단, preorder로 트리 순회하며 싱글 링크드 리스트로 만드는 문제다.
 * 그냥 preorder 순회하며 큐에 넣고 다 넣으면 연결하면 끝인데, follow up에 공간복잡도 O(1)로
 * 풀 수 있냐고 물어본다.
 * 2 -> 3 -> 4
 * left sub tree 연결 다 하고, right sub tree 연결 다 하고, 2 -> 3 -> 4 순서로 연결하면 된다.
 *
 *
 *
*/

class Solution {
public:
    pair<TreeNode*, TreeNode*>  recur(TreeNode* node) {
      // node의 왼쪽, 오른쪽 서브트리 연결한 후 리턴된 노드 2개를 node 랑 엮은 후 node 리턴
      
      if (!node) return {nullptr, nullptr};
      if (!node->left && !node->right) return {node, node};

      pair<TreeNode*, TreeNode*> left_sub_tree = recur(node->left);
      pair<TreeNode*, TreeNode*> right_sub_tree = recur(node->right);
      
      if (left_sub_tree.first) {
        node->right = left_sub_tree.first;
        if (right_sub_tree.first) {
          left_sub_tree.second->right = right_sub_tree.first;
          return {node, right_sub_tree.second};
        }
        else {
          return {node, left_sub_tree.second};
        }
      }
      else {
        if (right_sub_tree.left) {
          node->right = right_sub_tree.first;
          return {node, right_sub_tree.second};
        }
        else return {node, node};
      }
    }
    void flatten(TreeNode* root) {
      recur(root);
    }
};
