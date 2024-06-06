struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

/**
 * 일단, partition value x를 기준으로 두 파티션으로 나뉘기 때문에 두 파티션의 헤드 노드를 각각 하나씩 만들어준다.
 * 이후, 기존 리스트를 맨 처음 노드부터 순회하며 x와 비교를 한 후, 왼쪽 파티션에 속할지, 오른쪽 파티션에 속할지를 판단한다.
 * 속할 파티션이 정해졌으면, 해당 파티션의 맨 마지막 노드와 연결시켜준다.
 * 연결시켜주기 위해 마지막 노드 포인터가 필요하므로, 처음에 만들어 둔 각 파티션의 헤드노드 포인터 외에 추가로 임시 노드 포인터 두 개가 필요하다.
 * 연결시킨 후 다음 노드를 확인하러 간다.
 * 이렇게 마지막 노드까지 처리한 후 루프를 빠져나오면, 왼쪽 파티션의 마지막 노드를 오른쪽 파티션의 헤드 노드와 연결시켜준다.
 * 마지막으로, 오른쪽 파티션의 마지막 노드가 nullptr을 가리키도록 한다.
 * 이후, 왼쪽 파티션의 헤드노드를 리턴시켜주면 된다.
 * 
 * 주의점: 한쪽 파티션에 전부 속할 경우에 따로 예외처리를 해주어야 하는가?
 * 그렇다. 오른쪽 파티션의 마지막 노드가 nullptr를 가리키는 작업을 하면 안된다.
 * 
*/

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        if (!head) {
            return head;
        }

        ListNode* left_head = nullptr;
        ListNode* right_head = nullptr;
        ListNode* left_temp = left_head;
        ListNode* right_temp = right_head;

        ListNode* temp_head = head;

        while (temp_head) {
            // x보다 작으면 왼쪽 파티션과 연결
            if (temp_head->val < x) {
                // 아직 하나도 연결 안됐었으면 헤드로 삼기
                if (!left_head) {
                    left_head = temp_head;
                    left_temp = left_head;
                } 
                // 이미 설정됐었으면 left_temp와 연결하고 다음거로 이동
                else {
                    left_temp->next = temp_head;
                    left_temp = left_temp->next;
                }
            }
            // x와 같거나 더 크면 오른쪽 파티션과 연결
            else {
                if (!right_head) {
                    right_head = temp_head;
                    right_temp = right_head;
                }
                else {
                    right_temp->next = temp_head;
                    right_temp = right_temp->next;
                }
            }
            temp_head = temp_head->next;
        }

        // 3가지 경우로 나누어 처리
            // 왼쪽 파티션이 없는 경우
            if (!left_head) {
                return right_head;
            }
            // 오른쪽 파티션이 없는 경우
            if (!right_head) {
                return left_head;
            }

            // 둘 다 있는 경우
            left_temp->next = right_head;
            right_temp->next = nullptr;

            return left_head;
    }
};