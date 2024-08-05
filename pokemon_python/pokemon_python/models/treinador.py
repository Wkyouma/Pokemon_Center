from models import Base
from sqlalchemy import DATETIME, DATE, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, date

class Treinador(Base):
    __tablename__ = "treinador"
    cpf: Mapped[str] = mapped_column("cpf", VARCHAR(11), nullable=False, unique=True, primary_key=True)
    rg: Mapped[str] = mapped_column("rg", VARCHAR(10), nullable=False, unique=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    telefone: Mapped[str] = mapped_column("telefone", VARCHAR(12), nullable=False, unique=True)
    data_nasc: Mapped[date] = mapped_column("data_nasc", DATE, nullable=False)
    estado: Mapped[str] = mapped_column("estado", VARCHAR(45), nullable=False)
    cidade: Mapped[str] = mapped_column("cidade", VARCHAR(45), nullable=False)
    bairro: Mapped[str] = mapped_column("bairro", VARCHAR(45), nullable=False)
    rua: Mapped[str] = mapped_column("rua", VARCHAR(45), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())