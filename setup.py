from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'Search text on websites.'
LONG_DESCRIPTION = 'SearchURL allows you to search text on a webpage. It supports basic pattern matching, and fuzzy matching.'

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
    install_requires=['soupsieve>=2.6','beautifulsoup4>=4.12.3', 'requests', 'thefuzz>=0.22.1'],
    extras_require={
        "dev":["twine>=4.0.2"]
    },
    python_requires=">=3.10",
    keywords=['python', 'web-scraping', 'search', 'searchurl', 'SearchURL', 'Fuzzy matching', 'fuzzy search', 'web', 'scraping'],
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