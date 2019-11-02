import os
from config import UPLOAD_PATH


def salvaImagem():
    pass

def excluiImagem(id):
    arquivo = recupera_imagem(id)
    os.remove(os.path.join(UPLOAD_PATH, arquivo))


def recuperarImagem(id):
    for nome_arquivo in os.listdir(UPLOAD_PATH):
        if f'produto_{id}' in nome_arquivo:
            return f'{UPLOAD_PATH}/{nome_arquivo}'
