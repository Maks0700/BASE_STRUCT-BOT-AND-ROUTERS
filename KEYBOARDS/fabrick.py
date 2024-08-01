from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton



class Pagination(CallbackData,prefix="page"):
    page:int
    action:str

    

def paginator(page:int=0):
        builder=InlineKeyboardBuilder()
        builder.row(
        InlineKeyboardButton(text="⬅️",callback_data=Pagination(page=page,action="prev").pack()),
        InlineKeyboardButton(text="➡️",callback_data=Pagination(page=page,action="next").pack()),
        width=2
        )
        return builder.as_markup()