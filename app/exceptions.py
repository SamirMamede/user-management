class MongoDBConnectionError(Exception):
    """
    Erro ao conectar-se ao banco de dados MongoDB.

    Pode ser devido a problemas de rede, credenciais incorretas, servidor indisponível, ou outros problemas de conectividade.

    Verifique:
    - Se o servidor MongoDB está em execução.
    - Se as credenciais de conexão estão corretas.
    - Se há problemas de rede que impedem a conexão.
    """
    pass

class MongoDBCollectionError(Exception):
    """
    Erro ao obter uma coleção específica do banco de dados MongoDB.

    Pode ocorrer se a coleção não existir, se não houver permissões para acessá-la, ou se houver outros problemas com o banco de dados.

    Verifique:
    - Se o nome da coleção está correto.
    - Se o banco de dados está configurado corretamente.
    - Se o usuário tem permissões para acessar a coleção.
    """
    pass