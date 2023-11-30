#app.py
from fastapi import FastAPI
import pika
import json
from classes import RequestCliente, RequestProduto, RequestVenda, RequestVendedor
import logging

logger = logging.getLogger(__name__)
logging.getLogger("pika").propagate = False
FORMAT = "[%(asctime)s %(filename)s->%(funcName)s():%(lineno)s]%(levelname)s: %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

app = FastAPI()

# Configurações do RabbitMQ
# rabbitmq_url = "rabbitmq-service"
# connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
# channel = connection.channel()
# channel.queue_declare(queue='database_operations')


credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('rabbitmq-service',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()


#Cliente
@app.post("/create_client")
async def create_client(client: RequestCliente):
    # if not connection or connection.is_closed:
    #     connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
    message = {"operation": "create_client", "data": client.dict()}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": "Create client request sent"}

@app.post("/update_client/{client_id}")
async def update_client(client_id: int, client: RequestCliente):
    message = {"operation": "update_client", "client_id": client_id, "data": client.dict()}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Update client request for ID {client_id} sent"}

@app.get("/get_client/{client_id}")
async def get_client(client_id: int):
    message = {"operation": "get_client", "client_id": client_id}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Get client request for ID {client_id} sent"}

@app.delete("/delete_client/{client_id}")
async def delete_client(client_id: int):
    message = {"operation": "delete_client", "client_id": client_id}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Delete client request for ID {client_id} sent"}

#Vendedor
@app.post("/create_vendedor")
async def create_vendedor(vendedor: RequestVendedor):
    message = {"operation": "create_vendedor", "data": vendedor.dict()}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": "Create vendedor request sent"}

@app.post("/update_vendedor/{vendedor_id}")
async def update_vendedor(vendedor_id: int, vendedor: RequestVendedor):
    message = {"operation": "update_vendedor", "vendedor_id": vendedor_id, "data": vendedor.dict()}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Update vendedor request for ID {vendedor_id} sent"}

@app.get("/get_vendedor/{vendedor_id}")
async def get_vendedor(vendedor_id: int):
    message = {"operation": "get_vendedor", "vendedor_id": vendedor_id}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Get vendedor request for ID {vendedor_id} sent"}

@app.delete("/delete_vendedor/{vendedor_id}")
async def delete_vendedor(vendedor_id: int):
    message = {"operation": "delete_vendedor", "vendedor_id": vendedor_id}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Delete vendedor request for ID {vendedor_id} sent"}

#Produto
@app.post("/create_produto")
async def create_produto(produto: RequestProduto):
    message = {"operation": "create_produto", "data": produto.dict()}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": "Create produto request sent"}

@app.post("/update_produto/{produto_id}")
async def update_produto(produto_id: int, produto: RequestProduto):
    message = {"operation": "update_produto", "produto_id": produto_id, "data": produto.dict()}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Update produto request for ID {produto_id} sent"}

@app.get("/get_produto/{produto_id}")
async def get_produto(produto_id: int):
    message = {"operation": "get_produto", "produto_id": produto_id}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Get produto request for ID {produto_id} sent"}

@app.delete("/delete_produto/{produto_id}")
async def delete_produto(produto_id: int):
    message = {"operation": "delete_produto", "produto_id": produto_id}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Delete produto request for ID {produto_id} sent"}

#Venda
@app.post("/create_venda")
async def create_venda(venda: RequestVenda):
    message = {"operation": "create_venda", "data": venda.dict()}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": "Create venda request sent"}

@app.post("/update_venda/{venda_id}")
async def update_venda(venda_id: int, venda: RequestVenda):
    message = {"operation": "update_venda", "venda_id": venda_id, "data": venda.dict()}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Update venda request for ID {venda_id} sent"}

@app.get("/get_venda/{venda_id}")
async def get_venda(venda_id: int):
    message = {"operation": "get_venda", "venda_id": venda_id}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Get venda request for ID {venda_id} sent"}

@app.delete("/delete_venda/{venda_id}")
async def delete_venda(venda_id: int):
    message = {"operation": "delete_venda", "venda_id": venda_id}
    channel.basic_publish(exchange='',
                          routing_key='database_operations',
                          body=json.dumps(message))
    return {"message": f"Delete venda request for ID {venda_id} sent"}