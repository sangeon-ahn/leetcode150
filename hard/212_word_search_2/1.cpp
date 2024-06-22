#include <vector>
#include <string>
#include <iostream>
#include <string_view>
#include <unordered_map>
/*
 * 42/65 Time Limit Exceeded
 *
*/
using namespace std;
/*
 * 일단, board를 trie로 만들어둔다. 이렇게 하면 4방향 보고 이런것들 할 필요 없어진다.
 * 그리고 word 있는지 볼 땐, 한 문자씩 있는지 확인하면 끝이다(O(1)).
 *
 * */
class Node {
public:
  Node(char ch) : ch_(ch) {
    for (int i = 0; i < 26; ++i) {
      for (int j = 0; j < 4; ++j) {
        node_array_[i][j] = nullptr;
      }
      node_array_cnt_[i] = 0;
    }
  }
  ~Node() = default;

  char ch_;
  Node* node_array_[26][4];
  int node_array_cnt_[26];
};

class TrieBoard {
  public:
    Node* board_[12][12];
    int n;
    int m;
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    
    TrieBoard(vector<vector<char>>& board) : n(board.size()), m(board[0].size())
    {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          board_[i][j] = new Node(board[i][j]);
        }
      } 
    }

    ~TrieBoard() {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          if (board_[i][j]) delete board_[i][j];
        }
      }
    }
   
    bool inRange(int x, int y) {
      return x < n && x >= 0 && y < m && y >= 0;
    }

    void buildTrie() {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          Node* cur = board_[i][j];

          for (int k = 0; k < 4; ++k) {
            int nx = i + dx[k];
            int ny = j + dy[k];

            if (inRange(nx, ny)) {
              cur->node_array_[board_[nx][ny]->ch_ - 'a'][cur->node_array_cnt_[board_[nx][ny]->ch_ - 'a']] = board_[nx][ny];
              cur->node_array_cnt_[board_[nx][ny]->ch_ - 'a']++; 
            }
          }
        }
      } 
    }
   
    bool findWord(Node* node, int cnt, string& word, unordered_map<Node*, bool>& visited) {
      if (cnt == word.size()) return true;


      for (int i = 0; i < node->node_array_cnt_[word[cnt] - 'a']; ++i) {
        Node* nxt_node = node->node_array_[word[cnt] - 'a'][i];

        if (!visited[nxt_node]) {
          visited[nxt_node] = true;

          if (findWord(nxt_node, cnt + 1, word, visited)) {
            return true;
          }

          visited[nxt_node] = false;
        }
      }
      return false;
    }
    
    bool isWordExist(string& word) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
          if (board_[i][j]->ch_ == word[0]) {
            unordered_map<Node*, bool> s;
            s[board_[i][j]] = true;

            if (findWord(board_[i][j], 1, word, s)) {
              return true;
            }
          }
          }
        }
      return false;
      }
};

class Solution {
public:
  vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
    TrieBoard* trie_board = new TrieBoard(board);
    trie_board->buildTrie();

    vector<string> result; 

    for (int i = 0; i < words.size(); ++i) {
      if (trie_board->isWordExist(words[i])) {
        result.push_back(words[i]);  
      }
    }

    delete trie_board;
    return result;
  }
};

int main()
{
  Solution* sol = new Solution();
  
  vector<vector<char>> b;

  b.push_back(vector<char>{'o', 'a', 'a', 'n'});
  b.push_back(vector<char>{'e', 't', 'a', 'e'});
  b.push_back(vector<char>{'i', 'h', 'k', 'r'});
  b.push_back(vector<char>{'i', 'f', 'l', 'v'});

  vector<string> w{string("oath"), string("pea"), string("eat"), string("rain")};
  vector<string> answer = sol->findWords(b, w);

  for (auto& elem : answer) {
    cout << elem << endl;
  }
  delete sol;
}
