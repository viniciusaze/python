import os
from time import sleep
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


def main():
    choice = int(input("""---- BANK ----
    Select your choice
    [1] - View all clients
    [2] - View all accounts
    [3] - Search a client
    [4] - Search a account
    [5] - View Client balance
    [6] - Total of clients
    [0] - End
    
    ~~~>"""))
    user_choice(choice)


def user_choice(choice):
    try:
        if choice == 1:
            view_clients()
        elif choice == 2:
            view_accounts()
        elif choice == 3:
            identifier = int(input("Client ID: "))
            search_client_by_id(identifier)
        elif choice == 4:
            identifier = int(input("Account ID: "))
            search_account_by_id(identifier)
        elif choice == 5:
            identifier = int(input("Client ID: "))
            client_balance(identifier)
        elif choice == 6:
            count_client()
        elif choice == 0:
            end()
    except ValueError:
        print("[ERROR] Invalid input: Please enter a number.")
        return_to_principal()
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        return_to_principal()


def invalid_option():
    os.system('cls')
    print("[ERROR] Invalid option")
    return_to_principal()


def view_clients():
    os.system('cls')
    stmt_all_client = select(Client)
    print("\nClients in Database")
    for client in session.scalars(stmt_all_client):
        print(client)
    return_to_principal()


def view_accounts():
    os.system('cls')
    stmt_all_accounts = select(Account)
    print("\nAccounts in Database")
    for account in session.scalars(stmt_all_accounts):
        print(account)
    return_to_principal()


def search_client_by_id(identifier):
    os.system('cls')
    print("Selected client:")
    stmt_search_clients = select(Client).where(Client.id == identifier)
    client = session.scalars(stmt_search_clients).first()
    print(client)
    return_to_principal()


def search_account_by_id(identifier):
    os.system('cls')
    print("Selected account:")
    stmt_search_account = select(Account).where(Account.id == identifier)
    account = session.scalars(stmt_search_account).first()
    print(account)
    return_to_principal()


def client_balance(identifier):
    os.system('cls')
    print("Client balance:")

    stmt_client_balance = (
            select(Client.name, Client.cpf, Account.type, Account.balance)
            .where(Client.id == identifier)
            .join(Account, Client.id == Account.id_client)
        )

    result = session.execute(stmt_client_balance).all()

    if result:
        for name, cpf, account_type, balance in result:
            print(f"Name: {name} | CPF: {cpf} | Account Type: {account_type} | Balance: {balance:.2f}")
    else:
        print("No accounts found for this client.")

    return_to_principal()


def count_client():
    os.system('cls')
    stmt_count_client = select(func.count('*')).select_from(Client)
    for count in session.scalars(stmt_count_client):
        print(count)
    return_to_principal()


def return_to_principal():
    input('Press enter to return')
    main()


def end():
    os.system('cls')
    print("End system...")
    sleep(2)
    os.system('cls')


main()
