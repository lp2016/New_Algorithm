# -*- coding:utf-8 -*-
#思路：参照 https://blog.csdn.net/shansusu/article/details/50285735
#      利用两个指针p1和p2，p1每次移动一步，p2每次移动2步。如果链表中有环，那么p1和p2一定会相遇，记住。。。。
#      相遇之后，p1指向下一个结点，p2指向头结点，当p1和p2再次相遇的时候，就是环的入口点
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        #如果链表为空返回空
        if not pHead:
            return None
        #如果链表只有一个元素，不存在环，自然不存在环的入口
        if not pHead.next:
            return None

        p1 = pHead
        p2 = pHead.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next.next
        p2 = pHead
        p1 = p1.next
        while True:
            if p1 == p2 :
                return p1
            p1 = p1.next
            p2 = p2.next


a = [None]*8
for i in range(1, 8):
    a[i] = ListNode(i)

for i in range(1, 7):
    a[i].next = a[i+1]
a[7].next = a[4]
print(Solution().EntryNodeOfLoop(a[1]))