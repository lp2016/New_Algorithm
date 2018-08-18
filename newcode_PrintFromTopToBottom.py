# -*- coding:utf-8 -*-
#思路：层序遍历，利用队列实现
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def __init__(self):
        self.p=-1
        self.r=-1
        self.data=[]
    def inqueue(self,node):
        self.data.append(node)
        self.r+=1
    def outqueue(self):
        self.p+=1
        return self.data[self.p]
    def isEmpty(self):
        if self.p == self.r:
            return True
        else:
            return False
    def PrintFromTopToBottom(self, root):
        # write code here
        result=[]
        if not root:
            return []
        else:
            result.append(root.val)
            if root.left:
                self.inqueue(root.left)
            if root.right:
                self.inqueue(root.right)
            while not self.isEmpty():
                q = self.outqueue()
                result.append(q.val)
                if q.left:
                    self.inqueue(q.left)
                if q.right:
                    self.inqueue(q.right)
        return result


