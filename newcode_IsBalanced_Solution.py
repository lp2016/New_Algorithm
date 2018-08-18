#思路 Solution2的方法在求结点深度时，会重复访问结点
#Solution 的方法采用后序遍历的方法，每个结点只遍历一次
#并且在后序遍历的过程中同时统计左右子树深度
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        left_depth = self.IsBalanced_SolutionHelper(pRoot.left)
        if left_depth < 0:
            return False
        right_depth = self.IsBalanced_SolutionHelper(pRoot.right)
        if right_depth < 0:
            return False

        if abs(left_depth - right_depth) > 1:
            return False
        return True

    def IsBalanced_SolutionHelper(self, pRoot):
        if not pRoot:
            return 0
        left_depth = self.IsBalanced_SolutionHelper(pRoot.left)
        if left_depth < 0:
            return -1
        right_depth = self.IsBalanced_SolutionHelper(pRoot.right)
        if right_depth < 0:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        else:
            return max(left_depth, right_depth) + 1

    def IsBalanced_Solution2(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left_depth = self.Depth(pRoot.left)
        right_depth = self.Depth(pRoot.right)
        if abs(left_depth - right_depth) > 1:
            return False
        else:
            return True

        return self.IsBalanced_Solution2(pRoot.left) and self.IsBalanced_Solution2(pRoot.right)

    def Depth(self, root):
        if not root:
            return 0
        return max(self.Depth(root.left), self.Depth(root.right)) + 1



