from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


def links_keyboard()->InlineKeyboardMarkup:
    keyboard_links=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="YouTube",url="https://www.youtube.com")
                
            ],
            [
                InlineKeyboardButton(text="Vkontakte",url="https://vk.com/feed")
            ]
            
            ]
        )
    return keyboard_links
