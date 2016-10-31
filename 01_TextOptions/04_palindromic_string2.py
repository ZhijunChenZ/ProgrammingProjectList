# _*_ coding:utf-8 _*_

"""
判断用户输入的字符串是否为回文。
回文是指正反拼写形式都是一样的词，譬如“racecar”。
"""

def check_palindrome(data):
    while True:
        i = 1
        if data[i - 1].lower() == data[len(data) - i].lower():
            i += 1
            print "This word is a palindrome."
        else:
            print "It's not a palindrome."
            break

        return i

if __name__ == '__main__':
    while True:
        check_palindrome(raw_input('Please input a word: '))
        Q = raw_input('Quit? y/n ')
        if Q == 'y':
            break
