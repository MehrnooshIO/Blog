from fastapi import FastAPI
import uvicorn


blog = FastAPI(
    debug=True,
    title="Blog",
    version="0.1.0",
)


if __name__ == "__main__":
    uvicorn.run(app=blog)
