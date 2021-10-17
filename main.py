import random
from math import ceil


# 26 lower case letters of English alphabet, digits, space (37 characters total)

# Outputs zeroth-order approximation using provided set of characters, of some given length (300 by default)
def zeroth(chars=None, length=300):
    if chars is None:
        chars = ['a', 'b', 'c', 'd']
    chars_len = len(chars)

    with open('zeroth.txt', 'w') as fout:
        for i in range(1, length + 1):
            fout.write(chars[random.randrange(chars_len)])


# Removes digits from given dictionary
def remove_digits(dictionary):
    for key in [chr(char) for char in range(ord('0'), ord('9') + 1)]:
        if key in dictionary.keys():
            dictionary.pop(key)


# Outputs first-order approximation of some length, given frequency dictionary
def first_order(freq, file_name, length=500):
    if length < 0:
        print("length cannot be lower than 0")
        return

    total = sum(freq.values())
    for key in freq.keys():
        freq[key] = freq[key] / total

    # generate approximation
    with open('first-order-{}'.format(file_name), 'w') as fout:
        i = 0
        while i < length:
            fout.write("{}".format(random.choices(list(freq.keys()), list(freq.values()))[0]))
            i += 1

    # calculate average word length
    with open('first-order-{}'.format(file_name), 'r') as file:
        contents = file.readlines()
        contents = contents[0].split()
        word_lenghts = 0
        for word in contents:
            word_lenghts += len(word)
        print("\taverage length of words: {}\n".format(ceil(word_lenghts / len(contents))))


# Main function, carrying out all the approximations based on given norm sample
def run_approx(file_name):
    print("\n\ncurrent file: {}\n".format(file_name))
    freq = {}
    with open(file_name, 'r') as file:
        contents = file.readlines()
        for word in contents:
            for char in word:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1

        print("\tfrequencies:\n{}\n".format(
            {key: value for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True)}))
        remove_digits(freq)
        print("\tfrequencies(no digits):\n{}\n".format(
            {key: value for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True)}))
        total = sum(freq.values())
        print("\tno. of characters(no digits): {}\n".format(total))

        first_order(freq, file_name)


# MAIN PROGRAM
# zeroth-order approximation
chars = [chr(letter) for letter in range(ord('a'), ord('z') + 2)]
chars[26] = ' '
zeroth(chars, 1000)

# all other approximations
run_approx("norm_hamlet.txt")
run_approx("norm_romeo_and_juliet.txt")
run_approx("norm_wiki_sample.txt")
