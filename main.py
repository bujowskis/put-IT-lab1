import random

# 26 lower case letters of English alphabet, digits, space (37 characters total)

# Function outputting zeroth-order approximation using provided set of characters, of some given length (300 by default)
def zeroth(chars=None, length=300):
    if chars is None:
        chars = ['a', 'b', 'c', 'd']
    chars_len = len(chars)

    fout = open('zeroth.txt', 'w')
    for i in range(1, length + 1):
        fout.write(chars[random.randrange(chars_len)])

# MAIN PROGRAM
# pool of characters used for
chars = [chr(letter) for letter in range(ord('a'), ord('z') + 2)]
chars[26] = ' '

zeroth(chars, 1000) # zeroth-order approximation

# first file - hamlet
with open('norm_hamlet.txt', 'r') as file:
    contents = file.readlines()
    # print(contents, "\n")

# second file - romeo and juliet
with open('norm_romeo_and_juliet.txt', 'r') as file:
    contents = file.readlines()
    # print(contents, "\n")

# third file - wiki sample
with open('norm_wiki_sample.txt', 'r') as file:
    contents = file.readlines()
    # print(contents, "\n")
