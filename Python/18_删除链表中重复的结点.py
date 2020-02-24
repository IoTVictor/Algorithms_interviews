# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        dummy = ListNode(0)
        dummy.next = pHead
        prev = dummy
        cur = pHead

        while cur != None:
            # 有重复值的节点
            if cur.next != None and cur.next.val == cur.val:
                val = cur.val
                # 连续删除重复值
                while(cur != None and cur.val == val):
                    deleteNode = cur
                    prev.next = cur.next  # 前驱节点prev跳过当前重复节点，直接连上cur.next
                    cur = cur.next
                    del deleteNode  # 删除当前节点
            else:
                prev = prev.next
                cur = cur.next
        return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
# 1->2->5
print(s.deleteDuplication(node1).next.next.val)