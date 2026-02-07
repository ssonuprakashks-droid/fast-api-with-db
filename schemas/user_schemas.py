from pydantic import BaseModel
class user_schemas(BaseModel):
    email:str
    password:str