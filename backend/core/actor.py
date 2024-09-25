from pykka import ThreadingActor
import asyncio
from backend.core.utils import Utility
from loguru import logger

class ResultHandler(ThreadingActor):
    async def on_receive(self, message):
        logger.info("Received result:", message)


class Actor:
    @staticmethod
    async def parallel_processor(query: str, genre: list) -> dict:
        """
        :param query: Query for the recommendation model
        :param genre: Genre if needed.
        :return: Dictionary of one_hot_vectors and Hf_embeddings
        """
        if not query:
            raise ValueError("Empty text input is not allowed")
        result_handler = ResultHandler.start()
        try:
            results = await asyncio.gather(
                Utility.one_hot_encode_genre(genre),
                Utility.get_embedding(query)
            )
            embd = {
                "one_hot_embeddings": results[0],
                "hf_embeddings": results[1]
            }
            for result in results:
                result_handler.tell(result)
            return embd
        except Exception as e:
            logger.error(e)
        finally:
            result_handler.stop()
        return None
