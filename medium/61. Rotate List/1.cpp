struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (k == 0 || !head || !head->next) return head;
        int size = 0;

        ListNode* temp = head;
        
        while (temp) {
            size++;

            if (temp->next == nullptr) {
                break;
            }
            temp = temp->next;
        }

        int real_k = k % size; 

        if (real_k == 0) return head;
        
        temp->next = head;

        int cnt = size - real_k - 1; // cnt번 나아간 노드는 nullptr을 가리키도록 하고 끝
        ListNode* temp2 = head;
        while (cnt > 0) {
            temp2 = temp2->next;
            cnt--;
        }
        ListNode* new_head = temp2->next;
        temp2->next = nullptr;

        return new_head;
    }
};