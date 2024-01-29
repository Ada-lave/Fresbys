from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    first_name: str
    last_name:str
    group_id: int

class CreateUser(UserBase):
    pass

class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)