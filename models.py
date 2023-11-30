from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.engine import URL

# Definindo a URL para conexão no banco
url = URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='banco',
    host='localhost',
    database='loja_calcados',
    port=5432
)

# Nesse ponto são instanciados os objetos para conexão com o banco
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id       = Column(Integer, primary_key=True)
    nome     = Column(String, nullable=False)
    email    = Column(String, nullable=False, unique=True)
    cpf      = Column(String, nullable=False, unique=True)
    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)

class Vendedor(Base):
    __tablename__ = 'vendedores'

    id       = Column(Integer, primary_key=True)
    nome     = Column(String, nullable=False)
    email    = Column(String, nullable=False, unique=True)
    cpf      = Column(String, nullable=False, unique=True)
    telefone = Column(String, nullable=False)
    endereco = Column(String, nullable=False)

class Produto(Base):
    __tablename__ = 'produtos'

    id          = Column(Integer, primary_key=True)
    tipo_sapato = Column(String, nullable=False)
    cor         = Column(String, nullable=False)
    tamanho     = Column(Integer, nullable=False)
    valor       = Column(Float, nullable=False)

class Venda(Base):
    __tablename__ = 'vendas'

    id          = Column(Integer, primary_key=True)
    vendedor_id = Column(Integer, ForeignKey('vendedores.id'))
    vendedor    = relationship(Vendedor)
    cliente_id  = Column(Integer, ForeignKey('clientes.id'))
    cliente     = relationship(Cliente)
    valor       = Column(Float, nullable=False)

# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)