from typing import Generic, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class MyUser(BaseModel):
    name: str
    age: int

"""
generic을 사용하려면 GenericModel과 Generic을 상속해야한다.
"""
class Response(GenericModel, Generic[T]):
    total: int
    items: list[T]


my_users = [MyUser(name="User1", age=10), MyUser(name="User2", age=20)]

print(my_users)

resp = Response[MyUser](total=len(my_users), items=my_users)

print(resp)
print(resp.__annotations__)