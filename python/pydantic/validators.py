from pydantic import BaseModel, ValidationError, validator

"""
@validator 를 이용하면 좀 더 복잡한 유효성 검증을 할 수 있다.
- 유효성 검증에 실패하면 raise 해주면 된다. assert 를 사용하기도 한다.
- @validator 는 classmethod 이다. 따라서 첫번째 인자는 class 이다.
- 두번째 인자는 해당값이다.
- values, config, field, **kwargs 정해진 인자를 사용할 수도 있다.
- return 으로 값을 변형하는 것도 가능하다.
"""

class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    @validator('name')
    def name_must_contain_space(cls, v, values):
        print("arg2", type(values), values)
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v


user = UserModel(
    name='samuel colvin',
    username='scolvin',
    password1='zxcvbn',
    password2='zxcvbn',
)
print(user)
#> name='Samuel Colvin' username='scolvin' password1='zxcvbn' password2='zxcvbn'

try:
    UserModel(
        name='samuel',
        username='scolvin',
        password1='zxcvbn',
        password2='zxcvbn2',
    )
except ValidationError as e:
    print(e)
    """
    2 validation errors for UserModel
    name
      must contain a space (type=value_error)
    password2
      passwords do not match (type=value_error)
    """
