from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'Search text on websites.'
LONG_DESCRIPTION = 'This package allows you to search text on a webpage.'

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
    keywords=['python', 'web-scraping', 'search'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)