from pydantic import BaseModel
class user_schemas(BaseModel):
    username:str
    password:str