from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.db.models import async_session, User, Manager


async def get_user_by_phone(phone_number: str):
    async with async_session() as session:
        async with session.begin():
            query = select(User).where(User.phone_number == phone_number).options(selectinload(User.credits))
            result = await session.execute(query)
            user = result.scalars().first()
            return user



async def add_new_user(tg_id: int, phone_number: str, first_name: str, last_name: str, username: str):
    async with async_session() as session:
        async with session.begin():
            new_user = User(
                tg_id=tg_id,
                first_name=first_name or None,
                last_name=last_name or None,
                phone_number=phone_number,
                username=username or None
            )
            session.add(new_user)
            await session.commit()

async def get_manager_by_phone(phone_number: str):
    async with async_session() as session:
        async with session.begin():
            query = select(Manager).where(Manager.phone_number == phone_number)
            result = await session.execute(query)
            manager = result.scalars().first()
            return manager


# Функція для додавання нового менеджера
async def add_new_manager(tg_id: int, phone_number: str, first_name: str, last_name: str, username: str):
    async with async_session() as session:
        async with session.begin():
            new_manager = Manager(
                tg_id=tg_id,
                first_name=first_name or None,
                last_name=last_name or None,
                phone_number=phone_number,
                username=username or None
            )
            session.add(new_manager)
            await session.commit()
