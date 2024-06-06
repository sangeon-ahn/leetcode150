// time complexity: O(N)
// space complexity: O(N)
// Definition for a Node.
#include <unordered_map>
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

            unordered_map<Node*, Node*> old_to_new;

            Node* curr = head;
            // 노드 만들고 맵에 넣기만 함.
            while (curr) {
                old_to_new[curr] = new Node(curr->val);
                curr = curr->next;
            }

            // 
            curr = head;
            while (curr) {
                old_to_new[curr]->next = old_to_new[curr->next];
                old_to_new[curr]->random = old_to_new[curr->random];
                curr = curr->next;
            }

            return old_to_new[head];
        }        
};