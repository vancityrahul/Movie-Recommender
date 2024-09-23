from qdrant_client import AsyncQdrantClient
from backend.core.utils import Utility

class Config:
    client = None
    @staticmethod
    def load_client() -> None:
        Config.client = AsyncQdrantClient(
            url=Utility.env["qdrant"]["url"],
            api_key=Utility.env["qdrant"]["api_key"]
        )