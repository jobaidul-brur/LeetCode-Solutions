class Solution {
    int size[303], link[303];
    bool vis[303];
    int find (int x)
    {
        if (link[x] == x) return x;
        return link[x] = find(link[x]);
    }
    void unite(int a, int b)
    {
        a = find(a); b = find(b);
        if (a == b) return;
        if (size[a] < size[b]) swap(a, b);
        
        size[a] += size[b];
        link[b] = a;
    }
    bool similar(string & a, string & b)
    {
        int cnt = 0;
        for (int i = 0; i < a.size(); i++)
        {
            if (a[i] != b[i]) cnt++;
        }
        return cnt == 2 or cnt == 0;
    }
public:
    int numSimilarGroups(vector<string>& strs) 
    {
        int n = strs.size();
        
        for (int i = 0; i < n+1; i++) 
        {
            link[i] = i; size[i] = 1;
        }
        
        for (int i = 0; i < n; i++)
        {
            for (int j = i+1; j < n; j++)
            {
                if (similar(strs[i], strs[j])) unite(i, j);
            }
        }
        
        memset(vis, 0, sizeof vis);
        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            int x = find(i);
            if (not vis[x])
            {
                vis[x] = 1;
                ans++;
            }
        }
        return ans;
    }
};
