from models import Base
from sqlalchemy import DATETIME, DATE, VARCHAR, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date
from typing import List

class Funcionario(Base):
    __tablename__ = "funcionario"
    cpf: Mapped[str] = mapped_column("cpf", VARCHAR(11), nullable=False, unique=True, primary_key=True)
    rg: Mapped[str] = mapped_column("rg", VARCHAR(10), nullable=False, unique=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    salario: Mapped[float] = mapped_column("salario", DECIMAL(10,2), nullable=False)
    data_nasc: Mapped[date] = mapped_column("data_nasc", DATE, nullable=False)
    funcao: Mapped[str] = mapped_column("funcao", VARCHAR(50), nullable=False)
    estado: Mapped[str] = mapped_column("estado", VARCHAR(45), nullable=False)
    cidade: Mapped[str] = mapped_column("cidade", VARCHAR(45), nullable=False)
    bairro: Mapped[str] = mapped_column("bairro", VARCHAR(45), nullable=False)
    rua: Mapped[str] = mapped_column("rua", VARCHAR(45), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    # funcionario_loja: Mapped[List["Funcionario"]] = relationship(secondary="Funcionario_has_centro", back_populates='funcionario')