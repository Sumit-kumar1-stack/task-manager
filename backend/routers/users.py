from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import User
from schemas import UserCreate, Login
from auth import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(
            user.password
        )
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "User Registered"
    }


@router.post("/login")
def login(
    user: Login,
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    token = create_access_token(
        {"sub": db_user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }