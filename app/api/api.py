from fastapi import APIRouter

from api.endpoints import user, board, note

api_router = APIRouter()

api_router.include_router(user.router, prefix='/user', tags=['user'])
api_router.include_router(board.router, prefix='/board', tags=['board'])
api_router.include_router(note.router, prefix='/note', tags=['note'])
