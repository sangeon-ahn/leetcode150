struct Node {
  Node* links[26];
  bool flag = false;

  bool containsKey(char ch)
  {
    return (links[ch - 'a'] != NULL);
  }

  void put(char ch)
  {
    links[ch - 'a'] = new Node();
  }

  Node* get(char ch)
  {
    return links[ch-'a'];
  }
  
  void setEnd()
  {
    flag = true;
  }

  bool isEnd()
  {
    return flag;
  }
}

class WordDictionary
{
private:
  Node* root;
  bool searchHelper(string& word, int index, Node* node)
  {
    if (index == word.size()) return node->isEnd();

    char ch = word[index];
    if (ch == '.')
    {
      for (int i = 0; i < 26; ++i)
      {
        if (node->links[i] != NULL)
        {
          if (searchHelper(word, index + 1, node->links[i])) return true;
        }
      }
      return false;
    }
    else
    {
      if (!node->containsKey(ch)) return false;
      return searchHelper(word, index + 1, node->get(ch));
    }
  }

public:
  WordDictionary()
  {
    root = new Node();
  }

  void addWord(string word)
  {
    Node* node = root;
    for (int i = 0; i < word.length(); ++i)
    {
      if (!node->containsKey(word[i])) node->put(word[i]);
      node = node->get(word[i]);
    }
    node->setEnd();
  }

  bool search(string word)
  {
    return searchHelper(word, 0, root);
  }
};
