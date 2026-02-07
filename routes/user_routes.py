from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import get_db
from repositories.user_repo import userRepo
from schemas.user_schemas import user_schemas
router=APIRouter()

@router.post("/signup")
def signup(userRepo:Session=Depends(get_db)):
    userRepo=userRepo(db)
    userRepo.add_user(user)
    return {"message":"User created successfully"}
@router.post("/login")
def login():
    return {"message":"User logged in successfully"}