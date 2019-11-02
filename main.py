# pip installed
from flask import Flask, jsonify, request, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename

from io import StringIO, BytesIO
from PIL import Image
import urllib.request
import os


# app modules
from models import Produto
from dao import ProdutosDao

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)
produtoDao = ProdutosDao(db)


@app.route('/produtos', methods=['GET'])
def listar():
    try:
        response = jsonify(produtoDao.listar()), 200
    except:
        response = jsonify({"detail" : "Internal Server Error"}), 500
    return response


@app.route('/produtos/<int:id>', methods=['GET'])
def busca(id):
    try:
        response = jsonify(produtoDao.busca_por_id(id).json_encode()), 200
    except:
        response = jsonify({"detail" : "Not Found"}), 404
    return response


@app.route('/produtos', methods=['POST'])
def cadastrar():
    data = request.get_json()
    produto = Produto(data['nome'], data['descricao'],data['categoria'], data['preco'], data['marca'])    
    produto = produtoDao.salvar(produto)
    salvaImagem(produto.id, data['url-imagem'], app.config['UPLOAD_PATH'])
    return redirect(url_for('busca', id = produto.id))


@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.get_json()    
    produto = Produto(data['nome'], data['descricao'],data['categoria'], data['preco'], data['marca'], id)  
    produto = produtoDao.salvar(produto)     
    
    excluiImagem(id)
    salvaImagem(produto.id, data['url-imagem'], app.config['UPLOAD_PATH'])
    return redirect(url_for('busca', id = id))


@app.route('/produtos/<int:id>', methods=['DELETE'])
def remover(id):    
    produtoDao.deletar(id)
    excluiImagem(id)
    return redirect(url_for('listar'))



#métodos de manipulaçao de arquivo, criar helper pra isso
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




def json_encode(object):
        return object.__dict__

def excluiImagem(id):    
    arquivo = recuperarImagem(id)
    try:
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
    except:
        return


def recuperarImagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'produto_{id}' in nome_arquivo:
            return nome_arquivo  



app.run(debug=True)