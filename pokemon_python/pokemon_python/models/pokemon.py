from models import Base
from sqlalchemy import DATETIME, VARCHAR, CHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import TINYINT
from datetime import datetime

class Pokemon(Base):
    __tablename__ = "pokemon"
    id: Mapped[int] = mapped_column("id", nullable=False, autoincrement=True, primary_key=True, unique=True)
    nome: Mapped[str] = mapped_column("nome", VARCHAR(50), nullable=False)
    sexo: Mapped[str] = mapped_column("sexo", CHAR(1), nullable=False)
    n_pokedex: Mapped[int] = mapped_column("n_pokedex", TINYINT, nullable=False)
    tipo: Mapped[str] = mapped_column("tipo", VARCHAR(50), nullable=False)
    treinador_cpf: Mapped[str] = mapped_column("treinador_cpf", ForeignKey("treinador.cpf"))
    created_at: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())