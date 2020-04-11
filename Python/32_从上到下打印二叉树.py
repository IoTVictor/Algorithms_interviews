# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。(双端队列)
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        queue = []  # 双端队列,存储TreeNode
        result = []  # 存储弹出的队头值
        if root == None:
            return []

        queue.append(root)
        while len(queue) > 0:
            queueHead = queue.pop(0)  # 弹出队首的树节点（出队）
            result.append(queueHead.val)  # 存储被弹出树节点的值
            # 左右孩子节点入队
            if queueHead.left:
                queue.append(queueHead.left)
            if queueHead.right:
                queue.append(queueHead.right)
        return result


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
print(S.PrintFromTopToBottom(pNode1))
