# -*- coding:utf-8 -*-
# 请实现两个函数，分别用来序列化和反序列化二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        retList = []
        def preOrder(root):
            if root == None:
                retList.append('#')
                return

            retList.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        return ' '.join(retList)

    def Deserialize(self, s):
        # write code here
        retList = s.split()
        if retList == []:
            return None

        def dePreOrder():
            rootVal = retList[0]
            del retList[0]
            if rootVal == '#':
                return None

            node = TreeNode(int(rootVal))

            leftNode = dePreOrder()
            rightNode = dePreOrder()

            node.left = leftNode
            node.right = rightNode

            return node

        pRoot = dePreOrder()
        return pRoot

pRoot1 = TreeNode(1)
pRoot2 = TreeNode(2)
pRoot3 = TreeNode(4)
pRoot4 = TreeNode(3)
pRoot5 = TreeNode(5)
pRoot6 = TreeNode(6)

pRoot1.left = pRoot2
pRoot1.right = pRoot4

pRoot2.left = pRoot3

pRoot4.left = pRoot5
pRoot4.right = pRoot6

s = Solution()
serializeStr = s.Serialize(pRoot1)
print('序列化后的字符串：', serializeStr)
print('反序列化后的根节点值：', s.Deserialize(serializeStr).val)

