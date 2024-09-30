import chromadb
from chromadb.utils import embedding_functions

class VectorDB:
    def __init__(self) -> None:
        self.__EMBED_MODEL = "all-MiniLM-L6-v2"
        self.__COLLECTION_NAME = "Web_Data"

        try:
            self.__Client = chromadb.Client()
        except Exception as e:
            raise e
        
        embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=self.__EMBED_MODEL
        )

        try:
            self.__collection = self.__Client.create_collection(
                    name=self.__COLLECTION_NAME,
                    embedding_function=embedding_func,
                    metadata={"hnsw:space": "cosine"},
                )
        except:
            self.__collection = self.__Client.get_collection(
                name=self.__COLLECTION_NAME
            )
        
        self.index = 0

    def add(self, documents: list[str], metadatas: list[str] = None):

        self.__collection.add(
            documents=documents,
            metadatas=metadatas, 
            ids=[str(i) for i in range(self.index, self.index + len(documents))],
        )
    
    def query(self, keywords:list[str], limit:int = 2):
        
        result = self.__collection.query(
                    query_texts= keywords,
                    n_results= limit
                )
        
        return result

    def dropVectorData(self):
        try:
            self.__Client.delete_collection(self.__COLLECTION_NAME)
        except Exception as e:
            raise e