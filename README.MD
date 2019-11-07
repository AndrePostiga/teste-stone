#`Desafio Mundipagg StoneCo`

#`Desafio para vaga de desenvolvedor júnior na Mundipagg`
------------------------------

##### `Objetivo`
Desenvolver uma API Rest utilizando Python e o framework Flask, e, persistir os dados utilizando MySQL

##### `USO`
A Aplicação utiliza docker para facilitar a compilação do ambiente de desenvolvimento em qualquer máquina, para rodar o projeto do projeto basta buildar a imagem e rodar o container dentro do diretório

```docker
docker build -f .\Dockerfile -t andre/flask .
docker run -it -v "Seu_diretório_da_pasta_app:/var/www" -p 5000:5000 andre/flask
`````

O Serviço rodará em:
````
http://localhost:5000/produtos
````

Para consumir o serviço, o aplicativo utilizado foi o Postman <img src="https://www.getpostman.com/img/v2/logo-glyph.png?c01252cc6858ff9679973eb0c62ef27e" width="20">, que permite alterar os verbos do protocolo HTTP e mandar uma requisição complexa com muita simplicidade

##### ```ENDPOINTS```
A API conta com os seguintes endpoints
<img src="https://i.imgur.com/KG3H1QU.png">

Para realizar uma criação ou alteração basta enviar um JSON para os endpoints:
```
POST /produtos 
ou 
PUT /produtos/{id}
```
```JSON
{
    "nome": "Sapato",
    "descricao": "Tenis muito legal",
    "url-imagem" : "https://static.netshoes.com.br/produtos/sandalia-infantil-nike-sunray-protect-2/37/HZM-0783-937/HZM-0783-937_detalhe1.jpg?resize=280:280",
    "categoria": "Sapato Preto Fresh Fuinha",
    "preco": 235.0 ,
    "marca": "New Balance"
}
```
A imagem deve ser um link que conhenha um content-type, caso contrário o programa ignorará e retornará uma resposta indicando o erro. Caso o campo url-imagem seja passado de forma incorreta, nula, ou não seja passado, o programa entenderá como um objeto sem imagem ou excluirá a existente em caso de edição.

##### ``Aplicação``
Para criar a aplicação me baseei em projetos antigos que resolveram meus problemas de forma enxuta, organizar o projeto com um controller, um modelo e um DAO, me ajudou a escrever pouco código e realizar muitas tarefas.

Como o desafio não necessita de muitas regras de negócio, achei desnecessário seguir o modelo (MODEL -> SERVICE -> DAO), são poucas as validações que este projeto requere, não precisa de muita manipulação de dados, portanto, decidi colocá-las dentro do módulo helpers.

Essa arquitetura escolhida facilita a implementação caso se queira escalar o projeto com novos modelos ou novos controllers 

A Arquitetura escolhida para o desafio foi:
<img src="https://i.imgur.com/P4FUkPq.jpg">

O modelo para produtos é enxuto, me utilizei da orientação a objetos para deixar o código mais semântico e fácil de ler/escrever. Ele possui apenas seus atributos e uma método que retorna meu objeto em outro formato, facilitando a manipulação em alguns casos. Caso seja necessário implementar outros métodos é possível, basta adicionar na sua classe. 

Já o modelo DAO possui todas as strings SQL necessárias para realizar um CRUD básico, esta classe se aproveita do modelo da classe produto para retornar os dados de forma simplificada.

<img src="https://i.imgur.com/1gnQkqu.jpg">

O Dockerfile roda uma imagem pronta do Python com a distribuição Alpine do Linux presente no DockerHub, algumas dependências extras foram adicionadas pois o pacote mysqlclient do Python não está funcionando caso seja instalado da web, se faz necessário utilizar os pacotes descritos abaixo, ou baixar manualmente o client e instalar via pip.

```docker
FROM python:3.7-alpine 
MAINTAINER Andre Postiga

COPY app /var/www
WORKDIR /var/www

RUN pip install --upgrade pip

RUN pip install virtualenv
CMD ["venv/scripts/activate"]
RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                mariadb-dev \
                python3-dev \
                postgresql-dev \
                # Pillow dependencies
                jpeg-dev \
                zlib-dev \
                freetype-dev \
                lcms2-dev \
                openjpeg-dev \
                tiff-dev \
                tk-dev \
                tcl-dev \
                harfbuzz-dev \
                fribidi-dev \
        ;
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
```

Por fim, para auxiliar a criação do projeto, um arquivo contendo as configurações estáticas foi criado, com a finalidade de utilizar as constantes deixando o código mais legível. Para criar a tabela produtos um script também foi criado para facilitar a criação do projeto caso fosse migrar para um outro banco de dados relacional.

<small>Estrutura de pastas:</small>
````````
/
|   .gitignore
|   criarBanco.py
|   Dockerfile
|   output.txt
|   README.MD
|   
\---app
    |   config.py
    |   helpers.py
    |   main.py
    |   requirements.txt
    |   
    +---controllers
    |   |   produto.py
    |            
    |           
    +---dao
    |   |   produtosDao.py
    |             
    |           
    +---models
    |   |   produtoModel.py
    |       
    |           
    +---uploads
    |   |   produto_891.JPEG       

````````            
##### ``Considerações``
Considerações
Apesar de ter uma experiência com programação para resolver problemas, foi a primeira vez em que me aventurei criando um serviço web. Fiz um curso sobre a estruturação de uma API Rest com Python e já conhecia um pouco sobre o modelo REST, então foi engrandecedor ver como este se aplica à linguagem de programação que até então eu utilizara para programar hardware(Raspberry) e trabalhar com dados (Pandas). É muito interessante ver uma linguagem pode ser tão versátil de modo que muitas pessoas consigam contribuir para a comunidade.

Fazer este projeto no prazo estipulado foi um desafio (dado que a semana foi turbulenta), mas ainda assim, sair da zona de conforto mostra que é possível superar as dificuldades encontradas ao longo do processo de construção do código. Fazer uma aplicação que eu nunca havia feito me fez encontrar contratempos que nunca havia enfrentado. Com ajuda da comunidade, da iniciativa open source e de documentações disponíveis fui buscando a melhor maneira de ajuste. Ainda assim, como toda boa interpolação, ela nunca representará a curva ideal.

Alguns pontos que pretendo melhorar no futuro: 

Criar um docker compose; 
Aumentar a abstração do código com orientação a objetos/funcional;
Adicionar camada de serviço com as regras de negócios; 
Utilizar mais bibliotecas como SQLAlquemy; 
Flask Restplus; 
Adicionar camadas de autenticação; 
Utilizar outras formas de persistência de dados com bancos noSQL.



