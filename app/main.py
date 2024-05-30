from fastapi import FastAPI
from .routers import router

app = FastAPI()
app.include_router(router, prefix="/books", tags=["books"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
