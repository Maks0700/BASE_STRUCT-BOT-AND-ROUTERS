from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command,CommandObject
from KEYBOARDS import reply_keyboards 
from FILTERS.is_admin import IsAdmin
from FILTERS.check_is_digit import CheckDigit
router=Router()

@router.message(CommandStart(),IsAdmin(5528071947))
async def greeting(message:Message):
    await message.answer(f"Welcome to my bot, dear {message.from_user.first_name}",reply_markup=reply_keyboards.main_keyboard())
    
@router.message(Command("pay"),CheckDigit())
async def check_digit_or_float(message:Message,command:CommandObject):
    
    await message.answer(f"hello {command.args}")
    
    