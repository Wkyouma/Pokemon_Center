from models import Base
from sqlalchemy import ForeignKey, INTEGER
from sqlalchemy.orm import Mapped, mapped_column

class Cartao(Base):
    __tablename__ = "cartao"
    treinador_cpf: Mapped[str] = mapped_column("treinador_cpf", ForeignKey("treinador.cpf"), primary_key=True)
    qtd_pokemon: Mapped[int] = mapped_column("qtd_pokemon", INTEGER, nullable=False)
    qtd_vitorias: Mapped[int] = mapped_column("qtd_vitorias", INTEGER, nullable=False)
    qtd_insignias: Mapped[int] = mapped_column("qtd_insignias", INTEGER, nullable=False)
    