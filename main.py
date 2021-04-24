from mysql.connector import connect

def execute(sql, params=None):
    """ Executa um comando no mysql e salva os valores
        Serve para: inser, update, delete, create, alter, drop
    """
    with connect(host="localhost", user="root", password="225456", database="bluecommerce10") as conn: # conecta no banco
        with conn.cursor() as cursor: # abre uma página para executar coisas
            cursor.execute(sql, params) # executa o sql que está sendo passado por parametro
            conn.commit() # grava as coisas no banco de dados

def query(sql, params=None):
    """ Executa um comando no mysql e retorna o resultado
        Serve para: Select, SHOW """
    with connect(host="localhost", user="root", password="225456", database="bluecommerce10") as conn: #conecta no banco
        with conn.cursor() as cursor: # abre uma página para executar coisas
            cursor.execute(sql, params) # executa o sql que está sendo passado por parametro
            return cursor.fetchall() # pega o resultado da consulta e retorna

def create_table(nome_tabela, colunas):
    execute(f"""CREATE TABLE {nome_tabela} (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    {colunas}
)""")

def alter_table(nome_tabela):
    execute(f"""ALTER TABLE {nome_tabela} ADD CONSTRAINT fk_vendas_produtos_id_produto FOREIGN KEY (id_produto) REFERENCES produtos(id)""")
    execute(f"""ALTER TABLE {nome_tabela} ADD CONSTRAINT fk_vendas_produtos_id_venda FOREIGN KEY (id_venda) REFERENCES vendas(id)""")

def delete_value(nome_tabela, colunas, id):
    execute(f"DELETE FROM {nome_tabela} WHERE {colunas} = {id}")

tabelas = {"paises": "sigla char(3), nome varchar(255)",
           "estados": "sigla char(3), nome varchar(255)",
           "cidades": "sigla char(3), nome varchar(255)",
           "usuários": "sigla char(3), nome varchar(255)",
           "produtos": "sigla char(3), nome varchar(255)",
           "categoria_produtos": "sigla char(3), nome varchar(255)",
           "vendas": "sigla char(3), nome varchar(255)",
           "venda_produtos": "sigla char(3), nome varchar(255), id_produto INT UNSIGNED NOT NULL, id_venda INT UNSIGNED NOT NULL",
           "estoques": "sigla char(3), nome varchar(255)"
           }

#for tabela, colunas in tabelas.items():
#    create_table(tabela, colunas)

#APAGA UM VALOR DENTRO DE UMA COLUNA EM UMA TABELA
#delete_value("", "", "")


#alter_table("venda_produtos")