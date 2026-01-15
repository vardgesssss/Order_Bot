import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

MANAGER_CHAT_ID_RAW = os.getenv("MANAGER_CHAT_ID")
MANAGER_CHAT_ID = int(MANAGER_CHAT_ID_RAW) if MANAGER_CHAT_ID_RAW not in (None, "") else None

ENABLE_ORDER_NOTIFICATIONS = os.getenv("ENABLE_ORDER_NOTIFICATIONS", "true").lower() == "true"
ORDER_NOTIFICATION_TEMPLATE = os.getenv("ORDER_NOTIFICATION_TEMPLATE", "default")

CARD_NUMBER = "2202 2080 9748 5529"
ENABLE_CARD_PAYMENTS = True

BAKER_SCHEDULE_START_DATE = os.getenv("BAKER_SCHEDULE_START_DATE", "2025-01-01")

WORK_CYCLE_ON_DAYS = int(os.getenv("WORK_CYCLE_ON_DAYS", "2"))
WORK_CYCLE_OFF_DAYS = int(os.getenv("WORK_CYCLE_OFF_DAYS", "2"))

WORKING_HOURS_START = int(os.getenv("WORKING_HOURS_START", "10"))
WORKING_HOURS_END = int(os.getenv("WORKING_HOURS_END", "20"))

SLOT_MINUTES = int(os.getenv("SLOT_MINUTES", "60"))

MIN_LEAD_HOURS = int(os.getenv("MIN_LEAD_HOURS", "24"))

MAX_DAYS_AHEAD = int(os.getenv("MAX_DAYS_AHEAD", "14"))

WELCOME_EFFECT_ID = os.getenv("WELCOME_EFFECT_ID", "5159385139981059251")

if not BOT_TOKEN:
    raise RuntimeError("Не задан токен бота. Укажите BOT_TOKEN в .env или переменных окружения.")

print(f"Конфигурация загружена:")
print(f"- BOT_TOKEN: {'*' * len(BOT_TOKEN) if BOT_TOKEN else 'НЕ ЗАДАН'}")
print(f"- MANAGER_CHAT_ID: {MANAGER_CHAT_ID or 'НЕ ЗАДАН'}")
print(f"- Уведомления о заказах: {'ВКЛЮЧЕНЫ' if ENABLE_ORDER_NOTIFICATIONS else 'ОТКЛЮЧЕНЫ'}")
print(f"- Оплата на карту: {'ВКЛЮЧЕНА' if ENABLE_CARD_PAYMENTS else 'ОТКЛЮЧЕНА'}")
print(f"- Номер карты: {CARD_NUMBER}")
print("- Предзаказ и расписание:")
print(f"  • База цикла: {BAKER_SCHEDULE_START_DATE}")
print(f"  • Цикл: {WORK_CYCLE_ON_DAYS} на / {WORK_CYCLE_OFF_DAYS} от")
print(f"  • Часы: {WORKING_HOURS_START}:00–{WORKING_HOURS_END}:00, слот {SLOT_MINUTES} мин")
print(f"  • Минимальный срок: {MIN_LEAD_HOURS} ч, горизонт: {MAX_DAYS_AHEAD} дней")
print(f"- Эффект приветствия: {'ЗАДАН' if WELCOME_EFFECT_ID else 'не задан'}")
