from fastapi import FastAPI
from routers.UserRouter import UserRouter
from routers.TestRouter import TestRouter

app = FastAPI()

app.include_router(UserRouter)
app.include_router(TestRouter)
