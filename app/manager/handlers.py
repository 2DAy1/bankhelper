from aiogram import types, Router, F
from aiogram.filters import Command

from app.db.request import add_new_manager
import app.manager.keyboards as kb

router = Router()




@router.message(Command(commands=["addmanager"]))
async def add_manager_command(message: types.Message):
    await message.answer("Будь ласка, поділіться своїм контактом для реєстрації як менеджера.", reply_markup=kb.get_number)



