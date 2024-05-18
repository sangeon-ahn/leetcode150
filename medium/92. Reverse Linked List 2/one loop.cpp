#include <vector>
using namespace std;

struct ListNode {
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

    int val;
    ListNode *next;
};

class Solution
{
    public:
        ListNode* reverseBetween(ListNode* head, int m, int n) {
            ListNode* dummy = new ListNode{};
            dummy->next = head;
            
            ListNode* prev = dummy;
            ListNode* cur;
            
            for (int i = 0; i < m - 1; i++) {
                prev = prev->next;
            }

            cur = prev->next;

            for (int i = 0; i < n - m; i++) {
                ListNode* temp = prev->next;
                prev->next = cur->next;
                cur->next = prev->next->next;
                prev->next->next = temp;
            }

            head = dummy->next;
            delete dummy;
            return head;
        }
};
