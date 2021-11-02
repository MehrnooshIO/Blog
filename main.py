from fastapi import FastAPI
import uvicorn
from routes.routes import blog_router


blog = FastAPI(
    debug=True,
    title="Blog",
    version="0.1.0",
)
my_blog = blog_router()
blog.include_router(my_blog)


if __name__ == "__main__":
    uvicorn.run(app=blog)
