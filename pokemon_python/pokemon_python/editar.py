from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session
from models import *
from urllib.parse import quote

engine = create_engine(f"mysql+pymysql://root:{quote('Adjjadj7@')}@localhost:3306/pokemonzinho")

session = Session(bind=engine)

def atualizar_treinador():
    condicao = Treinador.telefone == '998690267'
    novos_valores = {
        Treinador.telefone: '041998690267',
    }
    consulta_atualizacao = update(Treinador).where(condicao).values(novos_valores)
    session.execute(consulta_atualizacao)
    session.commit()

def atualizar_produto():
    condicao = Produto.id == 3
    novos_valores = {
        Produto.quantidade: '100',
    }
    consulta_atualizacao = update(Produto).where(condicao).values(novos_valores)
    session.execute(consulta_atualizacao)
    session.commit()

def atualizar_pokemon():
    condicao = Pokemon.id == 3
    novos_valores = {
        Pokemon.nome: 'Blastoise',
    }
    consulta_atualizacao = update(Pokemon).where(condicao).values(novos_valores)
    session.execute(consulta_atualizacao)
    session.commit()

def atualizar_funcionario():
    condicao = Funcionario.nome == 'Sergio'
    novos_valores = {
        Funcionario.nome: 'Isadora',
        Funcionario.salario: 2300.00,
    }
    consulta_atualizacao = update(Funcionario).where(condicao).values(novos_valores)
    session.execute(consulta_atualizacao)
    session.commit()

def atualizar_cartao():
    condicao = Cartao.treinador_cpf == '06592397950'
    novos_valores = {
        Cartao.qtd_vitorias: '136',
        Cartao.qtd_insignias: '3',
    }
    consulta_atualizacao = update(Cartao).where(condicao).values(novos_valores)
    session.execute(consulta_atualizacao)
    session.commit()

atualizar_treinador()
atualizar_produto()
atualizar_pokemon()
atualizar_funcionario()
atualizar_cartao()

session.close()