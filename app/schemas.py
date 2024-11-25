def clientEntity(client) -> dict:
    return { 
        "id": str(client["_id"]),
        "razao_social": client.get("razao_social", ""),
        "nome_fantasia": client.get("nome_fantasia", ""),
        "cnpj": client.get("cnpj", ""),
        "proprietario": client.get("proprietario", ""),
        "cpf_proprietario": client.get("cpf_proprietario", ""),
        "rg_proprietario": client.get("rg_proprietario", ""),
        "responsavel": client.get("responsavel", ""),
        "cpf_responsavel": client.get("cpf_responsavel", ""),
        "sistema_que_utiliza": client.get("sistema_que_utiliza", ""),
        "mensalidade": client.get("mensalidade", 0),
        "inscricao_estadual": client.get("inscricao_estadual", ""),
        "inscricao_municipal": client.get("inscricao_municipal", ""),
        "cnae_fiscal": client.get("cnae_fiscal", ""),
        "regime_tributario": client.get("regime_tributario", ""),
        "email": client.get("email", ""),
        "celular": client.get("celular", ""),
        "cep": client.get("cep", ""),
        "municipio": client.get("municipio", ""),
        "logradouro": client.get("logradouro", ""),
        "numero": client.get("numero", ""),
        "bairro": client.get("bairro", ""),
    }

def clientsEntity(entity) -> list:
    return [clientEntity(client) for client in entity]