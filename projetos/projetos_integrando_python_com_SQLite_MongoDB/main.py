import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
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

    # Create representation
    def __repr__(self):
        return f"ID Client: {self.id} | Client: {self.name} | CPF: {self.cpf} | Address: {self.address}"


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

    # Create representation
    def __repr__(self):
        return (f"ID Account: {self.id} | Type: {self.type} | Agency: {self.agency} | Account: {self.number_account} | "
                f"Balance: {self.balance:.2f}")


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
            type="Current account",
            agency="00216505",
            number_account=886312,
            balance=567.98
        )]
    )

    client_2 = Client(
        name="Gabriel Teixeira Fagundes",
        cpf="064874650",
        address="Paraná",
        account=[Account(
            type="Savings account",
            agency="00216514",
            number_account=887801,
            balance=5650.0
        )]
    )

    client_3 = Client(
        name="Camila da Silva",
        cpf="874320654",
        address="Paraná",
        account=[Account(
            type="Current account",
            agency="00214479",
            number_account=883320,
            balance=1487.82
        )]
    )
    # Sending to db
    session.add_all([client_1, client_2, client_3])
    session.commit()


def view_clients():
    stmt_all_client = select(Client)
    for client in session.scalars(stmt_all_client):
        print(client)


def view_accounts():
    stmt_all_accounts = select(Account)
    for account in session.scalars(stmt_all_accounts):
        print(account)


def search_client_by_id(id):
    stmt_search_clients = select(Client).where(Client.id == id)
    client = session.scalars(stmt_search_clients).first()
    return client


def search_account_by_id(id):
    stmt_search_account = select(Account).where(Account.id == id)
    account = session.scalars(stmt_search_account).first()
    return account


def user_balance(id):
    stmt_client_balance = (select(Client.name, Client.cpf, Account.type, Account.balance).where(Client.id == id).
                           join_from(Client, Account))
    client = session.scalars(stmt_client_balance).first()
    return client
    




