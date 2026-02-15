import os

class Settings:
    SECRET_KEY :str = os.getenv("SECRET_KEY","dev-only-unsafe-key")
    ALGORITHM :str = os.getenv("JWT_ALGORITHM","HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES:int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES","30"))

settings= Settings()
