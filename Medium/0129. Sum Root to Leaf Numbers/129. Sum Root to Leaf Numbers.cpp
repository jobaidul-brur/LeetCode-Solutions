/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
    int ans = 0;
    void dfs(TreeNode* curr, int val)
    {
        if (curr->left != nullptr)
        {
            dfs(curr->left, val*10+curr->val);
        }
        if (curr->right != nullptr)
        {
            dfs(curr->right, val*10+curr->val);
        }
        if (curr->left == nullptr and curr->right == nullptr)
        {
            ans += val*10+curr->val;
        }
        return;
    }
public:
    int sumNumbers(TreeNode* root)
    {
        dfs(root, 0);
        return ans;
    }
};