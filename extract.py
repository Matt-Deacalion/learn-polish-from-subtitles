#!/usr/bin/env python3

import re
import sys
from collections import Counter


def count_occurences(items, limit=1000):
    """
    Takes a list of items and returns an ordered list of the most
    commonly occuring items in that list. The returned list will
    be equal to or less than `limit` length.
    """
    return Counter(items).most_common(n=limit)


def remove_non_words(line):
    """
    Takes a string and removes characters that serve no purpose for
    our task. This includes puncuation, digits and special characters.
    """
    non_word = [
        '`', '!', '"', '£', '$', '%', '^', '&', '*', '(', ')',
        '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        '-', '=', '¬', '+', '_', '\\', '|', ',', '.', '/', ';',
        '\'', '#', '[', ']', '{', '}', ':', '@', '~', '<', '>',
    ]

    regex = '[' + re.escape(''.join(non_word)) + ']'

    # replace non-word characters with spaces
    clean = re.sub(regex, ' ', line)

    # replace instances of two or more spaces with a single space
    return re.sub('\s+', ' ', clean).strip()


def test_removes_useless_chars():
    """
    Characters that serve no purpose for our task must be removed.
    """
    line = '~{}`¬1.-_"\'£$%^&*() This: [line] <|>=+ has; \\some/,# @characters!?'

    assert remove_non_words(line) == 'This line has some characters'


def test_count_occurences():
    """
    Occurences of words must be counted accurately.
    """
    words = ['Uno', 'Boom', 'Uno', 'Milkshake', 'Uno', 'Boom']
    counts = count_occurences(words)

    assert counts == [('Uno', 3), ('Boom', 2), ('Milkshake', 1)]


def test_count_occurences_limit():
    """
    Occurences of words must be obey `limit`.
    """
    assert len(count_occurences(['I', 'like', 'tea'], limit=1)) == 1


def main():
    if len(sys.argv) == 1:
        print('Please specify one or more file containing subtitles.')
        sys.exit()

    content = ''

    for word_file in sys.argv[1:]:
        try:
            with open(word_file) as f:
                content += f.read().lower()
        except IOError:
            print('Unable to open file "{}"'.format(word_file))

    content = remove_non_words(content).split()

    for i, count in enumerate(count_occurences(content)):
        print('{}. {}'.format(i + 1, count[0]))

if __name__ == '__main__':
    main()
