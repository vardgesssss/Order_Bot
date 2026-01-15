from aiogram.fsm.state import StatesGroup, State


class CheckoutState(StatesGroup):
    delivery_method = State()
    delivery_date = State()
    delivery_time = State()
    full_name = State()
    phone = State()
    address = State()
    comment = State()


class PaymentState(StatesGroup):
    confirm = State()
