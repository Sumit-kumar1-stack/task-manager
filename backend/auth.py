from jose import jwt
from passlib.context import CryptContext

SECRET_KEY="secret123"
ALGORITHM="HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(
    plain_password,
    hashed_password
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def create_access_token(data):
    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )