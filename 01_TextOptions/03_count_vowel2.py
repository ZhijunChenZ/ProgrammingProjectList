# _*_ coding:utf-8 _*_

"""
输入一个字符串，统计出其中元音字母的数量。
更复杂点的话，统计出每个元音字母的数量。
"""

vowel = 'aeiouAEIOU'
word = raw_input('Please input a word: ')

class CheckVowel(object):

    def __init__(self, word):
        self.word = word

    def check_vowel_num(self):
        count = 0
        for w in word:
            if w in vowel:
                count += 1
        return count

    def check_a(self):
        count = 0
        for w in word:
            if (w == 'a') or (w == 'A'):
                count += 1

        return 'a', count

    def check_e(self):
        count = 0
        for w in word:
            if (w == 'e') or (w == 'E'):
                count += 1

        return 'e', count

    def check_i(self):
        count = 0
        for w in word:
            if (w == 'i') or (w == 'I'):
                count += 1

        return 'i', count

    def check_o(self):
        count = 0
        for w in word:
            if (w == 'o') or (w == 'O'):
                count += 1

        return 'o', count

    def check_u(self):
        count = 0
        for w in word:
            if (w == 'u') or (w == 'U'):
                count += 1

        return 'u', count

if __name__ == '__main__':
    check = CheckVowel(word)
    vowel_num = check.check_vowel_num()
    print vowel_num
    print check.check_a()
    print check.check_e()
    print check.check_i()
    print check.check_o()
    print check.check_u()
