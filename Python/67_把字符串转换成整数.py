# -*- coding:utf-8 -*-
class Solution:
    # 如果输出是0, 通过检查flag判断输入不合法还是输入直接是'0'
    # 不合格情况
    # 1字符串为空， 2只有一个正号或负号
    # 3包含非数字和“+-”以外的特殊字符
    # 4整数上溢出或下溢出：32位最大的正数整数0x7FFFFFFF,最小的负数整数0x80000000
    def StrToInt(self, s):
        flag = False
        if s == None or len(s) < 1:
            return 0
        numStack = []
        sign = 1
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in s:
            if i in dict.keys():
                numStack.append(dict[i])
            elif i == '+':
                continue
            elif i == '-':
                sign = -1
            else:
                return 0  # 不合法数字都置0
        # print(numStack)
        ans = 0
        # 只包含符号
        if len(numStack) == 0:
            return 0
        # 输入的数字是0
        if len(numStack) == 1 and numStack[0] == 0:
            flag = True
            print(flag)
            return 0
        for i in numStack:
            ans = ans*10 + i
        # 判断取值范围是否合法（牛客网测试必加）
        if sign == 1 and ans > 0x7FFFFFFF:
            return 0
        elif sign == -1 and ans > 0x80000000:
            return 0
        else:
            return sign*ans


# 合法输入
test = '123'
test0 = '-123-56'
test1 = '+2147483647'
test2 = '0'
# 不合法输入
test3 = '-2147483649'
test4 = '1a33'
test5 = ''
test6 = '+'
test7 = '+-'

s = Solution()
print(s.StrToInt(test))
print(s.StrToInt(test0))
print(s.StrToInt(test1))
print(s.StrToInt(test2))
print(s.StrToInt(test3))
print(s.StrToInt(test4))
print(s.StrToInt(test5))
print(s.StrToInt(test6))
print(s.StrToInt(test7))