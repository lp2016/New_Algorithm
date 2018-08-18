# -*- coding:utf-8 -*-
#思路：翻转链表：递归
#      
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        return self.RL(pHead)[1]
    def RL(self,pHead):
        if pHead.next == None:
            return pHead,pHead
        r,re=self.RL(pHead.next)
        r.next=pHead
        pHead.next=None
        return pHead,re

p1=ListNode(1)
p2=ListNode(2)
p3=ListNode(3)
p4=ListNode(4)
p5=ListNode(5)
p1.next=p2
p2.next=p3
p3.next=p4
p4.next=p5
p5.next=None
r=Solution().ReverseList(p1)
print()