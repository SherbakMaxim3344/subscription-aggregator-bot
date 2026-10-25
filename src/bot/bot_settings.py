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
        BotCommand(command="settings", description="Настройки"),
        BotCommand(command="add_subscription", description="Добавить подписку"),
        BotCommand(command="subscriptions", description="Посмотреть ваши подписки"),
        BotCommand(command="info", description="О нас"),
        BotCommand(command="delete_subscription", description="удаление подписки"),
        BotCommand(command="delete_all_subscriptions", description="удалить все подписки"),
    ]
    await bot.set_my_commands(commands)
