# aplicacao
from main import app, db

# pip installed
from flask import jsonify, request, redirect, url_for

# app modules
from models.produtoModel import Produto
from dao.produtosDao import ProdutosDao
from helpers import salvaImagem, excluiImagem, getUrlFormats
from validacao import validacaoFormulario
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
    imagem = getUrlFormats(data['url-imagem'])

    produto = validacaoFormulario(data, imagem['type'])
    if not type(produto) is Produto:
        return jsonify(produto), 415
        
    produto = produtoDao.salvar(produto)
    salvaImagem(produto.id, data['url-imagem'], app.config['UPLOAD_PATH'], imagem['url'], imagem['type'].split("/")[-1])
    return redirect(url_for('busca', id = produto.id))


@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.get_json()    
    imagem = getUrlFormats(data['url-imagem'])

    produto = validacaoFormulario(data, imagem['type'], id)
    if not type(produto) is Produto:
        return jsonify(produto), 415    

    produto = produtoDao.salvar(produto)
    excluiImagem(id)
    salvaImagem(produto.id, data['url-imagem'], app.config['UPLOAD_PATH'], imagem['url'], imagem['type'].split("/")[-1])
    return redirect(url_for('busca', id = id))


@app.route('/produtos/<int:id>', methods=['DELETE'])
def remover(id):    
    try:
        produtoDao.deletar(id)
        excluiImagem(id)
    except:
        return jsonify({"datail": "An error has ocurred"})
    return redirect(url_for('listar'))