from aiogram import Router

from aiogram.types import Message

router = Router()

@router.message()
async def start(msg: Message):
    await msg.answer("Привет, бот всё ещё находится в разработке"
                        "Вся дополнительная информация в канале:"
                        "@stalker_roleplaybot_chanell")