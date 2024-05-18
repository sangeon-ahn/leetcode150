/**
 * 1. 가운데 지점 파악: 1칸씩 가는 slow runner, 2칸씩 가는 fast runner
 * 2. slow runner는 데이터를 외부 자료구조에 저장하면서 가다가 가운데 지점 도달 시, 역순으로 저장된 값을 노드 value에 swap 하면서 다시 자료구조에 노드 value를 0번 인덱스부터 넣음.
 * 3. 다시 순회 돌 땐 slow runner만 가운데까지 가면서 마지막 element부터 역순으로 할당  
 * 어려운 포인트: left~right 구간 길이에 따른(홀수, 짝수) 다른 처리 
 *      - 홀수: fast runner가 더이상 못 가는 시점에서 slow runner가 위치한 노드는 가운데 지점이라 무시해야 함.
 *      - 짝수: slow runner가 위치한 노드는 left-side라서 포함시켜야 함.
 * 
 * 
*/

struct ListNode {
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

    int val;
    ListNode *next;
};

#include <vector>
using namespace std;

class Solution
{
    public:
        ListNode* reverseBetween(ListNode* head, int left, int right) {
            ListNode* temp = head;
            ListNode* slow;
            ListNode* fast;

            vector<int> vec;
            int len = right - left + 1;
            bool is_odd = len % 2;

            int pos = 1;
            while (pos < left) {
                temp = temp->next;
                ++pos;
            }

            slow = temp;
            fast = temp;
            while (true) {

                if (pos + 1 > right || pos + 2 > right) {
                    if (!is_odd) {
                        vec.push_back(slow->val);
                    }
                    break;
                }

                pos += 2;
                vec.push_back(slow->val);
                slow = slow->next;
                fast = fast->next->next;
            }

            int cnt = len / 2;

            if (!(slow->next)) {
                return head;
            }

            for (int i = vec.size() - 1; i >= 0; --i) {
                slow = slow->next;

                int temp = vec[i];
                vec[i] = slow->val;
                slow->val = temp;
            }

            for (int i = 0; i < vec.size(); ++i) {
                temp->val = vec[i];
                temp = temp->next;
            }

            return head;
        }
};
