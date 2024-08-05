from models import Base
from sqlalchemy import DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import DECIMAL
from datetime import datetime
from typing import List

class Tratamento(Base):
    __tablename__ = "tratamento"
    id: Mapped[int] = mapped_column("id", nullable=False, autoincrement=True, primary_key=True, unique=True)
    data_hora: Mapped[datetime] = mapped_column("data_hora", DATETIME, nullable=False, default=datetime.now())
    valor: Mapped[str] = mapped_column("valor", DECIMAL(10,2), nullable=False)
    treinador_cpf: Mapped[str] = mapped_column("treinador_cpf", ForeignKey("treinador.cpf"))
    funcionario_cpf: Mapped[str] = mapped_column("funcionario_cpf", ForeignKey("funcionario.cpf"))
    created_at: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    pokemon_id: Mapped[int] = mapped_column("pokemon_id", ForeignKey("pokemon.id"))
    # tratamento_loja: Mapped[List["Tratamento"]] = relationship(secondary="Tratamento_has_Centro", back_populates='loja')
    