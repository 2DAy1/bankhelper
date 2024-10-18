from sqlalchemy import ForeignKey, String, BigInteger, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from config import DB_URL

# Створюємо асинхронний двигун з asyncpg
engine = create_async_engine(DB_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

# Базовий клас
class Base(AsyncAttrs, DeclarativeBase):
    pass

# Таблиця User
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)  # Telegram ID
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    second_name: Mapped[str] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=True)

    # Відношення з таблицею Credit
    credits: Mapped[list["Credit"]] = relationship(back_populates="user")

# Таблиця Manager
class Manager(Base):
    __tablename__ = 'managers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)  # Telegram ID
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=True)

# Таблиця Credit
class Credit(Base):
    __tablename__ = 'credits'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    amount: Mapped[float] = mapped_column(nullable=False)  # Сума кредиту
    status: Mapped[str] = mapped_column(String(50), nullable=False)  # Статус кредиту, наприклад "активний" або "погашений"
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)  # ForeignKey до таблиці User

    # Відношення з таблицею User
    user: Mapped["User"] = relationship(back_populates="credits")

# Створення таблиць у базі даних
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
