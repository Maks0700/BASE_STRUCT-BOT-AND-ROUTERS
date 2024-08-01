#The need for load for json file (smiles.py)
import os
from ujson import loads
import aiofiles


async def get_json():
    # path=f"DATA/{filename}"
    # if os.path.exists(path):
        async with aiofiles.open("C:\Aiogram3_Bot\DATA\smiles.json","r",encoding="utf-8") as file:
            return loads(await file.read())
            
    
