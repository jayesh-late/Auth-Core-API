from app.db.session import SessionLocal
from app.utils.hashing import hash_password
from app.db.model.user import User

db = SessionLocal()

user = User(
    email= "jaylate514@gmail.com",
    hashed_password= hash_password("123456")
)

db.add(user)
db.commit()
db.refresh(user)

print("Test user created")