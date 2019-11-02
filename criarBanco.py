import MySQLdb
conn = MySQLdb.connect(user='bd011b993abccb', passwd='2bd4da8b', host='us-cdbr-iron-east-05.cleardb.net', port=3306)

# Descomente se quiser desfazer o banco...
#conn.cursor().execute("DROP DATABASE `jogoteca`;")
#conn.commit()

criar_tabela = '''SET NAMES utf8;
    USE `heroku_f2b0b326ed67e14`;
    CREATE TABLE `produtos` (
      `id` integer NOT NULL AUTO_INCREMENT,
      `nome` varchar(255) COLLATE utf8_bin NOT NULL,
      `descricao` varchar(255) COLLATE utf8_bin NOT NULL,
      `categoria` varchar(255) COLLATE utf8_bin NOT NULL,
      `preco` double NOT NULL,
      `marca` varchar(255) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabela)


# populando a tabela
cursor = conn.cursor()
cursor.execute('INSERT INTO heroku_f2b0b326ed67e14.produtos (nome, descricao, categoria, preco, marca) VALUES (%s, %s, %s, %s, %s)',
      ('Sapato', 'Tenis muito lindo', 'Sapato',500,'New Balance'))

cursor.execute('INSERT INTO heroku_f2b0b326ed67e14.produtos (nome, descricao, categoria, preco, marca) VALUES (%s, %s, %s, %s, %s)',
      ('Camisa', 'camisa preta', 'Tshirt',100,'Supreme'))

cursor.execute('INSERT INTO heroku_f2b0b326ed67e14.produtos (nome, descricao, categoria, preco, marca) VALUES (%s, %s, %s, %s, %s)',
      ('Colar', 'colar de pedras', 'acessório',20,'artesanal'))


cursor.execute('select * from heroku_f2b0b326ed67e14.produtos')
print(' -------------  Produtos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()