struct node
{
    map<char , node *> path;
    bool flag;
    node(int flag=0) : flag(flag)
    {

    }
};
class Trie
{
    node * root;
public:
    Trie()
    {
        root = new node();
    }

    void insert(string word)
    {
        node * curr = root;
        for (char ch : word)
        {
            if (curr->path.count(ch) == 0)
            {
                curr->path[ch] = new node();
            }
            curr = curr->path[ch];
        }
        curr->flag = 1;
    }

    bool search(string word)
    {
        node * curr = root; bool found = 1;
        for (char ch : word)
        {
            if (curr->path.count(ch) == 0)
            {
                found = 0; break;
            }
            curr = curr->path[ch];
        }

        return found and curr->flag == 1;
    }

    bool startsWith(string prefix)
    {
        node * curr = root; bool found = 1;
        for (char ch : prefix)
        {
            if (curr->path.count(ch) == 0)
            {
                found = 0; break;
            }
            curr = curr->path[ch];
        }

        return found;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */