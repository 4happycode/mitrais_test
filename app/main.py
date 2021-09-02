from typing import Optional

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from pathlib import Path

from database import Base, SessionLocal, engine, SQLALCHEMY_DATABASE_URL
import models
import schemas
import crud
from sqlalchemy.orm import Session
from fastapi_sqlalchemy import DBSessionMiddleware

models.Base.metadata.create_all(bind=engine)
#templates = Jinja2Templates(directory="templates/")
BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=SQLALCHEMY_DATABASE_URL)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/registration", status_code=200)
def root(request: Request) -> dict:
    return templates.TemplateResponse(
        "reg.html",
        {"request": request},
    )

@app.post("/regist")
def regist_post(user: schemas.User, db: Session = Depends(get_db)):
    from fastapi_sqlalchemy import db
    # Check already email
    if crud.get_user_by_email(db, email=user.email):
        raise HTTPException(status_code=200, detail="Email already registered")
    # Check already phone
    if crud.get_user_by_phone(db, phone=user.phone):
        raise HTTPException(status_code=200, detail="Mobile phone already registered")

    # Save to DB use model
    db_user = models.UserModel(**user.dict())
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)

    return {"data":user, "detail":"saved"}

@app.post("/login")
def login_post(request:Request):

    return {"data":'user'}


@app.get("/viewLogin", status_code=200)
def login_post(request:Request) -> dict:

    return templates.TemplateResponse(
        "login.html",
        {"request": request},
    )


@app.get("/check_email", status_code=200)
def login_post(request:Request, q: Optional[str] = None) -> dict:
    from fastapi_sqlalchemy import db
    if crud.get_user_by_email(db, email=q):
        raise HTTPException(status_code=200, detail=q)

    return {"detail": True, 'data': q}

@app.get("/check_phone", status_code=200)
def login_post(request:Request, q: Optional[str] = None) -> dict:
    from fastapi_sqlalchemy import db
    if crud.get_user_by_phone(db, phone=q):
        # raise HTTPException(status_code=200, detail="Phone already taken")
        raise HTTPException(status_code=200, detail=q)

    return {"detail": True, 'data': q}