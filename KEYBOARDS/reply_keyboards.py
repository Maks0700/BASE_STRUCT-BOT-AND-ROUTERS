from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,KeyboardButtonPollType)

def main_keyboard()->ReplyKeyboardMarkup:
    keyboard=ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Smiles"),
            KeyboardButton(text="Links")
        ],
                  [
                      KeyboardButton(text="Calculations"),
                      KeyboardButton(text="Special buttons")
                  ]
                  
                  ],
        resize_keyboard=True,
        selective=True,
        input_field_placeholder="Write message!!!",
        one_time_keyboard=True
    
    )
    return keyboard




def special_buttons()->ReplyKeyboardMarkup:
    keyboard_special_buttons=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="My location",request_location=True)
            ],
            [
                KeyboardButton(text="My contact",request_contact=True)
                
                ],
            [
                KeyboardButton(text="Poll",request_poll=KeyboardButtonPollType())
            ]
        ],
        selective=True,
        one_time_keyboard=True,
        resize_keyboard=True
    )
    return keyboard_special_buttons
