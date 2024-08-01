from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from KEYBOARDS import reply_keyboards 

router=Router()

@router.message(CommandStart())
async def greeting(message:Message):
    await message.answer(f"Welcome to my bot, dear {message.from_user.first_name}",reply_markup=reply_keyboards.main_keyboard())
