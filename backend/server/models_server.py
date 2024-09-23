from fastapi import FastAPI, HTTPException
from backend.server.data_model import MovieRequest, MovieRequestv2
from backend.core.processor import Processor
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return "server is running"


@app.post("/v1/recommendation")
async def movie_recommend_v1(request: MovieRequest):
    try:
        response  = await Processor.process(
            request.query,
            request.genre,
            request.k
        )
        logger.info(response)
        return response
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/v2/recommendation")
async def movie_recommend_v2(request: MovieRequestv2):
    try:
        response  = await Processor.process_v2(
            request.query,
            request.k
        )
        logger.info(response)
        return response
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))