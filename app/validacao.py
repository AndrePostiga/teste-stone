from models.produtoModel import Produto
import urllib.request

def isNumber(value):
    value = str(value)
    if not value.strip().replace('-', '').replace('+', '').replace('.', '').isdigit():
        return False
    try:
         float(value)
    except ValueError:
         return False

    return True

def isImage(image_type):
    formats = {
        'image/jpeg': 'JPEG',
        'image/png': 'PNG',
        'image/gif': 'GIF'
    }

    try:
        format = formats[image_type]
    except:
        return False
    
    return True

def validacaoFormulario(data, id=None):    
    if not isNumber(data['preco']):
        return {"detail" : "field price is not valid"}      
    
    try:
        imagem = getUrlFormats(data['url-imagem'])
    except:
        return Produto(data['nome'], data['descricao'],data['categoria'], data['preco'], data['marca'], id=id)

    if not isImage(imagem['type']):
        return {"detail" : "field image is not valid"}

    return Produto(data['nome'], data['descricao'],data['categoria'], data['preco'], data['marca'], imagem=imagem, id=id)


def getUrlFormats(url):
    imageUrl = urllib.request.urlopen(url)
    image_type = imageUrl.info().get('Content-Type')

    return {
        "url" : imageUrl,
        "type" : image_type
    }