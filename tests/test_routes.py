from fastapi.testclient import TestClient
from main import blog

client = TestClient(blog)


def test_blog_main():
    response = client.get("/blog/")
    assert response.status_code == 200
    assert response.json() == {"list": ["list of posts"]}
    print("OK")
