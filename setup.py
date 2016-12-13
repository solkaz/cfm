from distutils.core import setup
setup(
    name = 'cfm',
    packages = ['cfm'], # this must be the same as the name above
    version = '0.1',
    description = 'A config file manager',
    author = 'Jeff Held',
    author_email = 'jheld135@gmail.com',
    url = 'https://github.com/solkaz/cfm',
    download_url = 'https://github.com/solkaz/cfm/tarball/0.1',
    keywords = [], 
    classifiers = [],
    entry_points={
        'console_scripts': [
            'cfm = cfm.main:main',
        ]
    }
)
