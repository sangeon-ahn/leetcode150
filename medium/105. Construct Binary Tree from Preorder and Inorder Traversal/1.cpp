#include <vector>
#include <unordered_map>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/**
 *     3
 *   /    \
 * 9        20
 *         /  \
 *        15   7
 * preorder = [3, 9, 20, 15, 7]
 * inorder = [9, 3, 15, 20, 7]
 * preorder만 가지고는 이진트리가 정확히 어떤 구조를 이루었는지 알 수 없다.
 * preorder값으로 이진 트리를 그려보면 한줄 구조도 가능하다.
 * 즉, a,b,c,...가 들어왔을 때 b가 a의 자식인 건 맞으나 c는 a의 자식일지 b의 자식일지 모른다. 그리고 b가 a의 왼쪽 자식인지 오른쪽 자식인지도 모른다.
 * 루트 노드만 위치가 확정적이고, 나머지 노드는 어디에 위치할지 모른다.
 * 이제 inorder를 보자.
 * [9, 3, 15, 20, 7]
 * inorder는 왼쪽 서브트리 -> 중앙노드 -> 오른쪽 서브트리 순서로 순회한다.
 * preorder를 통해 root node가 누구인지는 알 수 있다. -> 3
 * 이제 inorder를 보면, 3의 왼쪽에는 9가 있고 오른쪽엔 15, 20, 7이 있다.
 * 그럼 왼쪽 서브트리와 오른쪽 서브트리로 나눠지게 되는데, 이제 또 각각의 서브트리의 루트노드가 무엇인지를 파악해야한다.
 * 파악하는 법: preorder에서 왼쪽 서브트리의 노드가 모두 끝난 후에 나오는 가장 첫번째 노드가 오른쪽 서브트리의 루트노드다. 이 노드를 inorder에서 찾아서 이제 또 왼쪽 서브트리와 오른쪽 서브트리에 대해 재귀함수를 수행한다.
 * 이렇게 오른쪽 서브트리에 대한 작업은 모두 수행한거고, 왼쪽도 마찬가지로 서브루트노트를 구해야 한다. 서브루트노드 = inorder의 루트노드 왼쪽에 아무 노드도 없으면 왼쪽 서브트리가 없는거다. 있으면, 가장 preorder의 루트노드 바로 왼쪽위치의 노드가 왼쪽 서브트리의 루트노드다. 이렇게 구했으면 예를 자기 부모와 연결하고 다시 왼쪽 서브, 오른쪽 서브에 대해 재귀 수행.
 * 이런식으로 이진 트리를 만들면 된다.
*/

class Solution {
public:
    TreeNode* buildSubTree(vector<int>& preorder, vector<int>& inorder, int pre_left, int pre_right, int in_left, int in_right) {
        TreeNode* root = new TreeNode{preorder[pre_left]};
        int root_idx = 0;
        unordered_map<int, bool> m;
        for (int i = in_left; i <= in_right; ++i) {
            if (inorder[i] == root->val) {
                root_idx = i;
                break;
            }
            m[inorder[i]] = true;
        }

        int left_subtree_last_idx;
        for (left_subtree_last_idx = pre_left + 1;  left_subtree_last_idx <= pre_right; ++left_subtree_last_idx) {
            if (!m[preorder[left_subtree_last_idx]]) {
                break;
            }
        }

        root->left = buildSubTree(preorder, inorder, pre_left + 1, left_subtree_last_idx - 1, root_idx + 1, in_right);
        root->right = buildSubTree(preorder, inorder, left_subtree_last_idx, preorder.size() - left_subtree_last_idx, root)

    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // 1. 루트 노드 만들기.
        TreeNode* root = new TreeNode{preorder[0]};

        // 2. inorder에서 루트노드 위치 찾기
        int root_idx = 0;
        unordered_map<int, bool> m;

        for (int i = 0; i < inorder.size(); ++i) {
            if (inorder[i] == root->val) {
                root_idx = i;
                break;
            }
            m[inorder[i]] = true;
        }

        // 3. 왼쪽 오른쪽 서브트리 만들어서 이어붙이기.
        // 일단, preorder를 1부터 순회하며 0에서 root_idx - 1까지의 inorder 값에 속하지 않는게 나올때까지 순회하고 나오면 이전까지는 왼쪽 서브트리꺼다.
        
        int left_subtree_last_idx;
        for (left_subtree_last_idx = 1; left_subtree_last_idx < preorder.size(); ++left_subtree_last_idx) {
            // 왼쪽 서브트리에 존재하지 않는 숫자면 break
            if (!m[preorder[left_subtree_last_idx]]) {
                break;
            }
        }

        // 1 ~ left_subtree_last_idx - 1까지가 왼쪽 서브트리에 속함.

        root->left = buildSubTree(preorder, inorder, 1, left_subtree_last_idx - 1, 0, root_idx - 1);
        root->right = buildSubTree(preorder, inorder, left_subtree_last_idx, preorder.size() - left_subtree_last_idx, root_idx + 1, inorder.size() - 1);
        
        return root;
    }
};