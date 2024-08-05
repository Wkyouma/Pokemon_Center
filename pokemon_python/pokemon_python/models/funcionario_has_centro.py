from models import Base
from sqlalchemy import DATETIME, CHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import TINYINT
from datetime import datetime



class Funcionario_has_centro(Base):
    __tablename__ = "funcionario_has_centro"
    centro_id:Mapped[int] = mapped_column("centro_id", ForeignKey("loja.id"), primary_key=True)
    funcionario_cpf:Mapped[str] = mapped_column("funcionario_cpf", ForeignKey("funcionario.cpf"), primary_key=True)
    # funcionario = relationship("Funcionario", back_populates="funcionario_loja")