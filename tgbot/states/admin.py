from aiogram.fsm.state import State, StatesGroup


class Admin(StatesGroup):
    text = State()
