from aiogram.fsm.state import State, StatesGroup


class Login(StatesGroup):
    number = State()
    confirmation = State()