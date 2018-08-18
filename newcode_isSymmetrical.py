# -*- coding:utf-8 -*-
#思路：比较左孩子的右子树和右孩子的左子树，递归实现
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.isSymmetricalHelper(pRoot.left, pRoot.right)

    def isSymmetricalHelper(self, p1, p2):
        if (p1 and not p2) or (p2 and not p1):
            return False
        if not p1 and not p2:
            return True
        if p1.val != p2.val:
            return False
        return self.isSymmetricalHelper(p1.right,p2.left) and self.isSymmetricalHelper(p1.left, p2.right)

