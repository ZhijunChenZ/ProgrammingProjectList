# _*_ coding:utf-8 _*_

"""
将一个英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay。
譬如“banana”会变成“anana-bay”。
"""

vowel = 'aeiouAEIOU' # 元音
semivowel = 'ywYW' # 半元音
word = raw_input('Please input a word: ')

def pick_consonant(word): # 查找并提取第一个辅音
    consonant_word = ''
    for w in word:
        if (w not in vowel) and (w not in semivowel):
            consonant_word += w
            break
    return consonant_word

def ladingzhu(first_consonant_word):
    position = word.index(first_consonant_word)
    before = word[:position]
    after = word[position + 1:]
    new_word = before + after + first_consonant_word + '-ay'
    print new_word

first_consonant_word = pick_consonant(word)
ladingzhu(first_consonant_word)
