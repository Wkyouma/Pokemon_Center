from models import Base
from sqlalchemy import DATETIME, CHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import TINYINT
from datetime import datetime



# Tabela intermediária para o relacionamento N-N entre Loja e Produto
class Tratamento_has_centro(Base):
    __tablename__ = "tratamento_has_centro"
    tratamento_id:Mapped[int] = mapped_column("tratamento_id", ForeignKey("tratamento.id"), primary_key=True)
    centro_id:Mapped[int] = mapped_column("centro_id", ForeignKey("loja.id"), primary_key=True)
    
    