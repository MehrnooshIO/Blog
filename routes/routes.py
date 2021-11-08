from fastapi import APIRouter

def create_blog_router():
    router = APIRouter(
        prefix="/blog",
        tags=["blog"],
    )

    @router.get("/")
    def get_blogs():
        return {"message": "All posts"}

    @router.get("/{blog_id}")
    def get_blog(blog_id: int):
        return {"message": f"Blog {blog_id}"}

    @router.post("/")
    def create_blog():
        return {"message": "Create a new blog"}

    @router.put("/{blog_id}")
    def update_blog(blog_id: int):
        return {"message": f"Update blog {blog_id}"}

    @router.delete("/{blog_id}")
    def delete_blog(blog_id: int):
        return {"message": f"Delete blog {blog_id}"}

    @router.get("/{tag}")
    def get_blog_by_tag(tag: str):
        return {"message": f"Get blogs by tag {tag}"}

    return router