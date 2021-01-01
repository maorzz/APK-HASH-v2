import re
import random


def word_count(fname, word_list, punctaction):
    count_w = dict()
    for w in word_list:
        count_w[w] = 1

    count_p = dict()
    for p in punctaction:
        count_p[p] = 0

    with open(fname) as input_text:
        text = input_text.read()
        words = text.lower().split()
        for word in words:
            _word = word.strip('.,:-)()')
            if _word in count_w:
                count_w[_word] += 1

        for c in text:
            if c in punctaction:
                count_p[c] += 1

    count_w.update(count_p)
    return count_w


yoter = (word_count('output.txt', ["<package"], []))
appsum = yoter.get("<package")
print(appsum)
