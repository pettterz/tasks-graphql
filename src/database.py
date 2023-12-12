from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infra.repository.models import Base


SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/tasks.db'


class DatabaseContext:
    def initialize(self):

        engine = create_engine(
            SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False},
            echo=True
        )

        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=engine)
        # Base = mapper_registry.generate_base()
        Base.metadata.create_all(bind=engine)


database_context = DatabaseContext()


def get_db():
    """
    Get database

    Yields:
        SessionLocal: Local session for database connection
    """
    db = database_context.SessionLocal()
    try:
        yield db
    finally:
        db.close()
