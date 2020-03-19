# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if len(numbers) == 0:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        num = numbers[0]
        count = 1
        # 计数法
        for i in range(1, len(numbers)):
            if count == 0:
                num = numbers[i]
                count = 1
            elif numbers[i] == num:
                count += 1
            else:
                count -= 1
            # print(numbers[i], count)
        print("num:", num, ",count:", count)
        # 验证最多的数，是否满足超过长度一半
        times = 0
        for i in range(len(numbers)):
            if numbers[i] == num:
                times += 1
        if times > len(numbers)/2:
            return num
        else:
            return 0

S = Solution()
print(S.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(S.MoreThanHalfNum_Solution([1, 2, 3, 3, 3, 3, 4]))
print(S.MoreThanHalfNum_Solution([1, 2]))


