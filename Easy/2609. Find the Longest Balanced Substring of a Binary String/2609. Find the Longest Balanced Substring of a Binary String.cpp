class Solution {
public:
    int findTheLongestBalancedSubstring(string s) {
        int ans = 0;
        for (int i = 0; i < s.size(); i++) {
            for (int j = i + 1; j < s.size(); j += 2) {
                int mid = (i + j) / 2;
                bool flag0 = 1;
                for (int k = i; k <= mid; k++) {
                    if (s[k] != '0') {
                        flag0 = 0;
                        break;
                    }
                }
                bool flag1 = 1;
                for (int k = mid + 1; k <= j; k++) {
                    if (s[k] != '1') {
                        flag1 = 0;
                        break;
                    }
                }
                if (flag0 and flag1) {
                    ans = max(ans, j - i + 1);
                }
            }
        }
        return ans;
    }
};