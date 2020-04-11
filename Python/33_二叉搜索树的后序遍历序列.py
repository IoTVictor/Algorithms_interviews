# -*- coding:utf-8 -*-
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        return self.check(sequence, 0, len(sequence)-1)
    def check(self, arr, start, end):
        if start >= end:
            return True
        root = arr[end]
        end = end - 1
        while end >= 0 and arr[end] > root:
            end -= 1
        # 向前查找第一个小于root的值，mid-1就是分割处
        mid = end + 1
        for i in range(start, mid):
            if arr[i] > root:
                return False
        # 递归验证左子树[start,mid-1],右子树[mid,end]
        return self.check(arr, start, mid-1) and self.check(arr, mid, end)

# 测试代码
array = [5, 7, 6, 9, 11, 10, 8]
array2 = [7, 4, 6, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySquenceOfBST(array))
print(S.VerifySquenceOfBST(array2))
print(S.VerifySquenceOfBST(array3))
