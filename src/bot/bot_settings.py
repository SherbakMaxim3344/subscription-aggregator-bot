from aiogram import Bot
from aiogram.types import BotCommand

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="menu", description="Показать меню"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="vip", description="VIP"),
        BotCommand(command="profile", description="Просмотр профиля"),
        BotCommand(command="share_profile", description="Поделится статистикой профиля"),
        BotCommand(command="settings", description="Настройки")
    ]
    await bot.set_my_commands(commands)
