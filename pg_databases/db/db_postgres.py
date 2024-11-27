from databases import Database
import dotenv
from sqlalchemy import ARRAY, Column, Integer, MetaData, String, Table, create_engine

CFG = dotenv.dotenv_values("../.env")
engine = create_engine(CFG['SQLALCHEMY_DATABASE_URL'])
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(CFG['SQLALCHEMY_DATABASE_URL'])