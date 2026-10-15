from src.core.config_db import settings

admins = settings.ADMINS
if isinstance(admins, int):
    admins = [admins]
