class Solution {
    string to_string(char c) {
        string s = "";
        s += c;
        return s;
    }
public:
    long long distinctNames(vector<string>& ideas) {
        int n;
        unordered_set<string> st;
        for (int i = 0; i < ideas.size(); ++i) {
            st.insert(ideas[i]);
        }
        vector<int> can_accept[130][130];
        for (int i = 0; i < ideas.size(); ++i) {
            for (char c = 'a'; c <= 'z'; ++c) {
                if (st.count(to_string(c) + ideas[i].substr(1)) == 0) {
                    can_accept[ideas[i][0]][c].push_back(i);
                }
            }
        }
        long long cnt = 0;
        for (char a = 'a'; a <= 'z'; ++a) {
            for (char b = a + 1; b <= 'z'; ++b) {
                for (int i = 0; i < can_accept[a][b].size(); ++i) {
                    cnt += can_accept[b][a].size();
                }
            }
        }
        return cnt * 2;
    }
};
