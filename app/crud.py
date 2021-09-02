from models import UserModel
from sqlalchemy.orm import Session


# CRUD
from sqlalchemy.orm import Session
def get_user_by_email(db: Session, email: str):
    return db.session.query(UserModel).filter(UserModel.email == email).first()

def get_user_by_phone(db: Session, phone: str):
    return db.session.query(UserModel).filter(UserModel.phone == phone).first()