from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from config import DATABASE_URI
from sqlalchemy import Table, Column, Integer, String, MetaData


engine = create_engine(DATABASE_URI)
if not database_exists(engine.url):
    create_database(engine.url)

meta = MetaData()

ads_table = Table(
    'ads', meta,
    Column('id', Integer, primary_key=True),
    Column('image', String),
    Column('title', String),
    Column('date', String),
    Column('location', String),
    Column('beds', String),
    Column('description', String),
    Column('price', String),
    Column('currency', String),
)
meta.create_all(engine)

