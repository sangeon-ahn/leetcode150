/**
 * 이전에 reverse linked list 2 에서 도입한 방식 그대로 사용하면 될듯.
 * 위 문제: left~right 구간 reverse 시키는 것.
 * 지금 문제: 그룹 당 k개의 노드로 이루어지도록 나누어 각각의 그룹을 reverse 시키는 것.
 * 각각의 그룹에 대해 reverse linked list 2의 해법 적용하면 됨
 * 마지막 그룹이 k개가 아니라면 다시 reverse 해주면 됨.
 * reverse 해주는 함수 정의.
 *      인자: prev, cur, left, right
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
    // prev->next와 cur->next를 swap하는 함수
    void swapNode(ListNode* prev, ListNode* cur) {
        ListNode* temp = prev->next; // 그룹의 첫 노드 저장.
        prev->next = cur->next; // 그룹의 첫 노드에 현재의 다음 노드 배치
        cur->next = cur->next->next; // 현재의 다음 노드는 
        prev->next->next = temp;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        if (k == 1) {
            return head;
        }

        ListNode* dummy = new ListNode{};
        dummy->next = head;
        
        ListNode* prev = dummy;
        ListNode* cur = prev->next;
        ListNode* temp;

        int cnt = 1;
        bool flag = true;

        while (true) {
            // 다 돌았으면
            if (cur == nullptr || cur->next == nullptr) {
                if (flag && cnt % k == 1) {
                    break;
                }

                if (flag) {
                    flag = false;
                    cur = prev->next;
                } else {
                    break;
                }
            }

            swapNode(prev, cur);

            ++cnt;

            // 해당 그룹 reverse 끝냈으면 다음 그룹으로 이동
            if (flag && cnt % k == 0) {
                ++cnt;
                prev = cur;       
                cur = cur->next;
            }
        }
        
        head = dummy->next;
        delete dummy;

        return head;
    }
};