import click

from smartsnek import Word

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("search_word", metavar='<search_word>')
def search_for_word(search_word):
    """
    Enter a search word to find its definition

    search_word    Word to search for the definition of.
    """
    word = Word(search_word)
    print(word)
