import pytest

from assertions.assertion_base import assert_schema

from models.jsonplaceholder_model import JSONPlaceholderPostsModel
from models.jsonplaceholder_model import JSONPlaceholderTodosModel
from models.jsonplaceholder_model import JSONPlaceholderPhotosModel
from models.jsonplaceholder_model import JSONPlaceholderCommentsModel


@pytest.mark.parametrize(["post_id", "status_code"],
                         [(1, 200),
                          (10, 200),
                          (50, 200)])
def test_get_post_by_id(jsonplaceholder_client, post_id, status_code):
    response = jsonplaceholder_client.get_post_by_id(post_id)
    assert response.status_code == status_code
    assert_schema(response, JSONPlaceholderPostsModel)


@pytest.mark.parametrize(["user_id", "status_code"],
                         [(1, 200),
                          (2, 200),
                          (3, 200)])
def test_get_posts_by_user(jsonplaceholder_client, user_id, status_code):
    response = jsonplaceholder_client.get_posts_by_user(user_id)
    assert response.status_code == status_code
    assert_schema(response, JSONPlaceholderPostsModel)


@pytest.mark.parametrize(["todo_id", "status_code"],
                         [(1, 200),
                          (10, 200),
                          (50, 200)])
def test_get_todo_by_id(jsonplaceholder_client, todo_id, status_code):
    response = jsonplaceholder_client.get_todo_by_id(todo_id)
    assert response.status_code == status_code
    assert_schema(response, JSONPlaceholderTodosModel)


@pytest.mark.parametrize(["photo_id", "status_code"],
                         [(1, 200),
                          (500, 200),
                          (2000, 200)])
def test_get_photo_by_id(jsonplaceholder_client, photo_id, status_code):
    response = jsonplaceholder_client.get_photo_by_id(photo_id)
    assert response.status_code == status_code
    assert_schema(response, JSONPlaceholderPhotosModel)


@pytest.mark.parametrize(["post_id", "status_code"],
                         [(1, 200),
                          (10, 200),
                          (50, 200)])
def test_get_comments_by_post(jsonplaceholder_client, post_id, status_code):
    response = jsonplaceholder_client.get_comments_by_post(post_id)
    assert response.status_code == 200
    assert_schema(response, JSONPlaceholderCommentsModel)
