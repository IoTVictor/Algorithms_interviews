# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode == None:
            return None
        # 1、寻找右子树，如果存在就一直找，直到右子树的最左边就是下一个节点
        if pNode.right:
            tmpNode = pNode.right
            while tmpNode.left:
                tmpNode = tmpNode.left
            return tmpNode
        else:
        # 2、没有右子树，就寻找他的父节点，直到找到它是父节点的左子树，打印父节点
            tmpNode = pNode
            while tmpNode.next:
                if tmpNode.next.left == tmpNode:
                    return tmpNode.next
                tmpNode = tmpNode.next  # 重新赋值,下次循环中继续找父节点的父节点
            return None
