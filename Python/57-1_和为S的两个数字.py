# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # 递增数组tsum
        if len(array) < 2:
            return []
        # 双指针，从左和右一起向中间走
        # 找到符合条件的两个数，这两个数间隔越大，乘积便越小
        start = 0
        end = len(array) - 1
        while start < end:
            sum = array[start] + array[end]
            if sum < tsum:
                start += 1
            elif sum > tsum:
                end -= 1
            else:  # 如果相等，第一对即是乘积最小的
                return [array[start], array[end]]
        return []

test = [1,2,4,7,11,15]
s = Solution()
print(s.FindNumbersWithSum(test, 15))