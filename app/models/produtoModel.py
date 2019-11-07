# app modules
from helpers import recuperarImagem

class Produto:
    def __init__(self, nome, descricao, categoria, preco, marca, imagem=None, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao        
        self.categoria = categoria
        self.preco = preco
        self.marca = marca

        if not imagem == None: 
            self.imagem = imagem
        else:            
            self.imagem = recuperarImagem(id)
        
    
    def json_encode(self):
        return self.__dict__
    
        