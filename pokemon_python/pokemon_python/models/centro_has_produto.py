from models import Base
from sqlalchemy import DATETIME, CHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import TINYINT
from datetime import datetime


class Centro_has_produto(Base):
    __tablename__ = "centro_has_produto"
    centro_id:Mapped[int] = mapped_column("centro_id", ForeignKey("loja.id"), primary_key=True)
    centro_cnpj_loja:Mapped[int] = mapped_column("centro_cnpj_loja", ForeignKey("loja.cnpj_loja"))
    produto_id:Mapped[int] = mapped_column("produto_id", ForeignKey("produto.id"), primary_key=True)
