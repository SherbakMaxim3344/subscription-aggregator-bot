from aiogram.types import Message
from aiogram.filters import BaseFilter

from src.core.config_db import settings

admins = settings.ADMINS
if isinstance(admins, int):
    admins = [admins]

class IsAdmin(BaseFilter):
    def __init__(self, user_ids: int | list[int]) -> None:
        self.user_ids=user_ids

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.user_ids, int):
            return message.from_user.id == self.user_ids
        return message.from_user.id in self.user_ids
