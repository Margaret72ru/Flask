import atexit
from sqlalchemy import Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

PDSN = f'postgresql://app:secret@127.0.0.1:5431/app'
engine = create_engine(PDSN)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class AdvertisementModel(Base):
    __tablename__ = 'advertisements'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(nullable=False)
    owner: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(String)


Base.metadata.create_all(bind=engine)

atexit.register(lambda: engine.dispose())