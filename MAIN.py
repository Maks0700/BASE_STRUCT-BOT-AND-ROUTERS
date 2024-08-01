#Welcome to aiogram 3.10 YEEEEEEEEEEEEEEAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHH
import asyncio
from aiogram import Bot,Dispatcher
import os
from pprint import pprint
from CALLBACK import pagination
from HANDLERS import bot_message__commands,user_commands
from config_reader import config




async def main():
    bot=Bot(config.bot_token.get_secret_value(),parse_mode="Markdown")
    dp=Dispatcher()
    dp.include_routers(
        ####Connect our routers where its exists on packet
        
        user_commands.router,
        pagination.router, 
        bot_message__commands.router
        
    )

    try:
        await bot.delete_webhook(drop_pending_updates=True)# for skip all update
        pprint("Bot is success!!")
        await dp.start_polling(bot)
    except Exception:
        return -1


    
    

if __name__=="__main__":
    asyncio.run(main())