from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from .db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  
  __tablename__ = "users"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  email: Mapped[str] = mapped_column(String, unique=True)
  passwd: Mapped[str] = mapped_column(String)