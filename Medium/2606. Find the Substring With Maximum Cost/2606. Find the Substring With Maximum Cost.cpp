class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        map<char, int> mp;
        for (int i = 0; i < chars.size(); ++i) {
            mp[chars[i]] = vals[i];
        }
        for (char c = 'a'; c <= 'z'; c++) {
            if (mp.count(c) == 0) {
                mp[c] = c-'a'+1;
            }
        }
        int n = s.size();
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            arr[i] = mp[s[i]];
        }
        // kadane
        int best = 0, sum = 0;
        for (int k = 0; k < n; k++) {
            sum = max(arr[k],sum+arr[k]);
            best = max(best,sum);
        }
        return best;
    }
};