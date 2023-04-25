class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> stc;
        int n = pushed.size();
        bool res = true;
        for (int i = 0, j = 0; i < n; i++)
        {
            if (stc.size() > 0 and stc.top() == popped[i])
            {
                stc.pop();
            }
            else
            {
                while (j < n and pushed[j] != popped[i])
                {
                    stc.push(pushed[j++]);
                }
                if (j < n) j++;
                else
                {
                    res = false; break;
                }
            }
        }

        return res;
    }
};