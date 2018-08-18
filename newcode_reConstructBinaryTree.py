# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        if not tin:
            root = TreeNode(pre[0])
            return root
        root=TreeNode(pre[0])
        k=tin.index(pre[0])
        left_data = tin[0:k]
        righ_data = tin[k + 1:len(tin)]
        root.left=self.rootNode(left_data,pre[1:k+1])
        root.right=self.rootNode(righ_data,pre[k+1:len(pre)])
        return root

    def rootNode(self,tin,pre):
        if not tin  or not pre :
            return None
        root = TreeNode(pre[0])
        k = tin.index(pre[0])
        left_data = tin[0:k]
        righ_data = tin[k + 1:len(tin)]
        root.left=self.rootNode(left_data,pre[1:k+1])
        root.right=self.rootNode(righ_data,pre[k+1:len(pre)])
        return root

root=Solution().reConstructBinaryTree([],[4])
print(root)