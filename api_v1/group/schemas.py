from pydantic import BaseModel, ConfigDict


class BaseGroup(BaseModel):
    name: str
    

class CreateGroup(BaseGroup):
    pass
    
class Group(BaseGroup):
    id: int
    model_config = ConfigDict(from_attributes=True)
    