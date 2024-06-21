#include <string>
#include <iostream>
#include <vector>
using namespace std;

constexpr int ALPHABET_SIZE = 26;

int CharToIndex(char ch)
{
  return ch - 'a';
}

class Node {
  public:
    Node()
    {
      for (int i = 0; i < ALPHABET_SIZE; ++i) {
        node_array_[i] = nullptr;
      }  
    }

    ~Node()
    {
      for (int i = 0; i < ALPHABET_SIZE; ++i) {
        if (node_array_[i]) {
          delete node_array_[i];
        }
      }
    }

    bool is_last_char = false;
    Node* node_array_[ALPHABET_SIZE];

    void SetIsLastChar(bool flag) { is_last_char = flag; }
    bool GetIsLastChar() { return is_last_char; }
};

class Trie {
  private:
    Node root_node_;
    Node* travel(string word) {
      Node* temp = &root_node_;

      for (int i = 0; i < word.size(); ++i) {
        int idx = CharToIndex(word[i]);

        if (temp->node_array_[idx]) {
          temp = temp->node_array_[idx];
        } else { return nullptr; }
      }
      return temp;
    } 
  public:
    Trie() {}

    void insert(string word) {
      Node* temp = &root_node_;

      for (int i = 0; i < word.size(); ++i) {
        int idx = CharToIndex(word[i]);

        if (!temp->node_array_[idx]) {
          temp->node_array_[idx] = new Node(); 
        } 
        temp = temp->node_array_[idx];
      }
      temp->SetIsLastChar(true);
    }

    bool search(string word) {
      Node* last_node = travel(word);

      if (!last_node || !last_node->GetIsLastChar()) { return false; }
      return true;
    }

    bool startsWith(string prefix) {
      if (!travel(prefix)) { return false; }
      return true;
    }
};


int main() {
  Trie* trie = new Trie();
  std::vector<bool> results;
  trie->insert(std::string("apple"));
  results.push_back(trie->search(std::string("apple")));
  results.push_back(trie->search(std::string("app")));

  results.push_back(trie->startsWith(std::string("app")));
  trie->insert(std::string("app"));
  results.push_back(trie->search(std::string("app")));

  for (bool b : results) {
    std::cout << b << std::endl; 
  }
}
