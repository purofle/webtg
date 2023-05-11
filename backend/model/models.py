from sqlalchemy import Integer
from sqlalchemy.testing.schema import Column

from backend.database import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
