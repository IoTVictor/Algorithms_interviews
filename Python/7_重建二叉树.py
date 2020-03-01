# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        # 如果set的元素不同，则输入有误
        if set(pre) != set(tin):
            return None
        root = TreeNode(pre[0])
        # 取中序遍历中root的下标i
        i = tin.index(pre[0])
        # 左子树中序tin[:i]，右子树中序[i+1:]
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root
