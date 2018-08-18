# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def create_LinkList(nums):
    head = ListNode(nums[0])
    p = head
    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        p.next = node
        p = p.next
    return head

def print_LinkList(head):
    p = head
    while p:
        print(p.val)
        p = p.next

