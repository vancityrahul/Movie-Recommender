import pytest
from mock import patch
from numpy.ma.core import array
from backend.core.processor import Processor
from backend.tests.data.sample import data

@pytest.fixture
def mock_embeddings():
    with patch("backend.core.actor.Actor.parallel_processor") as mock:
        yield mock

@pytest.fixture
def mock_client_search():
    with patch("backend.core.qclient.Config.client.search") as mock:
        yield mock

@pytest.mark.asyncio
class Testprocessor:

    async def test_processor_exception(self, mock_embeddings) -> None:
        mock_embeddings.side_effect = Exception("Test exception")
        query = "Test_Query"
        genre = ["Test"]
        k = 3
        with pytest.raises(Exception) as exc_info:
            response = await Processor.process(query=query, genre=genre, k=k)
        assert str(exc_info.value) == "Test exception"

    async def test_processor_v2_exception(self) -> None:
        query = "Test_Query"
        k = 3
        with patch('backend.core.qclient.Config.client.search') as mock_search:
            mock_search.side_effect = Exception("Test exception")

            with pytest.raises(Exception) as exc_info:
                response = await Processor.process_v2(query=query, k=k)
            assert str(exc_info.value) == "Test exception"

    async def test_process(self, mock_embeddings, mock_client_search) -> None:
        mock_embeddings.return_value = embd = {
                "one_hot_embeddings": array([1,0,0,0,0,0]),
                "hf_embeddings": array([0,1,12,3,4,234,423,34])
            }
        # vectors = np.concatenate([embd["one_hot_embeddings"], embd["hf_embeddings"]])
        mock_client_search.return_value = data
        query = "Test_Query"
        genre = ["Test"]
        k = 3
        response  = await Processor.process(query = query,
                                            genre = genre,
                                            k = k)

        assert response == [
                              "Alatriste",
                              "America Is Still the Place",
                              "American Hero"
                            ]

    async def test_process_v2(self, mock_embeddings, mock_client_search) -> None:
        mock_embeddings.return_value = embd = {
                "one_hot_embeddings": array([1,0,0,0,0,0]),
                "hf_embeddings": array([0,1,12,3,4,234,423,34])
            }
        # vectors = np.concatenate([embd["one_hot_embeddings"], embd["hf_embeddings"]])
        mock_client_search.return_value = data
        query = "Test_Query"
        k = 3
        response  = await Processor.process_v2(query=query,
                                            k=k)

        assert response == [
                              "Alatriste",
                              "America Is Still the Place",
                              "American Hero"
                            ]