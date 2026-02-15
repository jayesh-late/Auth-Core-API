from app.db.session import engine
from app.db.model.user import User
from app.db.base import Base

Base.metadata.create_all(bind=engine)