#define ll long long
class Solution {
    vector<vector<ll>> arr; ll n, m;
    ll dp[51][51][11], mod = 1e9+7;
    ll solve(ll n, ll m, ll k) {
        if (k == 0) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (arr[i][j] == 1) {
                        return 1;
                    }
                }
            }
            return 0;
        }
        ll &ans = dp[n][m][k];
        if (ans != -1) {
            return ans;
        }
        ans = 0;
        for (int row = 1; row < n; row++) {
            bool flag = 0;
            for (int j = row; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (arr[j][k] == 1) {
                        flag = 1;
                        break;
                    }
                }
            }
            if (flag) {
                ans += solve(row, m, k-1);
                ans %= mod;
            }
        }
        for (int col = 1; col < m; col++) {
            bool flag = 0;
            for (int j = col; j < m; j++) {
                for (int k = 0; k < n; k++) {
                    if (arr[k][j] == 1) {
                        flag = 1;
                        break;
                    }
                }
            }
            if (flag) {
                ans += solve(n, col, k-1);
                ans %= mod;
            }
        }
        return ans;
    }
public:
    int ways(vector<string>& pizza, int k) {
        n = pizza.size(); m = pizza[0].size();
        arr = vector<vector<ll>>(n, vector<ll>(m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (pizza[i][j] == 'A') {
                    arr[n-1-i][m-1-j] = 1;
                } else {
                    arr[n-1-i][m-1-j] = 0;
                }
            }
        }
        memset(dp, -1, sizeof(dp));
        return solve(n, m, k-1);
    }
};