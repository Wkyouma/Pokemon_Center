from sqlalchemy import create_engine, delete
from sqlalchemy.orm import Session
from models import *
from urllib.parse import quote

engine = create_engine(f"mysql+pymysql://root:{quote('Adjjadj7@')}@localhost:3306/pokemonzinho")

session = Session(bind=engine)

def deletar_funcionario():
    condicao = Funcionario.nome == 'Akira'
    consulta_exclusao = delete(Funcionario).where(condicao)
    session.execute(consulta_exclusao)
    session.commit()
    print("deletado com sucesso")

def deletar_cartao():
    condicao = Cartao.qtd_insignias > 4
    consulta_exclusao = delete(Cartao).where(condicao)
    session.execute(consulta_exclusao)
    session.commit()

def deletar_treinador():
    condicao = Treinador.cpf == '06592398922'
    consulta_exclusao = delete(Treinador).where(condicao)
    session.execute(consulta_exclusao)
    session.commit()

def deletar_pokemon():
    condicao = Pokemon.id == 2
    consulta_exclusao = delete(Pokemon).where(condicao)
    session.execute(consulta_exclusao)
    session.commit()

def deletar_cobranca():
    condicao = Cobranca.tratamento_id == 2
    consulta_exclusao = delete(Tratamento).where(condicao)
    session.execute(consulta_exclusao)
    session.commit()


def deletar_produto():
    condicao = Produto.id == 2
    consulta_exclusao = delete(Produto).where(condicao)
    session.execute(consulta_exclusao)
    session.commit()



deletar_funcionario()
deletar_cartao()
deletar_treinador()
deletar_pokemon()
deletar_cobranca()
deletar_produto()



session.close()