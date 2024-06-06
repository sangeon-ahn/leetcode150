/**
 * 어떤 자료구조를 사용하여 구현할지 정해야 한다.
 * 조회와 삽입이 모두 O(1)로 구현되어야 한다.
 * 해시테이블 or 배열
 * key의 범위가 0 이상 1만 이하다. -> 배열로 구현 가능.
 * capacity는 1 이상 3천 이하다. -> capacity 초과하면 LRU로 evict 하나 시켜야 함.
 * 링크드 리스트로 만들어야겠다.
 * 두 개의 자료구조가 필요하다.
 * 1. key에 대한 노드 위치 저장용 자료구조(배열, unordered_map) 
 * 2. 노드 저장용 이중연결리스트(doubly linked list 자체구현)
*/

#include <unordered_map>
using namespace std;


constexpr int HEAD_NODE_KEY = (1 << 16);
constexpr int TAIL_NODE_KEY = (1 << 16) + 1;

class Node
{
    public:
        Node(int key, int val) {
            key_ = key;
            val_ = val;
        }
        ~Node() = default;
        
        int key_;
        int val_;
        Node* prev_ = nullptr;
        Node* next_ = nullptr;
};

class DoublyLinkedList
{
    public:
        DoublyLinkedList() {
            head.next_ = &tail;
            tail.prev_ = &head;
        }
        Node head = Node(HEAD_NODE_KEY, 0);
        Node tail = Node(TAIL_NODE_KEY, 0);

        void EraseNode(Node* node) {
            node->prev_->next_ = node->next_;
            node->next_->prev_ = node->prev_;
            delete node;
        }

        void InsertNodeToFirst(Node* node) {
            head.next_->prev_ = node;
            node->next_ = head.next_;
            head.next_ = node;
            node->prev_ = &head;
        }

        void MoveNodeToFirst(Node* node) {
            node->prev_->next_ = node->next_;
            node->next_->prev_ = node->prev_;

            head.next_->prev_ = node;
            node->next_ = head.next_;
            head.next_ = node;
            node->prev_ = &head;
        }
};
class LRUCache {
public:
    LRUCache(int capacity) {
        capacity_ = capacity;
        curr_cnt_ = 0;
    }

    DoublyLinkedList ddl;
    int curr_cnt_;
    int capacity_;
    unordered_map<int, Node*> nodes;
    
    int get(int key) {
        if (nodes[key] == nullptr) return -1;

        ddl.MoveNodeToFirst(nodes[key]);
        return nodes[key]->val_;
    }
    
    void put(int key, int value) {
        if (nodes[key] == nullptr) {
            if (curr_cnt_ >= capacity_) {
                evict();
            }
            nodes[key] = new Node{key, value};
            ddl.InsertNodeToFirst(nodes[key]);
            curr_cnt_++;
        } else {
            ddl.MoveNodeToFirst(nodes[key]);
            nodes[key]->val_ = value;
        }
    }
private:
    void evict() {
        Node* evicted_node = ddl.tail.prev_;

        nodes.erase(evicted_node->key_);
        ddl.EraseNode(evicted_node);
        
        curr_cnt_--;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */