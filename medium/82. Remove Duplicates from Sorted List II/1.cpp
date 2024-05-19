/**
 * 1. prev, curr 포인터 생성하고 prev는 dummy 가리키고 curr는 head 가리키도록 함.
 * 2. curr의 next 확인 후, curr과 다르면 다음 그룹임. 이때 curr의 그룹 크기가 1이면 prev와 연결하고, prev를 curr로 옮기고 curr을 curr.next로 옮김.
 * 3. curr과 같으면 curr 계속 전진시킴
 * 4. curr 그룹 크기가 1보다 크면 그룹 크기 초기화만.
 * 5. curr의 다음 노드가 없을 때, 현재 그룹 크기 1이면 prev와 연결시킴.
*/
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
        if (!head) return nullptr;
        
        ListNode *prev, *curr;
        ListNode* dummy = new ListNode{};
        dummy->next = head;
        prev = dummy;
        curr = head;

        int groupSize = 1;
        while (curr->next) {
            if (curr->val != curr->next->val) {
                if (groupSize == 1) {
                    prev->next = curr;
                    prev = curr;
                } else {
                    groupSize = 1;
                }
            }
            else {
                groupSize++;
            }
            curr = curr->next;
        }

        if (groupSize == 1) {
            prev->next = curr;
        } else {
            prev->next = nullptr;
        }

        head = dummy->next;
        delete dummy;
        return head;
    }
};