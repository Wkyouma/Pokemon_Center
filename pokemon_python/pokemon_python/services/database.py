from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import quote

instance = f"mysql+pymysql://root:{quote('Adjjadj7@')}@localhost:3306/pokemonzinho"

if not database_exists(instance):
    create_database(instance)

engine = create_engine(url=instance, echo=True)
session = Session(bind=engine, autocommit=False, autoflush=True)