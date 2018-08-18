# -*- coding:utf-8 -*-
#思路：中序遍历
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from 树.创建树 import CreateTree
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.count = 0
    def KthNode(self, pRoot, k):     #递归版
        # write code here

        if not pRoot:
            return None
        if pRoot.left:
            tmp = self.midOrder(pRoot.left, k)
            if k == self.count:
                return tmp
        self.count = self.count + 1
        if k == self.count:
            return pRoot
        if pRoot.right:
            tmp = self.midOrder(pRoot.right, k)
            if k == self.count:
                return tmp
        return None
    def midOrder(self, pRoot, k):
        if pRoot.left:
            tmp = self.midOrder(pRoot.left, k)
            if k == self.count:
                return tmp
        self.count = self.count + 1
        if k == self.count:
            return pRoot
        if pRoot.right:
            tmp = self.midOrder(pRoot.right, k)
            if k == self.count:
                return tmp

    def KthNode2(self, pRoot, k):  #非递归版
        if not pRoot:
            return None
        s = [pRoot]
        tmp = pRoot.left
        count = 0
        while len(s) or tmp :
            while tmp:
                s.append(tmp)
                tmp = tmp.left
            res = s.pop()
            count += 1
            if count == k:
                return res
            tmp = res.right
        return None

root = CreateTree([1,2,3,'#',4,'#',5])
print(Solution().KthNode2(root, 2).val)