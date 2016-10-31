# _*_ coding:utf-8 _*_

"""
判断用户输入的字符串是否为回文。
回文是指正反拼写形式都是一样的词，譬如“racecar”。
"""

def new_stri(old):
    new_data = ''
    for i in range(len(old)):
        if old[i] == old[len(old) - i - 1]:
            new_data += old[len(old) - i - 1]

    return new_data

def check_palindromic(old):
    new = new_stri(old)
    if new == old:
        print "This word is a palindrome."
    else:
        print "It's not a palindrome."

if __name__ == '__main__':
    while True:
        check_palindromic(raw_input("Please input a word: "))

        Q = raw_input('Quit? y/n ')
        if Q == 'y':
            break
