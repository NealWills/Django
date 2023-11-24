#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# a = 3

# def syntax1():
#     if a == 2:
#         print ("Answer")
#         print ("True")
#     else:
#         print ("Answer")
#   print ("False")    # 缩进不一致，会导致运行错误

# syntax1()

# def syntax2():
#     if a == 3:
#         print("Answer")
#         print("True")
#     else:
#         print("Answer")
#         print("False")

# syntax2()

# def syntax3():
#     if a == 3:
#         print("Answer")
#         print("True")
#     else:
#         print("Answer")
#     print("False")

# syntax3()

# def syntax4():
#     total = "a" + \
#             "pp" + \
#             "le"
#     print(total)
#
#
# syntax4()


# def syntax7():
#     # 最简单的函数
#     def hello():
#         print("Hello World!")
#
#     hello()  # 打印结果 Hello World!
#
#     # 带参数的函数
#     def max_num(num1, num2):
#         if num1 > num2:
#             return num1
#         else:
#             return num2
#
#     c1 = 20
#     c2 = 30
#     print(max_num(c1, c2))  # 打印结果 30
#     # 同时可以在传参时进行函数运算
#     print(max_num(40, max_num(50, 20)))  # 打印结果 50


# syntax7()

# def syntax5():
#     a = 1
#     b = False
#     c = "aaa"
#     d = ["a", "b", "c"]
#     e = (1, 2)
#     f = {"a": 1, "b": 2}
#     g = True
#     print(type(a), type(b), type(c), type(d), type(e), type(f))
#     print(type(a) == type(b))
#     print(type(b) == type(g))
#
#
# syntax5()

# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# def syntax6():
#     print(type(A()), type(B()))
#     print(type(A()) == type(B()))
#
#
# syntax6()

# def syntax_number():
#     a = 3  # int
#     b = 4  # int
#     c = 1.5  # float
#     d = True
#     e = False
#
#     r0 = a + b  # 加法 int + int = int               7 <class 'int'>
#     r1 = a + c  # 加法 int + float = float           4.5 <class 'float'>
#     r2 = a - b  # 减法 int - int = int               -1 <class 'int'>
#     r3 = a - c  # 减法 int - float = float           1.5 <class 'float'>
#     r4 = a * b  # 乘法 int * int = int               12 <class 'int'>
#     r5 = a * c  # 乘法 int * float = float           4.5 <class 'float'>
#     r6 = a / b  # 除法，得到一个浮点数 int / int = float         0.75 <class 'float'>
#     r7 = a / c  # 除法，得到一个浮点数 int / float = float       2.0 <class 'float'>
#     r8 = 4 / 2  # 除法，得到一个浮点数 int / int = float         2.0 <class 'float'>
#     r9 = a // b  # 除法，得到一个整数 int // int = int           0 <class 'int'>
#     r10 = a // c  # 非规则除法，得到一个float型的整数 int // float = float         2.0 <class 'float'>
#     r11 = c // a  # 非规则除法，得到一个float型的整数 float // int = float        0.0 <class 'float'>
#     r12 = a % b  # 取余 int % int = int               3 <class 'int'>
#     r13 = a % c  # 取余 int % float = float           0.0 <class 'float'>
#     r14 = c % a  # 取余 float % int = float           1.5 <class 'float'>
#     r15 = a ** b  # 乘方 int ** int = int           81 <class 'int'>
#     r16 = a ** c  # 乘方 int ** float = float       5.196152422706632 <class 'float'>
#     r17 = c ** a  # 乘方 float ** int = float       3.375 <class 'float'>
#     r18 = d + e     # 1 <class 'int'>
#     r19 = d * e     # 0 <class 'int'>
#     r20 = d * a     # 3 <class 'int'>
#     r21 = d * c     # 1.5 <class 'float'>
#     r22 = d         # True <class 'bool'>
#     result = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22]
#
#     for r in range(0, len(result)):
#         print(r, result[r], type(result[r]))
#
#
# syntax_number()

# def syntax_list():



# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyTestSite.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)
#
#
# if __name__ == '__main__':
#     main()
