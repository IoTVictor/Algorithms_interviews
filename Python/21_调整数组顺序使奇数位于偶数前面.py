# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        k = 0  # 记录奇数偶数分割处
        for i in range(len(array)):
            if array[i] & 0x01 == 1:  # 找到奇数
                j = i
                while j > k:
                    array[j], array[j-1] = array[j-1], array[j]  # 奇数向前冒泡，放到已归位的奇数后面
                    j -= 1
                k += 1
        return array
S = Solution()
print(S.reOrderArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
