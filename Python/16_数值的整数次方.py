# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # 特例底数为0且指数为负（0不能求倒数）
        if self.equal_zero(base) and exponent < 0:
            return ZeroDivisionError
        result = self.power_value(base, abs(exponent))
        if exponent < 0:
            return 1.0/result
        else:
            return result

    # 判断底数base是不是等于0的时候,不能直接写base==0
    # 因为计算机内表示小数时有误差,只能判断他们的差的绝对值是不是在一个很小的范围内
    def equal_zero(self, base):
        if abs(base - 0.0) < 0.0000001:
            return True

    def power_value(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        result = self.power_value(base, exponent >> 1)  # 用右移操作，代替“除以2”, 如2的5次方，可以先求2的2次方（5//2=2）
        result *= result
        # 如果求奇数次幂
        # 用“&与”来代替“%2”，判断奇偶数
        if exponent & 1 == 1:
            result = result * base

        return result


S = Solution()
print(S.Power(2, 5))
print(S.Power(5, -2))
print(S.Power(0, -2))  # 异常特例
