from pydantic import BaseModel
from typing import Union


class UserModel(BaseModel):
    snils: Union[str, None] = None # can be null if it is a put request
    login: str
    email: str
    hash_password: str
    name: str
    surname: str
    patronymic: Union[str, None] = None
    role_id: int
