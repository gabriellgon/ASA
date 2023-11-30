#subscriber.py
import pika
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
import json
import os
import sys
from models import Cliente, Vendedor, Produto, Venda

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
db_session = Session()

Base = declarative_base()

#Cliente
def create_client(request_data: dict):
    client_data = request_data['data']
    new_client = Cliente(**client_data)
    db_session.add(new_client)
    db_session.commit()

def update_client(request_data: dict):
    client_id = request_data['client_id']
    updated_data = request_data['data']

    client = db_session.query(Cliente).filter_by(id=client_id).first()
    if client:
        for key, value in updated_data.items():
            setattr(client, key, value)
        db_session.commit()
        print(f"Client with ID {client_id} updated successfully")
    else:
        print(f"Client with ID {client_id} not found")

def get_client(request_data: dict):
    client_id = request_data['client_id']
    client = db_session.query(Cliente).filter_by(id=client_id).first()
    if client:
        client_dict = client.__dict__
        client_dict.pop('_sa_instance_state', None)
        print(f"Client with ID {client_id}: {client_dict}")
    else:
        print(f"Client with ID {client_id} not found")

def delete_client(request_data: dict):
    client_id = request_data['client_id']
    client = db_session.query(Cliente).filter_by(id=client_id).first()
    if client:
        db_session.delete(client)
        db_session.commit()
        print(f"Client with ID {client_id} deleted successfully")
    else:
        print(f"Client with ID {client_id} not found")

#Vendedor
def create_vendedor(request_data: dict):
    vendedor_data = request_data['data']
    new_vendedor = Vendedor(**vendedor_data)
    db_session.add(new_vendedor)
    db_session.commit()

def update_vendedor(request_data: dict):
    vendedor_id = request_data['vendedor_id']
    updated_data = request_data['data']

    vendedor = db_session.query(Vendedor).filter_by(id=vendedor_id).first()
    if vendedor:
        for key, value in updated_data.items():
            setattr(vendedor, key, value)
        db_session.commit()
        print(f"Vendedor with ID {vendedor_id} updated successfully")
    else:
        print(f"Vendedor with ID {vendedor_id} not found")

def get_vendedor(request_data: dict):
    vendedor_id = request_data['vendedor_id']
    vendedor = db_session.query(Vendedor).filter_by(id=vendedor_id).first()
    if vendedor:
        vendedor_dict = vendedor.__dict__
        vendedor_dict.pop('_sa_instance_state', None)
        print(f"Vendedor with ID {vendedor_id}: {vendedor_dict}")
    else:
        print(f"Vendedor with ID {vendedor_id} not found")

def delete_vendedor(request_data: dict):
    vendedor_id = request_data['vendedor_id']
    vendedor = db_session.query(Vendedor).filter_by(id=vendedor_id).first()
    if vendedor:
        db_session.delete(vendedor)
        db_session.commit()
        print(f"Vendedor with ID {vendedor_id} deleted successfully")
    else:
        print(f"Vendedor with ID {vendedor_id} not found")

#Produto
def create_produto(request_data: dict):
    produto_data = request_data['data']
    new_produto = Produto(**produto_data)
    db_session.add(new_produto)
    db_session.commit()

def update_produto(request_data: dict):
    produto_id = request_data['produto_id']
    updated_data = request_data['data']

    produto = db_session.query(Produto).filter_by(id=produto_id).first()
    if produto:
        for key, value in updated_data.items():
            setattr(produto, key, value)
        db_session.commit()
        print(f"Produto with ID {produto_id} updated successfully")
    else:
        print(f"Produto with ID {produto_id} not found")

def get_produto(request_data: dict):
    produto_id = request_data['produto_id']
    produto = db_session.query(Produto).filter_by(id=produto_id).first()
    if produto:
        produto_dict = produto.__dict__
        produto_dict.pop('_sa_instance_state', None)
        print(f"Produto with ID {produto_id}: {produto_dict}")
    else:
        print(f"Produto with ID {produto_id} not found")
        
def delete_produto(request_data: dict):
    produto_id = request_data['produto_id']
    produto = db_session.query(Produto).filter_by(id=produto_id).first()
    if produto:
        db_session.delete(produto)
        db_session.commit()
        print(f"Produto with ID {produto_id} deleted successfully")
    else:
        print(f"Produto with ID {produto_id} not found")

#Venda
def create_venda(request_data: dict):
    venda_data = request_data['data']
    new_venda = Venda(**venda_data)
    db_session.add(new_venda)
    db_session.commit()

def update_venda(request_data: dict):
    venda_id = request_data['venda_id']
    updated_data = request_data['data']

    venda = db_session.query(Venda).filter_by(id=venda_id).first()
    if venda:
        for key, value in updated_data.items():
            setattr(venda, key, value)
        db_session.commit()
        print(f"Venda with ID {venda_id} updated successfully")
    else:
        print(f"Venda with ID {venda_id} not found")

def get_venda(request_data: dict):
    venda_id = request_data['venda_id']
    venda = db_session.query(Venda).filter_by(id=venda_id).first()
    if venda:
        venda_dict = venda.__dict__
        venda_dict.pop('_sa_instance_state', None)
        print(f"Venda with ID {venda_id}: {venda_dict}")
    else:
        print(f"Venda with ID {venda_id} not found")

def delete_venda(request_data: dict):
    venda_id = request_data['venda_id']
    venda = db_session.query(Venda).filter_by(id=venda_id).first()
    if venda:
        db_session.delete(venda)
        db_session.commit()
        print(f"Venda with ID {venda_id} deleted successfully")
    else:
        print(f"Venda with ID {venda_id} not found")

def main ():
    # Configurações do RabbitMQ
    # rabbitmq_url = "localhost"
    # connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
    # channel = connection.channel()
    # channel.queue_declare(queue='database_operations')


    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       '/',
                                       credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='database_operations')
    channel.queue_bind(exchange='', queue='database_operations', routing_key="")


    def callback(ch, method, properties, body):
        request_data = json.loads(body.decode())
        operation = request_data['operation']

        if operation == 'create_client':
            create_client(request_data)
            print("Client created successfully")
        elif operation == 'update_client':
            update_client(request_data)
        elif operation == 'get_client':
            get_client(request_data)
        elif operation == 'delete_client':
            delete_client(request_data)
        elif operation == 'create_vendedor':
            create_vendedor(request_data)
            print("vendedor created successfully")
        elif operation == 'update_vendedor':
            update_vendedor(request_data)
        elif operation == 'get_vendedor':
            get_vendedor(request_data)
        elif operation == 'delete_vendedor':
            delete_vendedor(request_data)
        elif operation == 'create_produto':
            create_produto(request_data)
            print("Produto created successfully")
        elif operation == 'update_produto':
            update_produto(request_data)
        elif operation == 'get_produto':
            get_produto(request_data)
        elif operation == 'delete_produto':
            delete_produto(request_data)
        elif operation == 'create_venda':
            create_venda(request_data)
            print("Venda created successfully")
        elif operation == 'update_venda':
            update_venda(request_data)
        elif operation == 'get_venda':
            get_venda(request_data)
        elif operation == 'delete_venda':
            delete_venda(request_data)

    channel.basic_consume(queue='database_operations',
                          on_message_callback=callback,
                          auto_ack=True)

    print('Waiting for messages. To exit, press CTRL+C')
    channel.start_consuming()