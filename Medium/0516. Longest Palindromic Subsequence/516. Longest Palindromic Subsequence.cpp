class Solution {
    int dp[1010][1010]; string s;
    int solve(int a, int b)
    {
        if (a > b) return 0;
        if (a == b) return 1;
        if (dp[a][b] != -1) return dp[a][b];
        if (s[a] == s[b]) dp[a][b] = 2+solve(a+1, b-1);
        else dp[a][b] = max(solve(a, b-1), solve(a+1, b));
        return dp[a][b];
    }
public:
    int longestPalindromeSubseq(string s)
    {
        this->s = s;
        memset(dp, -1, sizeof dp);
        return solve(0, s.size());
    }
};