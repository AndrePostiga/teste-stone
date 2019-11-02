from models import Produto

#Queries
SQL_DELETA = 'delete from produtos where id = %s'
SQL_SELECT_POR_ID = 'SELECT * from produtos where id = %s'
SQL_ATUALIZAR_PRODUTO = 'UPDATE produtos SET nome=%s, descricao=%s, categoria=%s, preco=%s , marca=%s  where id = %s'
SQL_BUSCA_TODOS = 'SELECT * from produtos' 
SQL_CRIAR_PRODUTO = 'INSERT INTO produtos (nome, descricao, categoria, preco, marca) values (%s, %s, %s, %s, %s)'


class ProdutosDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, produto):
        cursor = self.__db.connection.cursor()

        if (produto.id):
            cursor.execute(SQL_ATUALIZAR_PRODUTO, (produto.nome, produto.descricao, produto.categoria, produto.preco, produto.marca, produto.id))
        else:
            cursor.execute(SQL_CRIAR_PRODUTO, (produto.nome, produto.descricao, produto.categoria, produto.preco, produto.marca))
            produto.id = cursor.lastrowid
        self.__db.connection.commit()
        return produto

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_TODOS)
        produtos = traduz_produtos(cursor.fetchall())
        return produtos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Produto(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA , (id,))
        self.__db.connection.commit()


def traduz_produtos(produtos):
    def cria_produto_com_tupla(tupla):
        return Produto(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], id=tupla[0]).json_encode()
    return list(map(cria_produto_com_tupla, produtos))



