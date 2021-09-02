from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, validator
from datetime import datetime, date


# def form_body(cls):
#     # if use form body in request
#     cls.__signature__ = cls.__signature__.replace(
#         # parameters=[
#         #     arg.replace(default=Form(...))
#         #     for arg in cls.__signature__.parameters.values()
#         # ]
#         parameters=[
#             v.replace(default=Form(...)) if str(k) not in ['gender', 'datebirth', 'id'] else v.replace(default=Form(None))
#             for k,v in cls.__signature__.parameters.items()
#         ]
#     )
#     return cls

class GenderChoice(str, Enum):
    FEMALE = 'female'
    MALE = 'male'


# @form_body
class User(BaseModel):
    id: Optional[int] = None
    email: str
    phone: str
    firstname: str
    lastname: str
    gender: GenderChoice=None
    datebirth: Optional[str] = None

    @validator('datebirth')
    def none_value(cls, v):
        print(v)
        if v and str(v) != '--':
            return v
        else:
            return None

    class Config:
        orm_mode = True

# @form_body
class UserLogin(BaseModel):
    email: str
    password: str

    # class Config:
    #     orm_mode = True