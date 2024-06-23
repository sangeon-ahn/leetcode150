/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        Node* dummy = new Node(-1);
        dummy->next = root;

        while (dummy->next) {
            Node* cur = dummy->next;
            Node* prev = dummy;

            dummy->next = nullptr;

            while (cur) {
                if (cur->left) {
                    prev->next = cur->left;
                    prev = prev->next;
                }
                if (cur->right) {
                    prev->next = cur->right;
                    prev = prev->next;
                }
                cur = cur->next;
            }
        }

        delete dummy;
        return root;
    }
};
