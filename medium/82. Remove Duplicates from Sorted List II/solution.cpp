struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head) return head;

        ListNode *prev = nullptr, *curr = head, *next = curr->next;

        while (next) {
            // curr과 next가 같은 값이면 넘어가는 로직 수행.
            if (curr->val == next->val) {
                while (next && next->val == curr->val) {
                    next = next->next;
                }
                if (!prev) {
                    head = next;
                }
                else {
                    prev->next = next;
                }
            }
            else {
                prev = curr;
            }

            curr = next;
            if (next) {
                next = curr->next;
            }
        }

        return head;
    }
};