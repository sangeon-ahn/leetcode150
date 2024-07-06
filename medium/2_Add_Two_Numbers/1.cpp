/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
// 두 링크드 리스트가 주어진다.
// 각 링크드 리스트는 숫자를 표현한다. 이때 각 노드는 각 자리수의 수를 담고 있다.
// 그리고, 링크드 리스트는 각 자리수를 역순으로 연결짓고 있다.
// 이때, 두 숫자를 더한 값을 마찬가지로 역순의 링크드리스트로 표현해라.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      ListNode* root = l1;
      ListNode* l1_prev = nullptr;
      ListNode* l2_prev = nullptr;
      bool flag = false;
      int carry = 0;

      while (l1 || l2) {
        if (l1 && l2) {
          int val = carry + l1->val + l2->val;

          if (val >= 10) {
            l1->val = val - 10;
            carry = 1;
          } else {
            l1->val = val;
            carry = 0;
          }

          l1_prev = l1;
          l2_prev = l2;
          l1 = l1->next;
          l2 = l2->next;
        } 

        else if (!l1) {
          l1_prev->next = l2;

          while (l2) {
            int val = carry + l2->val;

            if (val >= 10) {
              l2->val = val - 10;
              carry = 1;
              l2_prev = l2;
              l2 = l2->next;
            }
            else {
              flag = true;
              l2->val = val;
              return root; 
            }
          }

          if (carry > 0) {
            l2_prev->next = new ListNode(carry);
          }
          return root;
        }
        
        else {
          ListNode temp = l1;
          l1 = l2;
          l2 = temp;

          temp = l1_prev;
          l1_prev = l2_prev;
          l2_prev = temp;
        }
      }

      if (carry > 0) {
        l1_prev->next = new ListNode(carry);
      }
      return root;
    }
};
