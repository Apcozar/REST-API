from fastapi import APIRouter

from . import auth_router, friendships_router, users_router

api_router = APIRouter()
api_router.include_router(users_router.router)
api_router.include_router(friendships_router.router)
api_router.include_router(auth_router.router)