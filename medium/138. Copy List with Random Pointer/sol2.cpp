#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
    public:
        Node* copyRandomList(Node* head) {
            if (!head) return nullptr;

            // 기존 리스트와 새 리스트가 지그재그로 연결되도록 만듬.
            Node* curr = head;
            while (curr) {
                Node* new_node = new Node(curr->val);
                new_node->next = curr->next;
                curr = new_node->next;
            }

            curr = head;
            while (curr) {
                if (curr->random) {
                    curr->next->random = curr->random->next; // 기존 노드와 다음 노드는 서로 짝지어 사실상 매핑되어 있는데, 기존 노드의 다음 노드와 매핑되어 있다. 그래서 새 노드의 random노드는 기존 노드의 랜덤(기존 랜덤노드)의 다음 노드이다.
                }
                curr = curr->next->next; // 기존 리스트 순회
            }

            Node* old_head = head;
            Node* new_head = head->next;
            Node* curr_old = old_head;
            Node* curr_new = new_head;

            while (curr_old) {
                curr_old->next = curr_old->next->next;
                curr_new->next = curr_new->next ? curr_new->next->next : nullptr;
                curr_old = curr_old->next;
                curr_new = curr_new->next;
            }

            return new_head;

        }

};