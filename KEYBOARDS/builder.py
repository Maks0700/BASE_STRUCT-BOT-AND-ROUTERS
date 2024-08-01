from aiogram.utils.keyboard import ReplyKeyboardBuilder



def button_calculator()->ReplyKeyboardBuilder:
    builder=ReplyKeyboardBuilder()
    items=[
        "1","2","3","/",
        "4","5","6","*",
        "7","8","9","-",
        "0",".","=","+",

    ]    
    [builder.button(text=item) for item in items]
    
    builder.adjust(*[4]*4)
    return builder.as_markup()