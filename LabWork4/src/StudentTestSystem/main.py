from fastapi import FastAPI
from routers.UserRouter import UserRouter

app = FastAPI()

app.include_router(UserRouter)
