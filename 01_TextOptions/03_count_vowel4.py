# _*_ coding:utf-8 _*_

"""
输入一个字符串，统计出其中元音字母的数量。
更复杂点的话，统计出每个元音字母的数量。
"""

vowel = 'aeiouAEIOU'

def ch(word):
    result = {}
    for c in word:
        if c in vowel:
            result[c] = result.get(c, 0) + 1

    return result

if __name__ == '__main__':
    while True:
        result = ch(raw_input('word: '))
        print sum(result.values())
        for k, v in result.items():
            print k, v

        Q = raw_input('Quit? y/s ')
        if Q == 'y':
            break
