from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import text


engine = create_engine('sqlite:///:memory:')

metadata_obj = MetaData()

user = Table(
    'user', metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)

user_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)


# Verificando as informações
print("\nInfo da tabela users")
print(user_prefs.primary_key)
print(user_prefs.constraints)
print(user_prefs.foreign_keys)

for table in metadata_obj.sorted_tables:
    print(table)

metadata_obj.create_all(engine)

# Novo schema
metadata_bd_obj = MetaData()
financial_info = Table(
    'financial_info', metadata_bd_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)

print("\nInfo da tabela financial_info")
print(financial_info.primary_key)
print(financial_info.constraints)

print('\nExecutando statement SQL')

# Inserindo dados na tabela 'user' e realizando a consulta
sql_insert = text("INSERT INTO user (user_id, user_name, email_address, nickname) VALUES (2, 'fernanda', 'fernanda@hotmail.com', 'fe')")

# Usando a conexão para inserir e consultar os dados
with engine.connect() as connection:
    connection.execute(sql_insert)
    sql_select = text('SELECT * FROM user')
    result = connection.execute(sql_select)
    for row in result:
        print(row)