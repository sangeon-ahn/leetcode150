/*
 * words를 trie로 만든다.
 * board를 2중 for문 돌며 4방향 dfs 돌면서 trie에 있으면 계속 진행. 없으면 리턴.
 * 해당 node가 word의 마지막 문자라면 result에 word 추가.
 * node에 cnt 멤버 추가해서 cnt = 0이면 진입도 못하도록 하기
 * node에 진입할 때 cnt 1빼고 진입
 * */
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Node {
public:
  Node() {
    for (int i = 0; i < 26; ++i) {
      node_array_[i] = nullptr;
    }
  }
  ~Node() {
    for (int i = 0; i < 26; ++i) {
      if (!node_array_[i]) delete node_array_[i];
    }
  }

  int cnt = 0;
  string word = "";
  Node* node_array_[26];
};

class Trie {
public:
  Node root_node_;

  void insert(string word) {
    Node* temp = &root_node_;
    temp->cnt++;

    for (int i = 0; i < word.size(); ++i) {
      if (!temp->node_array_[word[i] - 'a']) {
        temp->node_array_[word[i] - 'a'] = new Node(); 
      }
      temp->node_array_[word[i] - 'a']->cnt++;
      temp = temp->node_array_[word[i] - 'a'];
    }
    temp->word = string(word);
  }

  void build(vector<string>& words) {
    for (string word: words) {
      insert(word);
    }
  }
};

class Solution {
public:
  int dx[4] = {1, 0, -1, 0};
  int dy[4] = {0, 1, 0, -1};

  bool inRange(int x, int y, int n, int m) {
    return 0 <= x && x < n && 0 <= y && y < m; 
  }

  int dfs(vector<vector<char>>& board, int cur_x, int cur_y, Node* cur_node, vector<string>& result, bool vis[][12]) {
    if (cur_node->cnt == 0) return 0;
    
    int word_cnt = 0;
    if (cur_node->word.size() > 0) {
      result.push_back(cur_node->word);
      cur_node->word = "";
      word_cnt++;
    }
    

    for (int i = 0; i < 4; ++i) {
        int nx = cur_x + dx[i];
        int ny = cur_y + dy[i];

        if (!inRange(nx, ny, board.size(), board[0].size())) continue;

        Node* nxt_node = cur_node->node_array_[board[nx][ny] - 'a'];

        if (nxt_node) {
            if (vis[nx][ny]) continue;

            vis[nx][ny] = true;
            int res = dfs(board, nx, ny, nxt_node, result, vis);
            vis[nx][ny] = false;

            if (res > 0) {
                word_cnt += res;
                continue;
            };
        }
    }
    cur_node->cnt -= word_cnt;
    return word_cnt;
  }    

  vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
    vector<string> result;

    Trie* trie = new Trie();
    trie->build(words);

    bool arr[12][12];

    for (int i = 0; i < 12; ++i) {
      for (int j = 0; j < 12; ++j) {
        arr[i][j] = false;
      }
    }

    for (int i = 0; i < board.size(); ++i) {
      for (int j = 0; j < board[0].size(); ++j) {
        Node* temp = trie->root_node_.node_array_[board[i][j] - 'a'];

        if (temp) {
            arr[i][j] = true;
            dfs(board, i, j, temp, result, arr);
            arr[i][j] = false;
        }
      }
    }

    delete trie;
    return result;
  }
};

int main()
{
  vector<vector<char>> board = {
    {'o','a','a','n'},
    {'e','t','a','e'},
    {'i','h','k','r'},
    {'i','f','l','v'}
  };
  vector<string> words = {"oath","pea", "eat", "rain", "oathi", "oathk", "oathf", "oate", "oathii", "oathfi", "oathfii"};
  Solution sol;
  vector<string> result = sol.findWords(board, words);
  for (string word: result) {
    cout << word << endl;
  }
  return 0;
}

