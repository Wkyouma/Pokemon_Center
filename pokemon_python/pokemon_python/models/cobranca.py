from models import Base
from sqlalchemy import DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Cobranca(Base):
    __tablename__ = "cobranca"
    tratamento_id: Mapped[int] = mapped_column("tratamento_id", ForeignKey("tratamento.id"), primary_key=True, unique=True)
    data_hora: Mapped[datetime] = mapped_column("data_hora", DATETIME, nullable=False, default=datetime.now())