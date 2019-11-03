from models.produtoModel import Produto

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

def validacaoFormulario(data, image_type, id=None):    
    if not isNumber(data['preco']):
        return {"detail" : "field price is not valid"}  
    
    if not isImage(image_type):
        return {"detail" : "field image is not valid"}

    return Produto(data['nome'], data['descricao'],data['categoria'], data['preco'], data['marca'], id)