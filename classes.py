from pydantic import BaseModel

# Definição dos modelos Pydantic
class RequestCliente(BaseModel):
    nome: str
    email: str
    cpf: str
    telefone: str
    endereco: str

class RequestVendedor(BaseModel):
    nome: str
    email: str
    cpf: str
    telefone: str
    endereco: str

class RequestProduto(BaseModel):
    tipo_sapato: str
    cor: str
    tamanho: int
    valor: float

class RequestVenda(BaseModel):
    vendedor_id: int
    cliente_id: int
    valor: float
