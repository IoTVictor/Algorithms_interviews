class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1）首先判断是几位数，用digits表示
        print('——————求第', n, '个数字——————')
        base = 9
        digits = 1
        while n - base * digits > 0:
            n -= base*digits
            base *= 10
            digits += 1
        # 此时，n 表示为digits位数的第n个位
        print('digits:', digits, 'n:', n)
        # 2）计算目标数字number
        idx = n % digits
        if idx == 0:
            idx = digits
        number = 1
        for i in range(1, digits):
            number *= 10

        if idx == digits:
            number += n//digits - 1
        else:
            number += n//digits

        print('number:', number, ',idx:', idx)

        # 3)找到number的对应位
        for i in range(idx, digits):
            number //= 10
        return number % 10

s = Solution()
print(s.findNthDigit(364))
print(s.findNthDigit(365))
print(s.findNthDigit(366))
print(s.findNthDigit(11))
print(s.findNthDigit(12))