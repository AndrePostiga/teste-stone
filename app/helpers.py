# app modules
from config import UPLOAD_PATH

# pip installed
from PIL import Image
from io import BytesIO
import urllib.request
import os



def getUrlFormats(url):
    imageUrl = urllib.request.urlopen(url)
    image_type = imageUrl.info().get('Content-Type')

    return {
        "url" : imageUrl,
        "type" : image_type
    }

def salvaImagem(id, url, caminho, imagem):     
    img = Image.open(BytesIO(imagem['url'].read()))         
    format = imagem['type'].split("/")[-1]
    img.save(f'{caminho}/produto_{id}.{format}')

def excluiImagem(id):    
    arquivo = recuperarImagem(id)
    try:
        os.remove(arquivo)
    except:
        return


def recuperarImagem(id):
    for nome_arquivo in os.listdir(UPLOAD_PATH):
        if f'produto_{id}' in nome_arquivo:
            return os.path.join(UPLOAD_PATH, nome_arquivo)
