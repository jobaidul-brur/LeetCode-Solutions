# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        arr = [-1]*128
        ans = True

        def dfs(node, pos):
            if node == None:
                return
            if pos >= 128:
                ans = False
                return
            arr[pos] = 1
            dfs(node.left, pos*2)
            dfs(node.right, pos*2+1)

        dfs(root, 1)
        for i in range(1, 128):
            if arr[i] == -1:
                if max(arr[i:]) != -1:
                    ans = False
                break

        return ans