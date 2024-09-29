import requests
from bs4 import BeautifulSoup
from thefuzz import process, fuzz

class SearchURL:

    def __init__(self, cache:bool=True) -> None:
        '''
        Args:
            cache: If True, caches the webpage content for faster subsequent searches.
        '''
        self.searched = {}
        self.cache = cache

    def __getAllData(self, url:str) -> list[str]:
        
        if self.cache:
                data = self.searched.get(url)
                if data: return data
        
        try:
            response = requests.get(url)

            soup = BeautifulSoup(response.content, "html.parser")

            data = [text.strip('/ \\') for text in soup.get_text(' ').split('\n') if text and text != ' ']
            
            if self.cache: self.searched[url] = data

            return data

        except Exception as e:
            raise e
        
    def __includes(self, string:str, keywords:list[str]) -> bool:

        string = string.lower()

        for word in keywords:
            if word.lower() in string:
                return True
        return False
    
    def searchUrl(self, url: str, keywords: list[str] = []) -> dict:

        """Searches for keywords within the text content of a given URL.

        Args:
            url: The URL of the webpage to search.
            keywords: A list of keywords to search for.

        Returns:
        **A dictionary with the following structure:**
                - **success:** A boolean indicating whether the search was successful.
                - **data:** If successful, a paragraph composed of all sentences from the webpage that contain at least one of the specified keywords, concatenated together.
                - **detail:** If unsuccessful, a string describing the error that occurred.
        """

        try:
            data = self.__getAllData(url)
        except Exception as e:
            return {'success': False, 'detail': e.__str__()}

        if not keywords:
            return {'success': True, 'data':" ".join(data)}

        return {'success': True, 'data':" ".join([match for match in data if self.__includes(match, keywords)])}

    def searchUrlFuzz(self, url: str, keywords: list[str] = [], limit:int=10, filter:int=80) -> dict:
        
        """Searches for keywords within the text content of a webpage given its URL using fuzzy matching.

        Args:
            url: The URL of the webpage to search.
            keywords: A list of keywords to search for.
            limit: The maximum number of matches to return for each keyword.
            filter: The minimum acceptable score or rating a match must achieve to be considered a good fit. A higher filter value sets a stricter standard, requiring matches to have a higher score or rating to be accepted. **tip:** Higher filter values tend to give more relevent results.

        Returns:
        A dictionary with the following structure:
                - **success:** A boolean indicating whether the search was successful.
                - **data:** If successful, a paragraph composed of all sentences from the webpage that contain at least one of the specified keywords, concatenated together.
                - **detail:** If unsuccessful, a string describing the error that occurred.
        """
        try:
            data = self.__getAllData(url)
        except Exception as e:
            return {'success': False, 'detail': e.__str__()}

        if not keywords:
            return {'success': True, 'data':" ".join(data)}

        matched_data = [' | '.join([match[0] for match in process.extract(keyword, data, limit=limit, scorer= fuzz.token_set_ratio) if match[1]>=filter]) for keyword in keywords]

        return {'success': True, 'data':" | ".join([match for match in matched_data if match])}
