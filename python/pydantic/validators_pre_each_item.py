from typing import List
from pydantic import BaseModel, ValidationError, validator


class DemoModel(BaseModel):
    square_numbers: List[int] = []
    cube_numbers: List[int] = []

    # '*' is the same as 'cube_numbers', 'square_numbers' here:
    # "*" 를 이용하면 모든 맴버변수에 적용이 가능하다.
    # pre=True 를 이용하면 다른 validator 보다 먼저 호출된다.
    # 정확히는 field validation 이 발생하기 전에 호출된다. 이를 이용하면 유효성 검증 전에 적절한 값으로 변경이 가능하다.
    @validator('*', pre=True)
    def split_str(cls, v):
        if isinstance(v, str):
            return v.split('|')
        return v

    # 원하는 복수개의 맴버변수에 적용이 가능하다.
    @validator('cube_numbers', 'square_numbers')
    def check_sum(cls, v):
        if sum(v) > 42:
            raise ValueError('sum of numbers greater than 42')
        return v

    # 특정 맴버변수의 각 요소마다 적용이 가능하다. list, dict, set 등 집합구조에서 사용된다.
    @validator('square_numbers', each_item=True)
    def check_squares(cls, v):
        assert v ** 0.5 % 1 == 0, f'{v} is not a square number'
        return v

    @validator('cube_numbers', each_item=True)
    def check_cubes(cls, v):
        # 64 ** (1 / 3) == 3.9999999999999996 (!)
        # this is not a good way of checking cubes
        assert v ** (1 / 3) % 1 == 0, f'{v} is not a cubed number'
        return v


print(DemoModel(square_numbers=[1, 4, 9]))
#> square_numbers=[1, 4, 9] cube_numbers=[]
print(DemoModel(square_numbers='1|4|16'))
#> square_numbers=[1, 4, 16] cube_numbers=[]
print(DemoModel(square_numbers=[16], cube_numbers=[8, 27]))
#> square_numbers=[16] cube_numbers=[8, 27]
try:
    DemoModel(square_numbers=[1, 4, 2])
except ValidationError as e:
    print(e)
    """
    1 validation error for DemoModel
    square_numbers -> 2
      2 is not a square number (type=assertion_error)
    """

try:
    DemoModel(cube_numbers=[27, 27])
except ValidationError as e:
    print(e)
    """
    1 validation error for DemoModel
    cube_numbers
      sum of numbers greater than 42 (type=value_error)
    """
