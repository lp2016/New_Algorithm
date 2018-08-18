# -*- coding:utf-8 -*-
#思路：进行分类讨论
# 1.如果有右孩子，则下一个结点是右子树的最左侧结点
# 2.如果没有右孩子，判断是不是根节点，是根节点的话输出None，不是的话转3
# 3.不是根节点的话，判断当前结点是不是父结点的左孩子，是的话父结点就是下一个结点，直接返回父结点
# 4.如果当前结点不是父结点的左孩子，则判断父结点的父结点。。，直到结点是父结点的左孩子或者空

#  （1）右字数
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:                       # 1
            return self.dfs(pNode.right)
        if not pNode.next:                   # 2
            return None
        if pNode.next.left == pNode:         # 3
            return pNode.next
        else:
            return self.dfs2(pNode.next)    # 4

    def dfs(self, node):
        if node.left:
            return self.dfs(node.left)
        return node
    def dfs2(self, node):
        if node.next:
            if node.next.left == node:
                return node.next
            else:
                return self.dfs2(node.next)
        return None

