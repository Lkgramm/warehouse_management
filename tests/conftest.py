import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from infrastructure.orm import Base
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork


@pytest.fixture(scope="function")
def session() -> Session:
    # Создаем временную БД в памяти
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture
def uow(session):
    return SqlAlchemyUnitOfWork(session)