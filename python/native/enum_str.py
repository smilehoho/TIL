from enum import Enum, unique

class MyEnum(Enum):
    """
    기본적으로 name 중복을 허용하지 않는다.
    """
    A = "AAA"
    B = "BBB"
    C = "CCC"
    # C = "D" # TypeError: Attempted to reuse key: 'C'


@unique
class MyUniqueEnum(Enum):
    """
    @unique
    value 중복을 허용하지 않는다.
    """
    A = "AAA"
    # B = "AAA" # ValueError: duplicate values found in <enum 'MyUniqueEnum'>: B -> A
    

class MyStrEnum(str, Enum):
    """
    str, Enum 을 mixin 형태로 상속하면 각 항목은 문자열과 == 연산자를 사용할 수 있다.
    """
    A = "AAA"
    B = "BBB"
    C = "CCC"

    def __str__(self) -> str:
        return self.value


if __name__ == "__main__":
    print(MyEnum.A) # MyEnum.A
    print(MyEnum.A.name) # A
    print(MyEnum.A.value) # AAA

    print(MyEnum.A == "AAA") # False
    print(MyStrEnum.A == "AAA") # True
    print(isinstance(MyStrEnum.A, str)) # True

    print(type(MyStrEnum.A)) # <enum 'MyStrEnum'>
    print(MyStrEnum.A) # AAA __str__ 을 override 했기 때문
