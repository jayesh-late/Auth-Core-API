from pydantic import BaseModel ,EmailStr

class CreateLogin(BaseModel):
    email : EmailStr
    password : str

class CreateSignup(BaseModel):
    email: EmailStr
    password: str