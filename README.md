
## Installation

Install SearchURL with pip

```bash
  pip install SearchURL
```
    
## Documentation

**1. Getting all the text from a webpage by not passing in keywords:**
```python
from SearchURL.main import SearchURL

search = SearchURL(cache=True)

data = search.searchUrl(
    url="https://en.wikipedia.org/wiki/Web_scraping"
    )

print(data)
```
**output:** {'success': True, 'data': 'Web scraping - Wikipedia ...'}

**2. Searching with keywords:**

```python
from SearchURL.main import SearchURL

search = SearchURL(cache=True)

data = search.searchUrl(
    url="https://en.wikipedia.org/wiki/Web_scraping",
    keywords=['legal'])

print(data)
```
**output:** {'success': True, 'data': 'Legal issues Toggle Legal issues subsection Legal issues [ edit ] The legality of web scraping varies across the world ...'}

**4. Fuzzy Searching:**

```python
from SearchURL.main import SearchURL

search = SearchURL(cache=True)

data = search.searchUrlFuzz(
    url="https://en.wikipedia.org/wiki/Web_scraping",
    keywords=['legal'])


print(data)
```
**output:** {'success': True, 'data': 'Legal issues [ edit ] | In the United States, website owners can use three major  legal claims  to prevent undesired web scraping: (1) copyright ...'}

**3. Errors:** If this package runs into some error while fetching and searching, it will return an object like this: 
{'success': False, 'detail': 'The error that occurred'}
***
***

####
The URL used in this readme is a link to an article on [wikipedia.org](https://wikipedia.org) on the topic of [Web_scraping](https://en.wikipedia.org/wiki/Web_scraping).