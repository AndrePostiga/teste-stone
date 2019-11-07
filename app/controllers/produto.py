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

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('listar'))

@app.route('/produtos', methods=['GET'])
def listar():    
    try:
        response = jsonify(produtoDao.listar()), 200
    except:
        response = jsonify({"detalhe" : "Erro interno de servidor"}), 500
    return response


@app.route('/produtos/<int:id>', methods=['GET'])
def busca(id):
    try:
        response = jsonify(produtoDao.busca_por_id(id).json_encode()), 200
    except:
        response = jsonify({"detalhe" : "Não Encontrado"}), 404
    return response


@app.route('/produtos', methods=['POST'])
def cadastrar():
    data = request.get_json()   
    produto = validacaoFormulario(data)

    if not type(produto) is Produto:
        return jsonify(produto), 415
        
    try:    
        produto = produtoDao.salvar(produto)    
    except:
        return jsonify({"detalhe" : "Erro interno de servidor"}), 500

    if not produto.imagem is None:
        salvaImagem(produto.id, data['url-imagem'], app.config['UPLOAD_PATH'], produto.imagem)

    return redirect(url_for('busca', id = produto.id))


@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.get_json()    
    produto = validacaoFormulario(data, id)
    
    if not type(produto) is Produto:
        return jsonify(produto), 415    

    try:    
        produto = produtoDao.salvar(produto)    
    except:
        return jsonify({"detalhe": "Erro Interno de Servidor"}), 500

    if not produto.imagem is None:
        excluiImagem(id)        

    if type(produto.imagem) is dict:
        salvaImagem(produto.id, data['url-imagem'], app.config['UPLOAD_PATH'], produto.imagem)

    return redirect(url_for('busca', id = id))


@app.route('/produtos/<int:id>', methods=['DELETE'])
def remover(id):    
    try:
        produtoDao.deletar(id)
        excluiImagem(id)
    except:
        return jsonify({"detalhe": "Erro interno de Servidor"}), 500
    return redirect(url_for('listar'))