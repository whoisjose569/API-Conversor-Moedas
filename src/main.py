from fastapi import FastAPI
from src.routers.routers import router

app = FastAPI()
app.include_router(router=router)


@app.get('/hello-world')
def hello_world():
    return "Hello World!"