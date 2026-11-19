class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(n):
            if not n: return 0, 0
            l, d1 = dfs(n.left)
            r, d2 = dfs(n.right)
            return 1 + max(l, r), max(l + r, d1, d2)
        return dfs(root)[1]