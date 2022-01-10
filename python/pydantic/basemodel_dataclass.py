from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from pydantic.error_wrappers import ValidationError

"""
BaseModel vs dataclass
어떤 차이가 있을까?
"""

class MyModel(BaseModel):
    name: str
    age: int


@dataclass
class MyModel2:
    name: str
    age: int

try:
    choiws = MyModel(name="wooseok")
    print(choiws, type(choiws))
except ValidationError as e:
    print(e)
"""
1 validation error for MyModel
age
  field required (type=value_error.missing)
"""

print("=" * 80)

try:
    choiws2 = MyModel2(name="name")
    print(choiws2)
except TypeError as e:
    print(e)
"""
Traceback (most recent call last):
  File "/Users/brandi/smilehoho/TIL/python/pydantic/test.py", line 24, in <module>
    choiws2 = MyModel2(name="name")
TypeError: __init__() missing 1 required positional argument: 'age'
"""


"""
아직은 모르겠다.
그냥 BaseModel 이 더 강력하지 않을까??
ref. https://github.com/samuelcolvin/pydantic/issues/710
"""

print("=" * 80)

class Y(object):
    def __init__(self,mutable=[],data=None):
        self._mutable = mutable
        self.data = data

y1 = Y(data="x")              # y1._mutable = []
y2 = Y(data="y")              # y2._mutable = []
y1._mutable.append(1) # y1._mutable = [1], but surprise! y2._mutable = [1]
print(y1._mutable, y1.data)
print(y2._mutable, y2.data)

print("=" * 80)

@dataclass
class User:
    id: int
    name: str = "David"

u1 = User(id=1)
u2 = User(id=2)

print(u1, u2)

User.name = "James"

print(u1, u2)
