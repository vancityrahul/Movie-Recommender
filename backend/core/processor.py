from loguru import logger
from backend.core.qclient import Config
from backend.core.actor import Actor
from backend.core.utils import Utility
import numpy as np

Utility.load_env()
Config.load_client()
class Processor:
    @staticmethod
    async def process(query: str, genre: list, k=5) -> list:
        """
        :param k: No. of recommendation defaults to k.
        :param query: Query is writen by user about the type of movie they wish to watch
        :param genre: Favorable genre if any
        :return: A list of recommended movies
        """
        try:
            embeddings = await Actor.parallel_processor(query, genre)
            vectors = np.concatenate([embeddings["one_hot_embeddings"], embeddings["hf_embeddings"]])
            print("yes")
            hits =await Config.client.search(
                collection_name="movies_vectors",
                with_vectors=False,
                query_vector=vectors,
                limit=k
            )
            original_titles = [movie.payload['title']['original_title'] for movie in hits]
            logger.info("successFull!")
            return original_titles
        except Exception as e:
            logger.error(e)
            raise e

    @staticmethod
    async def process_v2(query: str, k=5) -> list:
        """
        :param k: No. of recommendation defaults to k.
        :param query: Query is writen by user about the type of movie they wish to watch
        :return: A list of recommended movies
        """
        try:
            embeddings = await Utility.get_embedding(query)
            hits = await Config.client.search(
                collection_name="movies_vectors_v2",
                with_vectors=False,
                query_vector=embeddings,
                limit=k
            )
            original_titles = [movie.payload['title']['original_title'] for movie in hits]
            logger.info("successFull!")
            return original_titles
        except Exception as e:
            logger.error(e)
            raise e