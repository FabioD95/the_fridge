from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import uvicorn
from configs.config import API_ENDPOINT_HOST, API_ENDPOINT_PORT, API_V1_STR, PROJECT_NAME

from database.engine import get_engine, get_session, create_table

from api.api import api_router


app = FastAPI(
    title=PROJECT_NAME,
    openapi_url=f'{API_V1_STR}//openapi.json'
)


app.include_router(api_router, prefix=API_V1_STR)


@app.on_event("startup")
def on_startup():
    create_table()


if __name__ == '__main__':
    uvicorn.run('main:app', port=API_ENDPOINT_PORT, host=API_ENDPOINT_HOST, reload=True)