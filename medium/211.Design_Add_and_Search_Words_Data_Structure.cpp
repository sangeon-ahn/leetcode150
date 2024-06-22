#include <vector>
#include <iostream>
#include <queue>
#include <utility>
using namespace std;

/*
 * 일반적인 trie와 다른 점은, char로 .이 들어왔을 경우 해당 번째의 모든 char가 .이 될 수 있다는 거다.
 * 그래서, 큐를 사용해서 각 상태에 대해 후보가 될 수 있는 다음 노드를 다 집어 넣은 후, 맨 앞에서 하나 뽑아 이후 과정을
 * 수행하면 된다. 이렇게 하다가 조건을 만족하는걸 찾았을 때 그냥 바로 true 리턴해주면 된다.
 * */
constexpr int ALPHABET_SIZE = 26;
int CharToIdx(char ch) {
  return ch - 'a'; 
}

class Node
{
  public:
    Node() {
      for (int i = 0; i < ALPHABET_SIZE; ++i) {
        node_array_[i] = nullptr;
      }
    };

    ~Node() {
      for (int i = 0; i < ALPHABET_SIZE; ++i) {
        if (node_array_[i] != nullptr) {
          delete node_array_[i];
        }
      }
    }

    int cnt = 0;
    bool is_finish = false;
    Node* node_array_[ALPHABET_SIZE];
};

class WordDictionary {
public:
    Node root_node_;

    WordDictionary() {}
    
    void addWord(string word) {
      Node* temp = &root_node_;

      for (int i = 0; i < word.size(); ++i) {
        int idx = CharToIdx(word[i]);

        if (!temp->node_array_[idx]) {
          temp->node_array_[idx] = new Node();
          temp->cnt++; 
        }
        temp = temp->node_array_[idx];
      }
      temp->is_finish = true; 
    }
    
    bool search(string word) {
      queue<pair<Node*, int>> q;
      q.push({&root_node_, 0});

      while (!q.empty()) {
        auto temp = q.front(); q.pop();
        
        Node* node = temp.first;
        int cur_idx = temp.second;
       
        if (cur_idx == word.size()) {
          if (node->is_finish) {
            return true;
          }
          continue;
        }

        if (node->cnt <= 0) {
          continue;
        }

        if (word[cur_idx] == '.') {
          for (int i = 0; i < ALPHABET_SIZE; ++i) {
            if (node->node_array_[i]) {
              q.push({node->node_array_[i], cur_idx + 1});
            }
          }
        }
        else {
          int idx = CharToIdx(word[cur_idx]);
          if (node->node_array_[idx]) {
            q.push({node->node_array_[idx], cur_idx + 1});
          }
        }
      }
      return false;
    }
};

int main() {
  WordDictionary* wordDictionary = new WordDictionary();
  vector<bool> vec;

  wordDictionary->addWord(std::string("bad"));
  wordDictionary->addWord(std::string("dad"));
  wordDictionary->addWord(std::string("mad"));
  
  vec.push_back(wordDictionary->search(std::string("pad")));
  vec.push_back(wordDictionary->search(std::string("bad")));
  vec.push_back(wordDictionary->search(std::string(".ad")));
  vec.push_back(wordDictionary->search(std::string("b..")));
  
  for (int i = 0; i < vec.size(); ++i) {
    std::cout << vec[i] << std::endl;
  }

  delete wordDictionary;
}
/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
