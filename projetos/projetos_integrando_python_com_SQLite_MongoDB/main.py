import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DECIMAL
from sqlalchemy import ForeignKey
from sqlalchemy import select


Base = declarative_base()

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    cpf = Column(String(9))
    address = Column(String(50))


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    type = Column(String(30))
    agency = Column(String(10))
    number_account = Column(Integer)
    id_client = Column(Integer, ForeignKey("client.id"), nullable=False)
    balance = Column(DECIMAL)
