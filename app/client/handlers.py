from aiogram import types, Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from sqlalchemy import select

from app.db.models import async_session, User
from app.db.request import get_user_by_phone, add_new_user, get_manager_by_phone
from app.client.states import Login
import app.client.keyboards as kb


router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    await state.set_state(Login.number)
    await message.answer("Вітаю! Щоб продовжити, будь ласка, поділіться своїм контактом.",reply_markup=kb.get_number)


@router.message(Login.number, F.contact)
async def login_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    contact = data['number']

    manager = await get_manager_by_phone(contact)

    if manager:

        await message.answer(f"Вітаємо, {manager.first_name}! Ви увійшли як менеджер.")
    else:
        user = await get_user_by_phone(contact)

        if user:
            await message.answer(f"Вітаємо, {user.first_name}! Ви вже зареєстровані.")
        else:
            await register_user(message, contact)

    await state.clear()

async def register_user(message: types.Message, contact:str):
    tg_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    await add_new_user(tg_id, contact, first_name, last_name, username)
    await message.answer("Ви успішно зареєстровані!")
