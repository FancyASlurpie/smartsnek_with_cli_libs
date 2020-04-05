import argparse

from smartsnek import Word


def search_for_word(search_word):
    word = Word(search_word)
    print(word)


def main():
    parser = argparse.ArgumentParser(description="Enter a search word to find its definition")
    parser.add_argument('search_word', help="Word to search for the definition of.")
    args = parser.parse_args()
    search_for_word(args.search_word)
