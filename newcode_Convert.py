#思路：其实就是中序遍历，只需要利用一个结点记录在访问当前结点之前访问的上一个结点
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.last_visit_node=None      #记录上一个访问的结点
    def Convert(self, pRootOfTree):
        # write code here
        self.ConvertHelper(pRootOfTree)
        #在将二叉搜索树变为双向链表后， self.last_visit_node指向了链表最后一个结点
        #所以需要从右到左找到链表的头结点并返回
        while self.last_visit_node and self.last_visit_node.left:
            self.last_visit_node = self.last_visit_node.left
        return self.last_visit_node


    def ConvertHelper(self, pRootOfTree):
        if not pRootOfTree:
            return

        #下面就是中序遍历的框架
        self.ConvertHelper(pRootOfTree.left)   #遍历左子树

        #处理根结点
        pRootOfTree.left = self.last_visit_node
        if self.last_visit_node:
            self.last_visit_node.right = pRootOfTree
        self.last_visit_node = pRootOfTree

        self.ConvertHelper(pRootOfTree.right)   #遍历右子树


