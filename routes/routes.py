from fastapi import APIRouter
from opentelemetry import trace

def blog_router() -> APIRouter:
    router = APIRouter(prefix="/blog")

    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("http-handler"):
        with tracer.start_as_current_span("all_posts"):
            @router.get("/")
            def all_posts():
                """
                :return: json format of all posts
                """
                return {"list": ["list of posts"]}

    @router.post("/")
    def create_post():
        pass

    @router.put("/")
    def edit_post():
        pass

    @router.delete("/")
    def delete_post():
        pass

    return router
