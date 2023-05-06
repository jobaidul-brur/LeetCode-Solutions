template <typename T> T binaryExpo(T n, T p)    { if (p == 0) { return 1LL;   } if (p&1) { return  n*binaryExpo(n, p - 1);     } T ret = binaryExpo(n, p/2) ; return ret * ret;     }
template <typename T> T bigMod(T n, T p, T m)   { if (p == 0) { return 1LL%m; } if (p&1) { return (n%m*bigMod(n, p - 1, m))%m; } T ret = bigMod(n, p/2, m)%m; return (ret * ret)%m; }
template <typename T> T modInv(T n, T m)        { return bigMod(n, m - 2, m); }

class Solution {
    static const long long MOD = 1e9 + 7;
public:
    int numSubseq(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        
        long long int ans = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] + nums[i] > target) {
                break;
            }
            int j = upper_bound(nums.begin(), nums.end(), target - nums[i]) - nums.begin();
            ans += bigMod(2LL, j - i - 1LL, MOD);
            ans %= MOD;
        }
        return ans;
    }
};
