"""
Enter a search word to find its definition

Usage: docopt_smartsnek [-h] <search_word>

Arguments:
    search_word    Word to search for the definition of.

Options:
    -h --help      Show help text.
"""
from docopt import docopt

from smartsnek import Word


def search_for_word(search_word):
    word = Word(search_word)
    print(word)


def main():
    args = docopt(__doc__)
    search_for_word(args['<search_word>'])
