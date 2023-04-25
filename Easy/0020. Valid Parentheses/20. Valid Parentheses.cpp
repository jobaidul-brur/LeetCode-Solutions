class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> stc; bool ans = 1;
        for (char ch : s)
        {
            if (ch == '(' or ch == '{' or ch == '[') stc.push(ch);
            else if (stc.size() == 0
                     or (ch == ')' and stc.top() != '(')
                     or (ch == '}' and stc.top() != '{')
                     or (ch == ']' and stc.top() != '['))
            {
                ans = 0; break;
            }
            else stc.pop();
        }
        if (stc.size()) ans = 0;

        return ans;
    }
};