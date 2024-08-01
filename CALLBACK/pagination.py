from aiogram import F,Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery
from KEYBOARDS import fabrick
from contextlib import suppress
from DATA.subloader import get_json
router=Router()




@router.callback_query(fabrick.Pagination.filter(F.action.in_(["prev","next"])))
async def process(call:CallbackQuery,callback_data:fabrick.Pagination):
    smiles=await get_json()
    page_num=int(callback_data.page)
    page_main=page_num-1 if page_num>0 else 0
    if callback_data.action=="next":
        
        page_main=page_num+1 if page_num<(len(smiles)-1) else page_num
    with suppress(TelegramBadRequest):
        await call.message.edit_text(f"{smiles[page_main][0]} {smiles[page_main][1]}",reply_markup=fabrick.paginator(page=page_main))    
    await call.answer("All good, don't worry!!")


