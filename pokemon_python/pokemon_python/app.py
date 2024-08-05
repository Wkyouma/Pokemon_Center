from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session
from models import *
from urllib.parse import quote

engine = create_engine(f"mysql+pymysql://root:{quote('Adjjadj7@')}@localhost:3306/pokemonzinho")

session = Session(bind=engine)
inserts1 = [
    insert(Treinador).values(cpf='06592398922', rg='378578340', nome='Jonas', telefone='998690267', data_nasc='1997-10-17', estado='parana', cidade='colombo', bairro='guaraituba', rua='leonidas alberti'),
    insert(Treinador).values(cpf='07880563954', rg='8546982', nome='Gabriel', telefone='9999999999', data_nasc='2005-05-07', estado='parana', cidade='curitiba', bairro='boqueirão', rua='oliveira viana'),
    insert(Treinador).values(cpf='13302978901', rg='888888888', nome='Igor', telefone='91246140', data_nasc='2004-10-30', estado='parana', cidade='curitiba', bairro='juveve', rua='conselheiro carrão'),
    insert(Treinador).values(cpf='04431381252', rg='777777777', nome='Antonio', telefone='981024233', data_nasc='2005-04-26', estado='parana', cidade='curitiba', bairro='boqueirão', rua='salvador ferrante'),
    insert(Treinador).values(cpf='01234567891', rg='666666666', nome='Marcelly', telefone='985201478', data_nasc='2000-05-24', estado='são paulo', cidade='santos', bairro='centro', rua='avenida brasil'),
    insert(Treinador).values(cpf='06592397950', rg='578346589', nome='Jonatas', telefone='999160029', data_nasc='1991-12-04', estado='são paulo', cidade='são bernardo do campo', bairro='centro', rua='marechal deodoro'),
    insert(Pokemon).values(nome='Empoleon', sexo='M', n_pokedex='114', tipo='agua e aço', treinador_cpf='06592398922'),
    insert(Pokemon).values(nome='Lucario', sexo='M', n_pokedex='123', tipo='lutador e aço', treinador_cpf='07880563954'),
    insert(Pokemon).values(nome='Zoruark', sexo='M', n_pokedex='002', tipo='sombrio', treinador_cpf='04431381252'),
    insert(Pokemon).values(nome='Greninja', sexo='F', n_pokedex='005', tipo='agua e sombrio', treinador_cpf='13302978901'),
    insert(Pokemon).values(nome='Dialga', sexo='M', n_pokedex='009', tipo='aço', treinador_cpf='01234567891'),
    insert(Pokemon).values(nome='Charizard', sexo='F', n_pokedex='007', tipo='fogo e voador', treinador_cpf='06592397950'),
    insert(Produto).values(nome='poção', quantidade='99', preco='100'),
    insert(Produto).values(nome='reviver', quantidade='99', preco='300'),
    insert(Produto).values(nome='pokebola', quantidade='99', preco='50'),
    insert(Produto).values(nome='antidodo', quantidade='99', preco='75'),
    insert(Produto).values(nome='repelente', quantidade='99', preco='50'),
    insert(Produto).values(nome='bicicleta', quantidade='10', preco='1000'),
    insert(Loja).values(cnpj_loja='13990662000106', num_maquinas='2'),
    insert(Loja).values(cnpj_loja='69306570000100', num_maquinas='2'),
    insert(Loja).values(cnpj_loja='73414826000170', num_maquinas='4'),
    insert(Loja).values(cnpj_loja='19983617000100', num_maquinas='4'),
    insert(Loja).values(cnpj_loja='80085833000131', num_maquinas='6'),
    insert(Loja).values(cnpj_loja='29043459000154', num_maquinas='6'),
    insert(Funcionario).values(cpf='57691346077', rg='1111111111', nome='Leila', salario='2300.00', data_nasc='2001-05-26', funcao='atendente', estado='parana', cidade='curitiba', bairro='centro', rua='XV de novembro'),
    insert(Funcionario).values(cpf='24263941020', rg='2222222222', nome='Sergio', salario='2300.00', data_nasc='2000-10-08', funcao='atendente', estado='parana', cidade='curitiba', bairro='agua verde', rua='avenida republica argentina'),
    insert(Funcionario).values(cpf='05649238006', rg='3333333333', nome='Natalia', salario='3700.00', data_nasc='1997-07-12', funcao='gerente', estado='parana', cidade='curitiba', bairro='cabral', rua='rua dos funcionarios'),
    insert(Funcionario).values(cpf='42940957096', rg='4444444444', nome='Cintia', salario='1800.00', data_nasc='2004-04-14', funcao='vendedor', estado='parana', cidade='curitiba', bairro='centro', rua='alameda dr muricy'),
    insert(Funcionario).values(cpf='91343155002', rg='5555555555', nome='Tereza', salario='5500.00', data_nasc='1995-02-03', funcao='coordenador', estado='parana', cidade='curitiba', bairro='batel', rua='alameda princesa izabel'),
    insert(Funcionario).values(cpf='56914592012', rg='6666666666', nome='Akira', salario='7000.00', data_nasc='1991-11-11', funcao='gerente geral', estado='parana', cidade='curitiba', bairro='juveve', rua='augusto stresser'),
    insert(Tratamento).values(valor='150', treinador_cpf='07880563954', funcionario_cpf='57691346077', pokemon_id='1'),
    insert(Tratamento).values(valor='780', treinador_cpf='06592397950', funcionario_cpf='57691346077', pokemon_id='1'),
    insert(Tratamento).values(valor='75', treinador_cpf='01234567891', funcionario_cpf='24263941020', pokemon_id='1'),
    insert(Tratamento).values(valor='50', treinador_cpf='06592398922', funcionario_cpf='42940957096', pokemon_id='1'),
    insert(Tratamento).values(valor='230', treinador_cpf='07880563954', funcionario_cpf='24263941020', pokemon_id='1'),
    insert(Tratamento).values(valor='490', treinador_cpf='06592397950', funcionario_cpf='24263941020', pokemon_id='1'),
    insert(Cartao).values(treinador_cpf='06592398922', qtd_pokemon='6', qtd_vitorias='367', qtd_insignias='8'),
    insert(Cartao).values(treinador_cpf='07880563954', qtd_pokemon='5', qtd_vitorias='124', qtd_insignias='3'),
    insert(Cartao).values(treinador_cpf='13302978901', qtd_pokemon='6', qtd_vitorias='210', qtd_insignias='5'),
    insert(Cartao).values(treinador_cpf='04431381252', qtd_pokemon='6', qtd_vitorias='326', qtd_insignias='7'),
    insert(Cartao).values(treinador_cpf='01234567891', qtd_pokemon='6', qtd_vitorias='652', qtd_insignias='8'),
    insert(Cartao).values(treinador_cpf='06592397950', qtd_pokemon='3', qtd_vitorias='97', qtd_insignias='2')
]

