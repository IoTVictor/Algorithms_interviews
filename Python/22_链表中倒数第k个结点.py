# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # 防止头指针为空，或k无意义
        if head == None or k <= 0:
            return None
        # 快慢指针：实现仅一次遍历链表
        pAhead = head
        pBehind = head
        # 先让快指针前进k-1步
        for i in range(k-1):
            # 防止节点数少于k，造成访问空指针
            if pAhead.next != None:
                pAhead = pAhead.next
            else:
                return None  # 节点数少于k

        while pAhead.next != None:
            pAhead = pAhead.next
            pBehind = pBehind.next
        return pBehind


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

S = Solution()
print(S.FindKthToTail(node1, 5).val)


