from aiogram import Router,F
from aiogram.types import Message
from KEYBOARDS import inline_keyboards,reply_keyboards,fabrick,builder
from DATA.subloader import get_json
from CALLBACK import pagination

router=Router()


@router.message(F.text.in_(["Links"]))
async def proceess_message(message:Message):
    await message.answer("Your Links",reply_markup=inline_keyboards.links_keyboard())
    

@router.message(F.text.in_(["Special buttons"]))
async def proceess_message(message:Message):
    await message.answer("Your special buttons",reply_markup=reply_keyboards.special_buttons())



@router.message(F.text.in_(["Calculations"]))
async def proceess_message(message:Message):
    await message.answer("Your Calculator",reply_markup=builder.button_calculator())
    
@router.message(F.text.in_(["Smiles"]))
async def proceess_message(message:Message):
    smiles=await get_json()
    await message.answer(f"{smiles[0][0]} {smiles[0][1]}",reply_markup=fabrick.paginator(page=0))




