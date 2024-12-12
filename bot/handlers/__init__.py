from aiogram import Dispatcher

# Импорты
from . import other

# Функция подключения роутеров из handlers
async def includer(dp: Dispatcher):
    dp.include_routers(
        other.router
    )