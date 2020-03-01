# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead == None:
            return None
        slow = pHead
        fast = pHead
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == None or fast.next == None:
            return None

        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast




    # def EntryNodeOfLoop(self, pHead):
    #     slow = pHead
    #     fast = pHead
    #     while(fast != None and fast.next != None):
    #         slow = slow.next
    #         fast = fast.next.next
    #         if slow == fast:  # 第一次相撞
    #             fast = pHead  # 让快指针重头开始,相当于记录了环的节点数
    #             # 此时slow领先fast的步数即环的节点数
    #             while fast != slow:
    #                 fast = fast.next
    #                 slow = slow.next
    #             return slow
    #     return None
    #
    #
