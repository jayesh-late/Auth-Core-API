from fastapi import APIRouter,Depends,HTTPException,status

from app.schemas.user import CreateLogin, CreateSignup
from app.services.auth_service import user_login,user_signup
from sqlalchemy.orm import Session
from typing import Annotated
from app.db.session import get_db

router = APIRouter(prefix='/auth',tags=['Auth'])

db_dependency = Annotated[Session,Depends(get_db)]

@router.post('/login')
async def login(db:db_dependency, data:CreateLogin):
    token = user_login(
        db=db,
        email=str(data.email),
        password=data.password
    )

    if not token :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Credentials'
        )

    return {"access_token":token,
            "token_type":"bearer"
            }

@router.post('/signup')
async def signup(db:db_dependency,data:CreateSignup):

    result = user_signup(
        db=db,
        email=str(data.email),
        password=data.password
    )

    if result == "weak_password":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="password does not meet minimum requirements"
        )

    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email Already Registered '
        )

    return  {"message":"User Created Successfully"}