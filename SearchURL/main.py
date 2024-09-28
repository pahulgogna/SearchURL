import requests
from bs4 import BeautifulSoup

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
