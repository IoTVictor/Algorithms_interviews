# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 递归终止条件：达到了树A或者树B的叶节点，即遍历完某树
class Solution:
    # 遍历函数
    def HasSubtree(self, pRoot1, pRoot2):
        # 空树不是任意树的子结构
        if pRoot1 == None or pRoot2 == None:
            return False

        # 如果val相等，才会遍历树2的左右节点，与树1 对比
        def hasEqual(pRoot1, pRoot2):
            if pRoot2 == None:  # 树2 已遍历完毕
                return True
            if pRoot1 == None:
                return False
            if pRoot1.val == pRoot2.val:
                if pRoot2.left == None:
                    leftEqual = True
                else:
                    leftEqual = hasEqual(pRoot1.left, pRoot2.left)
                if pRoot2.right == None:
                    rightEqual = True
                else:
                    rightEqual = hasEqual(pRoot1.right, pRoot2.right)
                # 左边和右边同时相等
                return leftEqual and rightEqual
            return False
        # 判断根节点是否相等
        if pRoot1.val == pRoot2.val:
            ret = hasEqual(pRoot1, pRoot2)
            if ret:
                return True
        # 判断左节点是否和pRoot2相等
        ret = self.HasSubtree(pRoot1.left, pRoot2)
        if ret:
            return True
        ret = self.HasSubtree(pRoot1.right, pRoot2)
        return ret

pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.HasSubtree(pRoot1, pRoot8))