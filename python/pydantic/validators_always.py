from datetime import datetime

from pydantic import BaseModel, validator

"""
성능상의 이유로 값이 제공되지 않으면 기본적으로 필드에 대해 유효성 검사기가 호출되지 않습니다.
그러나 항상 유효성 검사기를 호출하는 것이 유용하거나 필요할 수 있는 상황이 있습니다.
동적 기본값을 설정합니다.
"""
class DemoModel(BaseModel):
    ts: datetime = None

    @validator('ts', pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.now()

# ts를 지정해주지 않아서 
print(DemoModel())
#> ts=datetime.datetime(2021, 12, 31, 15, 4, 57, 629206)
print(DemoModel(ts='2017-11-08T14:00'))
#> ts=datetime.datetime(2017, 11, 8, 14, 0)
