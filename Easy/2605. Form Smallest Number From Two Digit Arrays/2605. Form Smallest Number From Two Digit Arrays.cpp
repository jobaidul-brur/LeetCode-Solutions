class Solution {
public:
    int minNumber(vector<int>& nums1, vector<int>& nums2) {
        set<int> s1, s2;
        for (int e : nums1) s1.insert(e);
        for (int e : nums2) s2.insert(e);

        for (int i = 0; ; i++) {
            string s = to_string(i);
            bool flag1 = 0, flag2 = 0;
            for (char c : s) {
                if (s1.count(c - '0')) flag1 = 1;
                if (s2.count(c - '0')) flag2 = 1;
            }
            if (flag1 && flag2) return i;
        }
        return -1;
    }
};