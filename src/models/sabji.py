from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .db import db

class Sabji(db.Model):
  
  __tablename__ = "sabjis"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String)
  qty: Mapped[str] = mapped_column(String)
  
  user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))