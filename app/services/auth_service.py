from app.repositories.user_repo import get_login_by_email , create_user
from app.utils.hashing import hash_password,verify_password
from sqlalchemy.orm import Session
from app.core.security import create_access_token

def user_login(db:Session,email:str,password:str):
    user = get_login_by_email(
        db=db,
        email=email
    )

    if not user :
        return None

    if not verify_password(password,user.hashed_password):
        return None

    token = create_access_token(
        data={'sub':str(user.id)}
    )

    return token


def _validate_password_policy(password:str)->bool:
    return len(password) >= 8


def user_signup(db:Session,email:str,password:str):

    if not _validate_password_policy(password):
        return "weak_password"

    existing_user = get_login_by_email(
        db=db,
        email=email
    )

    if existing_user :
        return None

    hashed = hash_password(password)

    user = create_user(
        db=db,
        email=email,
        hashed_password=hashed
    )
    return user