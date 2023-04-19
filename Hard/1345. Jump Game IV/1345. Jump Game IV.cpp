class Solution
{
public:
    int minJumps(vector<int>& arr)
    {
        int n = arr.size();
        if (n <= 1) return 0;

        map<int, vector<int>> same;
        for (int i = 0; i < n; i++) same[arr[i]].push_back(i);
        int dis[n];
        memset(dis, -1, sizeof dis);
        queue<int>q;

        dis[0] = 0;
        q.push(0);

        while (q.size())
        {
            int curr = q.front(); q.pop();
            //cout << curr << "[" << arr[curr] << "] : " << dis[curr] << endl;
            if (curr-1 >= 0 and dis[curr-1] == -1)
            {
                dis[curr-1] = dis[curr]+1;
                q.push(curr-1);
            }
            if (curr+1 < n and dis[curr+1] == -1)
            {
                dis[curr+1] = dis[curr]+1;
                q.push(curr+1);
            }
            for (int adj : same[arr[curr]])
            {
                if (dis[adj] == -1)
                {
                    dis[adj] = dis[curr]+1;
                    q.push(adj);
                }
            }
            same[arr[curr]].clear();
        }

        return dis[n-1];
    }
};