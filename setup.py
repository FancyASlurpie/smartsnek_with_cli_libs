from setuptools import setup, find_packages

setup(
    name='cli_example',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'beautifulsoup4==4.8.2',
        'bs4==0.0.1',
        'certifi==2019.11.28',
        'chardet==3.0.4',
        'click==7.1.1',
        'docopt==0.6.2',
        'idna==2.9',
        'soupsieve==2.0',
        'urllib3==1.25.8',
    ],
    entry_points='''
        [console_scripts]
        click_smartsnek=click_example:search_for_word
        docopt_smartsnek=docopt_example:main
        argparse_smartsnek=argparse_example:main
    ''',
)
