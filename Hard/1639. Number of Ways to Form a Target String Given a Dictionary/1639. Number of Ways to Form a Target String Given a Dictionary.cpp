class Solution {
    int n, m, MOD = 1e9+7;
    string target;
    vector<vector<int>> cnt;
    vector<vector<int>> dp;
    int solve(int pos1, int pos2) {
        if (pos2 == m) {
            return  1;
        }
        if (pos1 == n) {
            return 0;
        }
        if (dp[pos1][pos2] != -1) {
            return dp[pos1][pos2];
        }
        long long ans = solve(pos1 + 1, pos2);
        ans += ((long long)solve(pos1 + 1, pos2 + 1) * cnt[pos1][target[pos2] - 'a']) % MOD;
        ans %= MOD;

        return dp[pos1][pos2] = ans;
    }
public:
    int numWays(vector<string>& words, string target) {
        n = words[0].size(); m = target.size();
        this->target = target;
        cnt = vector<vector<int>>(n, vector<int>(26, 0));
        for (auto &word : words) {
            for (int i = 0; i < n; ++i) {
                ++cnt[i][word[i] - 'a'];
            }
        }
        dp = vector<vector<int>>(n, vector<int>(m, -1));
        return solve(0, 0);
    }
};
