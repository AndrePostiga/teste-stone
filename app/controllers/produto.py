# aplicacao
from main import app, db

# pip installed
from flask import jsonify, request, redirect, url_for

# app modules
from models.produtoModel import Produto
from dao.produtosDao import ProdutosDao
from helpers import salvaImagem, excluiImagem

produtoDao = ProdutosDao(db)

@app.route('/produtos', methods=['GET'])
def listar():
    return jsonify(produtoDao.listar()), 200
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