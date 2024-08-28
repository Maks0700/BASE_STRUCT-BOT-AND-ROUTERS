from aiogram.types import Message
from aiogram.filters import BaseFilter,CommandObject
from typing import Any

class CheckDigit(BaseFilter):
    async def __call__(self, message: Message, **data: Any) -> bool: #Method call is make class of calling others modules
        command:CommandObject=data.get("command") #extract command because commandobject is dictionary
        arg=command.args #arguments which is keeping in the command thanks to CommandObject
        if (arg.isnumeric()) or (arg.count(".")==1 and arg.replace("."," ").isnumeric()):#checking merely
            return True
        return False
    
    
    
        