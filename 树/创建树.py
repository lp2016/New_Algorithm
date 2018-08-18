# -*- coding:utf-8 -*-
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def CreateTree(data):
    q = deque()
    root = TreeNode(data[0])
    q.append(root)
    i = 0
    while i + 2 < len(data):
        tmp = q.popleft()
        if data[i + 1] != '#':
            tmp.left = TreeNode(data[i + 1])
            q.append(tmp.left)
        if data[i + 2] != '#':
            tmp.right = TreeNode(data[i + 2])
            q.append(tmp.right)
        i = i + 2
    return root

def printTree(root):
    q = deque()
    q.append(root)
    while len(q):
        tmp = q.popleft()
        print(tmp.val)
        if tmp.left:
            q.append(tmp.left)
        if tmp.right:
            q.append(tmp.right)


if __name__ == '__main__':
    root = CreateTree([1, 2, '#', 3, '#', 4, '#'])
    printTree(root)







