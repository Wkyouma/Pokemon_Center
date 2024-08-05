from models import Base
from sqlalchemy import DATETIME, CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import TINYINT
from datetime import datetime
from typing import List

class Loja(Base):
    __tablename__ = "loja"
    id: Mapped[int] = mapped_column("id", nullable=False, autoincrement=True, primary_key=True, unique=True)
    cnpj_loja: Mapped[str] = mapped_column("cnpj_loja", CHAR(14), nullable=False, unique=True, primary_key=True)
    num_maquinas: Mapped[int] = mapped_column("num_maquinas", TINYINT, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    # loja_tipo: Mapped[List["Loja"]] = relationship(secondary="Centro_has_produto", back_populates='produto')
    # loja_funcionario: Mapped[List["Loja"]] = relationship(secondary="Funcionario_has_centro", back_populates='funcionario')
    # loja_tratamento: Mapped[List["Loja"]] = relationship(secondary="Tratamento_has_Centro", back_populates='tratamento')
    