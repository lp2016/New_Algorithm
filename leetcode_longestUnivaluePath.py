# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from 树.创建树 import CreateTree
class Solution:
    def __init__(self):
        self.res = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l = 0
        r = 0
        tmpl = 0
        tmpr = 0
        if root.left:
                l = self.dfs(root.left)
                if root.val == root.left.val:
                    tmpl = l + 1
        if root.right:
                r = self.dfs(root.right)
                if root.val == root.right.val:
                    tmpr = r + 1
        if root.left and root.right:
            if root.val == root.left.val and root.left.val == root.right.val:
                self.res = max(self.res, tmpl + tmpr)
        return max(self.res,max(tmpl,tmpr))

    def dfs(self, root):
        l = 0
        r = 0
        tmpl = 0
        tmpr = 0
        if root.left:
            l = self.dfs(root.left)
            if root.val == root.left.val:
                tmpl = l + 1
        if root.right:
            r = self.dfs(root.right)
            if root.val == root.right.val:
                tmpr = r + 1
        if root.left and root.right:
            if root.val == root.left.val and root.left.val == root.right.val:
                self.res = max(self.res, tmpl+tmpr)
        self.res = max(self.res, max(tmpl, tmpr))
        return max(tmpl, tmpr)

p = CreateTree([1,1,1])
print(Solution().longestUnivaluePath(p))