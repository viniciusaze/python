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
    # Create Table and attributes of Client
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    cpf = Column(String(11))
    address = Column(String(50))

    # Create relationship
    account = relationship("Account", back_populates="client")


class Account(Base):
    # Create Table and attributes of Account
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    type = Column(String(30))
    agency = Column(String(8))
    number_account = Column(Integer)
    id_client = Column(Integer, ForeignKey("client.id"), nullable=False)
    balance = Column(DECIMAL)

    # Create relationship
    client = relationship("Client", back_populates="account")


# Connecting with database
engine = create_engine("sqlite://")

# Create tables with class
Base.metadata.create_all(engine)

with Session(engine) as session:
    client_1 = Client(
        name="Vinícius Azevedo Rosso",
        cpf="03643545002",
        address="Rio Grande do Sul",
        account=[Account(
            type="Conta corrente",
            agency="00216505",
            number_account=886312,
            balance=567.98
        )]
    )

    client_2 = Client(
        name="Gabriel Teixeira Fagundes",
        cpf="064874650",
        address="Paraná"
    )

    client_3 = Client(
        name="Camila da Silva",
        cpf="874320654",
        address="Paraná"
    )

