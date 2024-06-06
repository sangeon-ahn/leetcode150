// 일단, 기본적으로 싱글 링크드리스트니까 next 가면서 노드들 다 복사한 다음에
// 다시 순회할 땐 random을 매핑한 후 다음 노드로 가는 방식으로 random 매핑
// 총 두 번 링크드 리스트 순회 = O(N)

// Definition for a Node.
// class Node {
// public:
//     int val;
//     Node* next;
//     Node* random;
    
//     Node(int _val) {
//         val = _val;
//         next = NULL;
//         random = NULL;
//     }
// };

// prev:next 매핑된 맵 사용하면 될듯
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    Node* copyRandomList(Node* head) {
        map<Node*, Node*> m;

        Node* root = new Node{0};

        Node* temp1 = root;
        Node* temp2 = head;

        // 리스트 복사
        while (temp1 && temp2) {
            // 새 노드 만들기
            Node* newNode = new Node{temp2->val};

            // 연결
            temp1->next = newNode;

            m[temp2] = newNode;

            // 다음으로 가기
            temp1 = temp1->next;
            temp2 = temp2->next;
        }

        // 랜덤노드 매핑
        temp1 = root->next;
        temp2 = head;

        while (temp1 && temp2) {
            temp1->random = m[temp2->random];
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        
        return root->next;
    }
};