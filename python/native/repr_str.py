class MyClass:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

class MyClass2(MyClass):
    def __repr__(self) -> str:
        return super().__repr__() + f"__repr__(name: {self.name}, email: {self.email})"
    
    def __str__(self) -> str:
        return super().__str__() + f"__str__()"

if __name__ == "__main__":
    instance = MyClass("wooseok", "smilehoho@gmail.com")
    print(instance) # <__main__.MyClass object at 0x1031564f0>

    instance2 = MyClass2("wooseok", "smilehoho@gmail.com")
    print(repr(instance2)) # <__main__.MyClass2 object at 0x1104dddc0>__repr__(name: wooseok, email: smilehoho@gmail.com)
    print(instance2) # <__main__.MyClass2 object at 0x1104dddc0>__repr__(name: wooseok, email: smilehoho@gmail.com)__str__()
    print(str(instance2)) # <__main__.MyClass2 object at 0x1104dddc0>__repr__(name: wooseok, email: smilehoho@gmail.com)__str__()

"""
결론:
1. 그냥 인스턴스를 출력할때는 __str__() 이 호출된다.
2. __str__() 은 내부적으로 __repr__() 을 먼저 호출한다.
3. str() 은 __str__() 을 호출한다.
4. repr() 은 __repr__() 을 호출한다.

목적:
__str__ : 객체를 문자열화
__repr__ : 객체를 표현
"""
    