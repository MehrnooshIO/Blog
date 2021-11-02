from fastapi import APIRouter


def blog_router() -> APIRouter:
    router = APIRouter(prefix="/blog")

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
