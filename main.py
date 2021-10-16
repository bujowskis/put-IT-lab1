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


def remove_digits(dictionary):
    for key in [chr(char) for char in range(ord('0'), ord('9') + 1)]:
        if key in dictionary.keys():
            dictionary.pop(key)


# Function outputting first-order approximation of some length, given a dictionary
# def first_order(dict, length=500):


# MAIN PROGRAM
# pool of characters used for
chars = [chr(letter) for letter in range(ord('a'), ord('z') + 2)]
chars[26] = ' '
zeroth(chars, 1000)  # zeroth-order approximation

freq = {}
print("\n\nfirst file - hamlet\n")
with open('norm_hamlet.txt', 'r') as file:
    contents = file.readlines()
    for word in contents:
        for char in word:
            if char in range(ord('0'), ord('9') + 1):
                continue
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    print("frequencies in hamlet:\n{}\n".format(
        {key: value for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True)}))

    remove_digits(freq)
    total = sum(freq.values())

print("\n\nsecond file - romeo and juliet\n")
with open('norm_romeo_and_juliet.txt', 'r') as file:
    contents = file.readlines()
    for word in contents:
        for char in word:
            if char in range(ord('0'), ord('9') + 1):
                continue
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    print("frequencies in romeo and juliet:\n{}\n".format(
        {key: value for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True)}))

    remove_digits(freq)
    total = sum(freq.values())

print("\n\nthird file - wiki sample\n")
with open('norm_wiki_sample.txt', 'r') as file:
    contents = file.readlines()
    for word in contents:
        for char in word:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    print("frequencies in wiki:\n{}\n".format(
        {key: value for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True)}))

    remove_digits(freq)
    total = sum(freq.values())

