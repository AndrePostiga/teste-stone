from config import UPLOAD_PATH
import urllib.request
from PIL import Image
from io import BytesIO
import os

def salvaImagem(id, url, caminho): 
    
    formats = {
        'image/jpeg': 'JPEG',
        'image/png': 'PNG',
        'image/gif': 'GIF'
    }

    response = urllib.request.urlopen(url)
    image_type = response.info().get('Content-Type')
    
    try:
        format = formats[image_type]
    except:
        return jsonify({"detail" : str(e)}), 415 
    
    img = Image.open(BytesIO(response.read()))         
    img.save(f'{caminho}/produto_{id}.{format}')

def excluiImagem(id):    
    arquivo = recuperarImagem(id)
    try:
        os.remove(os.path.join(UPLOAD_PATH, arquivo))
    except:
        return


def recuperarImagem(id):
    for nome_arquivo in os.listdir(UPLOAD_PATH):
        if f'produto_{id}' in nome_arquivo:
            return os.path.join(UPLOAD_PATH, nome_arquivo)
