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
class BSTIterator {
public:
    vector<TreeNode*> nodes;
    int cursor = 0;
    BSTIterator(TreeNode* root) {
      inorder(root); 
    }
    
    int next() {
      int prev_cursor = cursor;
      cursor++;
      return nodes[prev_cursor]->val;
    }
    
    bool hasNext() {
       return nodes.size() > cursor; 
    }

    void inorder(TreeNode* node) {
      if (node) {
        inorder(node->left);
        nodes.push_back(node);
        inorder(node->right);
      }
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
