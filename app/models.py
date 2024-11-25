from pydantic import BaseModel, EmailStr
from typing import Optional

class Client(BaseModel):
    id: Optional[str]
    razao_social: str
    nome_fantasia: str
    cnpj: str
    proprietario: str
    cpf_proprietario: str
    rg_proprietario: str
    responsavel: str
    cpf_responsavel: str
    sistema_que_utiliza: str
    mensalidade: float
    inscricao_estadual: Optional[str]
    inscricao_municipal: Optional[str]
    cnae_fiscal: Optional[str]
    regime_tributario: str
    email: EmailStr
    celular: str
    cep: str
    municipio: str
    logradouro: str
    numero: str
    bairro: str