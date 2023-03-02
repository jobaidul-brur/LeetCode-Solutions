# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        st = set()
        visited = set()
        res = []
        def is_leaf(node):
            return node.left is None and node.right is None
        def dfs(node):
            if node is None:
                return "()"
            subtree = ""
            if is_leaf(node):
                subtree = f"({node.val})"
            else:
                subtree = f"({dfs(node.left)}{node.val}{dfs(node.right)})"

            if subtree in st:
                if not subtree in visited:
                    res.append(node)
                    visited.add(subtree)
            else:
                st.add(subtree)
            return subtree

        dfs(root)
        return res
            
