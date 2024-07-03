class Solution {
public:
    TreeNode* preOrder(TreeNode* node, TreeNode* p, TreeNode* q) {
        if (node == nullptr || node == p || node == q)
            return node;

        TreeNode* left = preOrder(node->left, p, q);
        TreeNode* right = preOrder(node->right, p, q);

        if (left == nullptr)
            return right;
        if (right == nullptr)
            return left;
        return node;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* answer =preOrder(root, p, q);
        return answer;
    }
};
