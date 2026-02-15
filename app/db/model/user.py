from app.db.base import Base
from sqlalchemy import Integer,String,Column

class User(Base):
    __tablename__ = "users"

    id= Column(Integer,primary_key=True,index=True)
    email= Column(String,nullable=False,unique=True)
    hashed_password= Column(String,nullable=False)
