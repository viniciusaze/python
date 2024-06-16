import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base() # Declarando a base


class User(Base):
    __tablename__ = "user_accont" # Nome da tabela
    # Atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    ) # Criando o relacionamento

    def __repr__(self): # Representação da classe
        return f"User (id={self.id}, name={self.name}, fullname={self.fullname}"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False) # Referenciando a chave estrangeira

    user = relationship("User", back_populates="address")

    def __repr__(self): # Representação da classe
        return f"Address (id={self.id}, email={self.email_address})"

print(User.__tablename__)
print(Address.__tablename__)
print('oi')


