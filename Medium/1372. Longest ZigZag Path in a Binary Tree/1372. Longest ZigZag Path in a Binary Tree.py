# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def slove(node, direction):
            if not node:
                return 0
            if (node, direction) in dp:
                return dp[(node, direction)]
            if direction == 0:
                dp[(node, direction)] = slove(node.left, 1) + 1
            else:
                dp[(node, direction)] = slove(node.right, 0) + 1
            return dp[(node, direction)]

        self.ans = 0
        def dfs(node):
            if not node:
                return
            self.ans = max(self.ans, slove(node.left, 1), slove(node.right, 0))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans