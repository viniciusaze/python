import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column , create_engine, inspect, select, func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import select


Base = declarative_base() # Declarando a base


class User(Base):
    __tablename__ = "user_account" # Nome da tabela
    # Atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    ) # Criando o relacionamento

    def __repr__(self): # Representação da classe
        return f"User (id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False) # Referenciando a chave estrangeira

    user = relationship("User", back_populates="address")

    def __repr__(self): # Representação da classe
        return f"Address (id={self.id}, email_address={self.email_address})"

print(User.__tablename__)
print(Address.__tablename__)

# Conexão com banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Inspetor = investiga o esquema do banco de dados
inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    vinicius = User(
        name='Vinicius',
        fullname='Vinicius Azevedo',
        address=[Address(email_address='ar-vinicius@hotmail.com')]
    )

    fernanda = User(
        name='Fernanda',
        fullname='Fernanda Meyer',
        address=[Address(email_address='fernandameyer04@hotmail.com'),
                 Address(email_address='fernandameeyer@gmail.com')]
    )

    patrick = User(
        name='Patrick',
        fullname='Patrick Galileu'
    )

    # Enviando para o banco de dados (persistência de dados)
    session.add_all([vinicius, fernanda, patrick])

    session.commit()

stmt_user = select(User).where(User.name.in_(['Vinicius', 'Fernanda']))
print('\nRecuperando usuários a partir de condição de filtragem')
for user in session.scalars(stmt_user):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print('\nRecuperando endereços a partir de condição de filtragem')
for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc()) # Padrão de ordenamento é ascendente
print('\nRecuperando informação de maneira ordenada')
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print('\nExecutando statement a partir da connection')
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print('\nTotal de instancias em User')
for result in session.scalars(stmt_count):
    print(result)
