from smart_config import ConfigLoader
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from FlagEmbedding import BGEM3FlagModel
from fastapi.encoders import jsonable_encoder

class Utility:
    env = None
    @staticmethod
    def load_env() -> None:
        """
        :return: None
        Loads Environment variables from system.yaml
        """
        Utility.env = ConfigLoader('backend/system.yaml').get_config()

    @staticmethod
    async def one_hot_encode_genre(text: list) -> np.array:
        """
        One-hot encodes genres for a list of movies.

        Args:
            text : genres for movies.

        Returns:
            np.array: One-hot encoded genres.
        """
        if text:
            all_genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                          'Fantasy', 'Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction',
                          'TV Movie', 'Thriller', 'War', 'Western']
            genre_binarizer = MultiLabelBinarizer(classes=all_genres)
            genre_binarizer.fit([all_genres])
            genre_vector= genre_binarizer.transform([text])[0]
        else:
            genre_vector= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        genre_vector = np.array(genre_vector)
        return genre_vector

    model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)
    @staticmethod
    async def get_embedding(text: str):
        """
        :param text: Takes the query as input
        :return: Embeddings for the query
        """
        embd = Utility.model.encode(text, return_dense=True, return_sparse=True, return_colbert_vecs=True)
        return embd["dense_vecs"]

    @staticmethod
    def prepare_response(data: dict) -> dict:
        return jsonable_encoder(data)