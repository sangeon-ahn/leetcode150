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
// inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3]
// inorder는 왼쪽, 나, 오른쪽 순서로 순회
// postorder는 왼쪽, 오른쪽 나 순서로 순회
// 즉, inorder에서 가장 처음으로 방문하는 노드는 해당 트리에서 가장 왼쪽에 있는 리프노드이다.
// 그 다음으로 방문하는 노드는 해당 리프 노드의 부모 노드
// 여기까지는 확실히 정해지는 순서다.
// 그 이후엔, 부모 노드의 오른쪽 서브트리일지, 부모 노드의 부모노드일지 모른다.
// 이를 알기 위해 postorder 순회 결과가 필요하다. postorder에서 부모 노드를 방문한 순서를 보자.
// 3은 postorder의 맨 마지막 인덱스에 위치한다.
// 그리고, postorder는 왼쪽 오른쪽 나 순서로 순회한다. 3이 맨 마지막에 있다는 소리는, 3이 루트 노드라는 것이다.
// 따라서, inorder에서 맨 두번째 노드는 위치관계가 정해지고, 부모 노드를 postorder에서 찾은 후, postorder에서 자식 노드의 위치,
// 부모 노드의 위치를 찾고 나서, 그 사이에 있는 노드들을 부모의 오른쪽 서브트리를 이루는 노드라고 보면 된다.
//
class Solution {
public:
  TreeNode* buildSubTree(vector<int>& inorder, vector<int>& postorder, int in_first, int in_end, int post_first, int post_end, unordered_map<int, int>& m) {
    if (in_first > in_end || post_first > post_end) return nullptr;
    int root_node_idx = m[postorder[post_end]];

    TreeNode* root_node = new TreeNode(postorder[post_end]);
    
    root_node->left = buildSubTree(inorder, postorder, in_first, root_node_idx - 1, post_first, post_first + (root_node_idx - in_first - 1), m);
    root_node->right = buildSubTree(inorder, postorder, root_node_idx + 1, in_end, post_first + root_node_idx - in_first, post_end - 1, m);

    return root_node;
  }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
      unordered_map<int, int> m; 
      for (int i = 0; i < inorder.size(); ++i) {
        m[inorder[i]] = i;
      }

      return buildSubTree(inorder, postorder, 0, inorder.size() - 1, 0, postorder.size() - 1, m);
    }
};

