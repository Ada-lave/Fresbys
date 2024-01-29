from fastapi import FastAPI
import uvicorn
from api_v1 import router as api_v1
from core.config.conf import settings

app = FastAPI()
app.include_router(api_v1, prefix=settings.api_v1)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)