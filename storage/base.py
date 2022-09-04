from environ import Env
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

env = Env(DEBUG=(bool, False))
Env.read_env('../.env')


db_login = env('DB_LOGIN', default='SECRET')
db_password = env('DB_PASSWORD', default='SECRET')
db_path = env('DB_PATH', default='SECRET')

engine = create_engine(f'postgresql://{db_login}:{db_password}@{db_path}:5432')
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()


if __name__ == '__main__':
    with session_factory() as session:
        print(1)
