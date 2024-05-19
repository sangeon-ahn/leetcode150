/**
 * 마지막 노드로부터 n번째의 노드를 제거하는데, 한 번의 순회 만으로 푸는 법.
 * 1. 처음에 n번째 노드를 가리키도록 포인터p 이동
 *      - n번까지 가지도 못하면 head 리턴
 * 2. head를 가리키는 노드가 리스트 길이가 n인 경우의 제거될 노드이다. head 노드 가리키는 포인터 q 생성
 * 3. p를 한칸씩 이동시키며, 다음 노드가 nullptr이면 q 제거, nullptr 아니면 둘다 한칸씩 이동
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* p = head, *q;

        for (int i = 0; i < n - 1; i++) {
            if (p->next == nullptr) return head;
            p = p->next;
        }

        ListNode* dummy = new ListNode{};
        dummy->next = head;

        q = dummy;

        while (p != nullptr) {
            if (p->next == nullptr) {
                q->next = q->next->next;
                break;
            }
            p = p->next;
            q = q->next;
        }

        head = dummy->next;
        delete dummy;
        return head;
    }
};