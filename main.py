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
    print("\t(running first-order approximation)")
    if length < 0:
        print("length cannot be lower than 0")
        return

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
        print("\t\taverage length of words: {}\n".format(ceil(word_lenghts / len(contents))))


# generates markov approximation of given order, based on the contents
# todo - this could work (recursion/clever iteration)
def markov(contents, freq, file_name, order=1, length=500):
    print("\t(running markov approximation of order {})\n".format(order))
    if length < 0:
        print("length cannot be lower than 0")
        return

    # 1 - 'a', 2 - 'b', (...), 27 = ' '
    count_matrix = []
    i = 0
    while i < order:
        #count_matrix =
        i += 1


# generates markov approximation of first order
def markov1(contents, freq, file_name, length=500):
    print("\t(running markov approximation of first order)\n")
    if length < 0:
        print("length cannot be lower than 0")
        return

    # count all possible doubles
    count_matrix = [[0 for i in range(27)] for j in range(27)]
    char_dict = {}
    id_dict = {}
    i = 0
    for key in freq.keys():
        char_dict[key] = i
        id_dict[i] = key
        i += 1
    for key1 in freq.keys():
        for key2 in freq.keys():
            cur_format = "{}{}".format(key1, key2)
            count_matrix[char_dict[key1]][char_dict[key2]] = contents.count(cur_format)

    with open("markov1-{}".format(file_name), 'w') as file_out:
        # first character based on first-order approximation
        prev1 = random.choices(list(freq.keys()), list(freq.values()))[0]

        # all other characters based on first order Markov sequence
        for i in range(length - 1):
            current = id_dict[
                random.choices(range(27), list(count_matrix[char_dict[prev1]]))[0]]  # choose next character
            file_out.write(prev1)  # write the last previous character
            prev1 = current  # shift current to previous


# generates Markov approximation of third order
def markov3(contents, freq, file_name, length=500):
    print("\t(running markov approximation of third order)\n")
    if length < 0:
        print("length cannot be lower than 0")
        return
    # todo


# generates Markov approximation of fifth order
def markov5(contents, freq, file_name, length=500):
    print("\t(running markov approximation of fifth order)\n")
    if length < 0:
        print("length cannot be lower than 0")
        return
    # todo


# Main function, carrying out all chosen approximations based on given norm sample
def run_approx(file_name, first=True, cond_prob=True, mar1=True, mar3=True, mar5=True):
    print("\n\ncurrent file: {}\n".format(file_name))
    freq = {}
    with open(file_name, 'r') as file:
        contents = file.readline()  # as all contents in single line
        for char in contents:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        print("\tcount of characters:\n{}\n".format(
            {key: value for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True)}))
        remove_digits(freq)
        print("\tcount of characters(no digits):\n{}\n".format(
            {key: value for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True)}))
        print("\tno. of characters(no digits): {}\n".format(sum(freq.values())))

        if first:
            first_order(freq, file_name)

        # find two most frequent characters
        if freq['a'] > freq['b']:
            max_first = 'a'
            max_second = 'b'
        else:
            max_first = 'b'
            max_second = 'a'
        for key in freq.keys():
            if freq[key] > freq[max_first]:
                max_second = max_first
                max_first = key
            elif freq[key] > freq[max_second]:
                max_second = key
        print("\tmost frequent character: \'{}\', second most frequent: \'{}\'\n".format(max_first, max_second))

        if cond_prob:
            # probabilities of occurring after two most frequent characters
            first_dict = {}
            second_dict = {}
            # count occurrences of all possible doubles
            for key in freq.keys():
                first_format = "{}{}".format(max_first, key)
                second_format = "{}{}".format(max_second, key)
                first_dict[first_format] = contents.count(first_format)
                second_dict[second_format] = contents.count(second_format)
            # convert count into probabilities
            first_format_total = sum(first_dict.values())
            second_format_total = sum(second_dict.values())
            for key in freq.keys():
                first_format = "{}{}".format(max_first, key)
                second_format = "{}{}".format(max_second, key)
                first_dict[first_format] /= first_format_total
                second_dict[second_format] /= second_format_total
            print("\tconditional probabilities of the following doubles:")
            print("\tnote: due to need for the same probabilistic space, the formula is:"
                  "\tP(\"e|a\") = P(\"ea\")/P(\"e*\")\n")
            print("{}\n".format(
                {key: value for key, value in sorted(first_dict.items(), key=lambda item: item[1], reverse=True)}))
            print("{}\n".format(
                {key: value for key, value in sorted(second_dict.items(), key=lambda item: item[1], reverse=True)}))

        # Markov approximations
        if mar1:
            markov1(contents, freq, file_name)
        if mar3:
            markov3(contents, freq, file_name)
        if mar5:
            markov5(contents, freq, file_name)


# MAIN PROGRAM
# zeroth-order approximation
chars = [chr(letter) for letter in range(ord('a'), ord('z') + 2)]
chars[26] = ' '
zeroth(chars)

# all other approximations; adjust parameters for desired approximations
run_approx("norm_hamlet.txt",
           first=False,
           cond_prob=False,
           mar1=True,
           mar3=False,
           mar5=False)
# run_approx("norm_romeo_and_juliet.txt",
#            first=False,
#            cond_prob=False,
#            mar1=False,
#            mar3=False,
#            mar5=False)
# run_approx("norm_wiki_sample.txt",
#            first=False,
#            cond_prob=False,
#            mar1=False,
#            mar3=False,
#            mar5=False)
