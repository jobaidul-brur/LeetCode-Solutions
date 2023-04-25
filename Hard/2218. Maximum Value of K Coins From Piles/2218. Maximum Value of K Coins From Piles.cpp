class Solution {
    vector<vector<int>> piles, dp;
    int solve(int pos, int k) {
        if (pos == piles.size()) {
            return 0;
        }
        if (dp[pos][k] != -1) {
            return dp[pos][k];
        }
        int ans = 0;
        int sum = 0;
        ans = solve(pos + 1, k);
        for (int i = 0; i < k and i < piles[pos].size(); ++i) {
            sum += piles[pos][i];
            ans = max(ans, sum + solve(pos + 1, k-i-1));
        }
        return dp[pos][k] = ans;
    }
public:
    int maxValueOfCoins(vector<vector<int>>& piles, int k) {
        this->piles = piles;
        dp.resize(piles.size(), vector<int>(k + 1, -1));
        return solve(0, k);
    }
};