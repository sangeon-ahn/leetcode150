class TreeNode
{
  TreeNode() : value{0} {};
  TreeNode(int val) : value{val} {}

  int value; 
  TreeNode* next;
  TreeNode* left;
  TreeNode* right;
};
/*
 * N과 관계없이 constant한 space complexity 풀이?
 * 가장 간단한 방법은 각 노드의 level을 기준으로 같은 level인 노드를 다 찾은 후 연결하면 된다.
 * 근데 어쩔수없이 각 level별연결지을  노드를 담는 자료구조가 필요한데 어떻게 가능? 일단 h만큼 공간 필요한 풀이로 풀어보자.
 * root node's level = 0, 밑으로 갈수록 1씩 증가
 *
*/
class Solution
{
  // 자신의 오른쪽 자식부터 순회
  void dfs(TreeNode** arr, TreeNode* node, int level) {
    if (!node) return;

    // 오른쪽 자식 있으면 연결
    if (node->right) {
      // 근데 자기가 처음이면 자기 넣기  
      if (!arr[level]) {
        arr[level] = node;
      }
      // 이미 있으면 연결하고 갱신
      else {
        node->next = arr[level];
        arr[level] = node;
      }
      // 재귀
      dfs(arr, node->right, level + 1);
    }

    // 왼쪽 자식 있으면 연결
    if (node->left) {
      if (!arr[level]) {
        arr[level] = node;
      }
      else {
        node->next = arr[level];
        arr[level] = node;
      }
      dfs(arr, node->left, level + 1);
    }
  }
  TreeNode* sol(TreeNode* head) {
    TreeNode* latest_nodes[2<<12];
    
    dfs(latest_nodes, head, 0);
    return head;
  }
};
