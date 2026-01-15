from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from datetime import datetime
from .catalog import CATALOG, Cake


def main_menu_kb(user_id: int = None) -> ReplyKeyboardMarkup:
    if user_id is not None:
        try:
            from main import CARTS
            cart_items = sum(CARTS.get(user_id, {}).values())
            if cart_items > 0:
                button_text = f"🛒 Корзина ({cart_items})"
            else:
                button_text = "🛒 Корзина"
        except:
            button_text = "🛒 Корзина"
    else:
        button_text = "🛒 Корзина"
    
    keyboard = [
        [KeyboardButton(text="🍰 Каталог"), KeyboardButton(text=button_text)],
        [KeyboardButton(text="⭐ Отзывы")]
    ]
    
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


def catalog_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for cake in CATALOG:
        builder.button(text=f"{cake.name} — {cake.price}₽", callback_data=f"cake:{cake.id}")
    builder.adjust(1)
    builder.button(text="⬅️ Назад", callback_data="back:main")
    return builder.as_markup()


def cake_card_kb(cake: Cake, user_id: int = None) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    
    if user_id is not None:
        from .catalog import get_cake_by_id
        current_qty = 0
        try:
            from main import CARTS
            current_qty = CARTS.get(user_id, {}).get(cake.id, 0)
        except:
            pass
        
        if current_qty > 0:
            button_text = f"➕ В корзину ({current_qty})"
        else:
            button_text = "➕ В корзину"
    else:
        button_text = "➕ В корзину"
    
    builder.button(text=button_text, callback_data=f"add:{cake.id}")
    builder.button(text="⬅️ К каталогу", callback_data="back:catalog")
    builder.button(text="🛒 Открыть корзину", callback_data="open:cart")
    builder.adjust(1)
    return builder.as_markup()


def cart_kb(has_items: bool) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if has_items:
        builder.button(text="🧹 Очистить", callback_data="cart:clear")
        builder.button(text="✅ Оформить заказ", callback_data="cart:checkout")
    builder.button(text="⬅️ К каталогу", callback_data="back:catalog")
    return builder.as_markup()


def order_confirmation_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="💳 Оплатить заказ", callback_data="payment:start")
    builder.button(text="⬅️ Назад к корзине", callback_data="back:cart")
    builder.adjust(1)
    return builder.as_markup()


def payment_confirm_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Платёж выполнен", callback_data="payment:confirm")
    builder.button(text="❌ Отменить", callback_data="payment:cancel")
    builder.adjust(1)
    return builder.as_markup()


def delivery_method_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="🚶 Самовывоз", callback_data="delivery:самовывоз")
    builder.button(text="🚚 Доставка", callback_data="delivery:доставка")
    builder.button(text="⬅️ К корзине", callback_data="back:cart")
    builder.adjust(1)
    return builder.as_markup()


def dates_kb(date_items: list[str]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for d in date_items:
        try:
            y, m, day = [int(x) for x in d.split("-")]
            label = f"{day:02d}.{m:02d}.{y}"
        except Exception:
            label = d
        builder.button(text=label, callback_data=f"date:{d}")
    builder.button(text="⬅️ Назад", callback_data="back:delivery")
    builder.adjust(1)
    return builder.as_markup()


def time_slots_kb(date_str: str, slot_items: list[str]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for t in slot_items:
        builder.button(text=t, callback_data=f"time:{t}|{date_str}")
    builder.button(text="⬅️ Назад", callback_data="back:dates")
    builder.adjust(2)
    return builder.as_markup()
