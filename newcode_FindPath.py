# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        if not root.left and not root.right:
            res.append([root.val])
        if root.left:
            self.FindPathHelper(root.left, res, [root.val], expectNumber)
        if root.right:
            self.FindPathHelper(root.right, res, [root.val], expectNumber)
        return res

    def FindPathHelper(self, root, res, tmp, expectNumber):
        tmp.append(root.val)
        if not root.left and not root.right:
            if sum(tmp) == expectNumber:
                res.append(tmp)
        if root.left:
            self.FindPathHelper(root.left, res, tmp[:], expectNumber)
        if root.right:
            self.FindPathHelper(root.right, res, tmp[:], expectNumber)

