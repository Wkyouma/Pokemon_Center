from models import Base
from sqlalchemy import DATETIME, VARCHAR, INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import DECIMAL
from datetime import datetime
from typing import List

class Produto(Base):
    __tablename__ = "produto"
    id: Mapped[int] = mapped_column("id", nullable=False, autoincrement=True, primary_key=True, unique=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    quantidade: Mapped[int] = mapped_column("quantidade", INTEGER, nullable=False)
    preco: Mapped[float] = mapped_column("preco", DECIMAL(8,2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    # loja_tipo: Mapped[List["Produto"]] = relationship(secondary="Centro_has_produto", back_populates='loja')