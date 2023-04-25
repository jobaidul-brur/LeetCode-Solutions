class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        vector<vector<int>> ans;
        map<int, int> cnt;
        sort(nums.begin(), nums.end());
        for (int num : nums) {
            if (ans.size() <= cnt[num]) {
                ans.emplace_back();
            }
            ans[cnt[num]].push_back(num);
            cnt[num]++;
        }
        return ans;
    }
};