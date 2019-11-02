import helpers

class Produto:
    def __init__(self, nome, descricao, categoria, preco, marca, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao        
        self.categoria = categoria
        self.preco = preco
        self.marca = marca
        self.imagem = helpers.recuperarImagem(id)
    
    def json_encode(self):
        return self.__dict__
    
        