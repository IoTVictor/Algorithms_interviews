# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # 判断二维列表为空特例
        rows = len(array)  # 行
        if rows == 0:
            return False
        # 若list本身就是空的，当访问到list[0]的时候，会出错误IndexError: list index out of range
        cols = len(array[0])  # 列
        if cols == 0:
            return False

        # 初始点左下角
        i = rows - 1  # 行（因为数组下标从零开始）
        j = 0  # 列
        while j <= cols-1 and i >= 0:
            # 查询目标值大于当前值，删除当前列，列坐标往右走
            if target > array[i][j]:
                j += 1
            # 查询目标值小于当前值，删除当前行，行坐标往上走
            elif target < array[i][j]:
                i -= 1
            # 找到target值
            else:
                return True
        return False

array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
array2 = []
findtarget = Solution()
print(findtarget.Find(10, array))
print(findtarget.Find(30, array))
print(findtarget.Find(13.0, array))
print(findtarget.Find(10, array2))

