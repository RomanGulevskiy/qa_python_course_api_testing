from pydantic import BaseModel


class JSONPlaceholderBaseModel(BaseModel):
    id: int


class JSONPlaceholderPostsModel(JSONPlaceholderBaseModel):
    userId: int
    title: str
    body: str


class JSONPlaceholderTodosModel(JSONPlaceholderBaseModel):
    userId: int
    title: str
    completed: bool


class JSONPlaceholderPhotosModel(JSONPlaceholderBaseModel):
    albumId: int
    title: str
    url: str
    thumbnailUrl: str


class JSONPlaceholderCommentsModel(JSONPlaceholderBaseModel):
    postId: int
    name: str
    email: str
    body: str
