# _*_ coding:utf-8 _*_

"""
输入一个字符串，统计出其中元音字母的数量。
更复杂点的话，统计出每个元音字母的数量。
"""

vowel = 'aeiouAEIOU'
while True:
    word = raw_input('Please input a word: ')
    count = 0
    for w in word:
        if w in vowel:
            count += 1
    print count
    Q = raw_input('Quit?y/n ')
    if Q == 'y':
        break
