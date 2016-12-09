#!/usr/bin/python

from string import ascii_lowercase
word = ascii_lowercase[::-1]
print(word[0:5] + 'U' + word[6:11] + 'O' + word[12:17] + 'I' + word[18:21] + 'E' + word[22:25] + 'A')