from config import UPLOAD_PATH
import urllib.request
from PIL import Image
from io import BytesIO
import os



def getUrlFormats(url):
    imageUrl = urllib.request.urlopen(url)
    image_type = imageUrl.info().get('Content-Type')

    return {
        "url" : imageUrl,
        "type" : image_type
    }

def salvaImagem(id, url, caminho, response, format):     
    img = Image.open(BytesIO(response.read()))         
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
