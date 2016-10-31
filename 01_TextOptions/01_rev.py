# _*_ coding:utf-8 _*_

"""
输入一个字符串，将其逆转并输出。
"""

stri = raw_input('Please input a string: ')
rev = ''
for i in range(len(stri)):
    rev += stri[len(stri) - i - 1]

print rev
