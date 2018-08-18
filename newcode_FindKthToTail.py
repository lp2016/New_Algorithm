# -*- coding:utf-8 -*-
#思路：利用两个指针，第一个指针走到第k个结点的时候，第二个指针开始走：
#      这样：当地一个指针走到最后一个结点时，第二个指针走到了第n-k+1个结点，即倒数第k个结点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k<=0:
            return None
        r=None
        p=q=head
        c=1
        while p:
            if c>=k:
                r=q
                q=q.next
            c+=1
            p=p.next
        return r
