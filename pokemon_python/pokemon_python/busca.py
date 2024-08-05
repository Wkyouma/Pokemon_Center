from sqlalchemy import create_engine, text
from sqlalchemy.orm import session, sessionmaker
from urllib.parse import quote


# Configurar a conexão com o banco de dados
engine = create_engine(f"mysql+pymysql://root:{quote('Adjjadj7@')}@localhost:3306/pokemonzinho")

Session = sessionmaker(bind=engine)
session = Session(bind=engine)

# 1 Listar todos os treinadores
query = text("SELECT * FROM treinador")
result = session.execute(query)
for row in result:
    print(row)

# 2 Listar todos os funcionários
query = text("SELECT * FROM funcionario")
result = session.execute(query)
for row in result:
    print(row)

# 3 Listar todos os pokémons
query = text("SELECT * FROM pokemon")
result = session.execute(query)
for row in result:
    print(row)

# 4 Listar todos os produtos
query = text("SELECT * FROM produto")
result = session.execute(query)
for row in result:
    print(row)

# 5 Listar todos os centros
query = text("SELECT * FROM loja")
result = session.execute(query)
for row in result:
    print(row)

# 6 Listar todos os tratamentos
query = text("SELECT * FROM tratamento")
result = session.execute(query)
for row in result:
    print(row)

# 7 Listar todas as cobranças e seus tratamentos
query = text("SELECT * FROM tratamento t JOIN cobranca c ON t.id = c.tratamento_id")
result = session.execute(query)
for row in result:
    print(row)

# 8 Listar todos os pokémons e seus treinadores
query = text("SELECT * FROM pokemon p JOIN treinador t ON p.treinador_cpf = t.cpf")
result = session.execute(query)
for row in result:
    print(row)

# 9 Listar os funcionários que trabalham no mesmo centro
query = text("SELECT COUNT(funcionario_cpf) num_func, centro_id FROM funcionario_has_centro GROUP BY centro_id ORDER BY num_func DESC")
result = session.execute(query)
for row in result:
    print(row)

# 10 Listar quantos tratamentos cada funcionário fez
query = text("SELECT COUNT(id) qtd_trat, funcionario_cpf FROM tratamento GROUP BY funcionario_cpf ORDER BY qtd_trat")
result = session.execute(query)
for row in result:
    print(row)

# 11 Listar os tratamentos e seus respectivos pokémons
query = text("SELECT * FROM tratamento t JOIN pokemon p ON t.pokemon_id = p.id")
result = session.execute(query)
for row in result:
    print(row)

# 12 Listar os tratamentos e seus respectivos funcionários
query = text("SELECT * FROM tratamento t JOIN funcionario f ON t.funcionario_cpf = f.cpf")
result = session.execute(query)
for row in result:
    print(row)

# 13 Listar todos os cartões e seus treinadores
query = text("SELECT * FROM cartao c JOIN treinador t ON c.treinador_cpf = t.cpf")
result = session.execute(query)
for row in result:
    print(row)

# 14 Listar os pokémons por ordem de mais tratamentos
query = text("SELECT COUNT(id) qtd_trat, pokemon_id FROM tratamento GROUP BY pokemon_id ORDER BY qtd_trat DESC")
result = session.execute(query)
for row in result:
    print(row)

# 15 Listar os pokémons por número de Pokedex
query = text("SELECT * FROM pokemon ORDER BY n_pokedex ASC")
result = session.execute(query)
for row in result:
    print(row)

# 16 Listar os treinadores por idade
query = text("SELECT *, TIMESTAMPDIFF(YEAR, data_nasc, CURRENT_TIMESTAMP) idade FROM treinador ORDER BY idade")
result = session.execute(query)
for row in result:
    print(row)

# 17 Listar os treinadores por maior número de tratamentos
query = text("SELECT COUNT(id) qtd_trat, treinador_cpf FROM tratamento GROUP BY treinador_cpf ORDER BY qtd_trat")
result = session.execute(query)
for row in result:
    print(row)

# 18 Listar e juntar os treinadores que têm a mesma idade
query = text("SELECT COUNT(cpf) qtd_idades, TIMESTAMPDIFF(YEAR, data_nasc, CURRENT_TIMESTAMP) idade FROM treinador GROUP BY idade ORDER BY idade")
result = session.execute(query)
for row in result:
    print(row)

# 19 Listar e juntar os cartões que têm a mesma quantidade de insígnias
query = text("select count(treinador_cpf) qtd_trei_insig, qtd_insignias from cartao group by qtd_insignias order by qtd_insignias desc")
result = session.execute(query)
for row in result:
    print(row)

# 20 Listar os produtos por quantidade
query = text("SELECT * FROM produto ORDER BY quantidade DESC")
result = session.execute(query)
for row in result:
    print(row)

session.close()