inserts2 = [
    insert(Cobranca).values(tratamento_id='1'),
    insert(Cobranca).values(tratamento_id='2'),
    insert(Cobranca).values(tratamento_id='3'),
    insert(Cobranca).values(tratamento_id='4'),
    insert(Cobranca).values(tratamento_id='5'),
    insert(Cobranca).values(tratamento_id='6'),
    insert(Funcionario_has_centro).values(centro_id='1', funcionario_cpf='24263941020'),
    insert(Funcionario_has_centro).values(centro_id='2', funcionario_cpf='42940957096'),
    insert(Funcionario_has_centro).values(centro_id='3', funcionario_cpf='24263941020'),
    insert(Funcionario_has_centro).values(centro_id='4', funcionario_cpf='57691346077'),
    insert(Funcionario_has_centro).values(centro_id='5', funcionario_cpf='42940957096'),
    insert(Funcionario_has_centro).values(centro_id='6', funcionario_cpf='24263941020'),
    insert(Tratamento_has_centro).values(tratamento_id='2', centro_id='1'),
    insert(Tratamento_has_centro).values(tratamento_id='1', centro_id='2'),
    insert(Tratamento_has_centro).values(tratamento_id='3', centro_id='3'),
    insert(Tratamento_has_centro).values(tratamento_id='4', centro_id='4'),
    insert(Tratamento_has_centro).values(tratamento_id='5', centro_id='5'),
    insert(Tratamento_has_centro).values(tratamento_id='6', centro_id='6'),
	insert(Centro_has_produto).values(centro_id='1', centro_cnpj_loja='13990662000106', produto_id='1'),
    insert(Centro_has_produto).values(centro_id='1', centro_cnpj_loja='69306570000100', produto_id='2'),
    insert(Centro_has_produto).values(centro_id='1', centro_cnpj_loja='73414826000170', produto_id='3'),
    insert(Centro_has_produto).values(centro_id='1', centro_cnpj_loja='19983617000100', produto_id='4'),
    insert(Centro_has_produto).values(centro_id='1', centro_cnpj_loja='80085833000131', produto_id='5'),
    insert(Centro_has_produto).values(centro_id='1', centro_cnpj_loja='29043459000154', produto_id='6')
]

for insert in inserts1:
    session.execute(insert)

session.commit()

for insert in inserts2:
    session.execute(insert)

session.commit()

session.close()