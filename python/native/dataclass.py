# from dataclasses import dataclass
from pydantic.dataclasses import dataclass
from enum import Enum, unique

"""
ref: https://jackmckew.dev/dataclasses-vs-attrs-vs-pydantic.html
dataclasses.dataclass: 값보다는 데이터의 분류가 중요한 경우
pydantic.dataclasses.dataclass: 값의 유효성이 중요한 경우
attrs: 다 중요한 경우
"""

class MyEnum(str, Enum):
    A = "AAA"
    B = "BBB"
    C = "CCC"


@dataclass(frozen=True)
class MyDataClass:
    data: MyEnum


if __name__ == "__main__":
    """
    - pydantic.dataclasses 를 사용했기 때문에 value 를 신뢰할 수 있다.
    - fronzen=True 옵션으로 인해 인스턴스 생성이후 수정이 불가능하다.
    """
    a: MyDataClass = MyDataClass(data=MyEnum.A)
    # b = MyDataClass(data="ABC") # pydantic.error_wrappers.ValidationError
    
    print(a)

    # a.data = None # dataclasses.FrozenInstanceError: cannot assign to field 'data'
