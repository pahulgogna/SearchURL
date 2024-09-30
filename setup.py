from setuptools import setup, find_packages

VERSION = '1.1.0'
DESCRIPTION = 'Search text on websites.'
with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="SearchURL",
    version=VERSION,
    author="Pahul Gogna",
    author_email="pahulgogna@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(where='.'),
    license='MIT',
    install_requires=['soupsieve>=2.6','beautifulsoup4>=4.12.3', 'requests', 'thefuzz>=0.22.1',
                      'chromadb>=0.5.11', 'sentence-transformers>=3.1.1'],
    extras_require={
        "dev":["twine>=4.0.2"]
    },
    python_requires=">=3.10",
    keywords=['python', 'web-scraping', 'search', 'searchurl', 'SearchURL', 'Fuzzy matching', 'fuzzy search', 'web', 'scraping', 'semantic search', 'nlp', 'natural language processing'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing"
    ]
)