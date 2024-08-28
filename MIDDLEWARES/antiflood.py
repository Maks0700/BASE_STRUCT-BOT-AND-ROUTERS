from typing import Dict,Any,Callable,Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from cachetools import  TTLCache


class Antiflood(BaseMiddleware): 
    def __init__(self,time_limit:int) -> None:
        self.limit=TTLCache(maxsize=10_000,ttl=time_limit) # the book 10_000 pages,on every page keep only chat
        
    async def __call__(self, handler: Callable[[Message, 
                                                Dict[str, Any]], 
                                               Awaitable[Any]], 
                       event: Message, 
                       data: Dict[str, Any]) -> Any:
        if event.chat.id in self.limit:
            return
        else:
            self.limit[event.chat.id]=None
        return await handler(event,data)
    
        
        
        
        
