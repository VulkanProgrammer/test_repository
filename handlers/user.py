import os

from aiogram import Bot, F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, LabeledPrice, Message, PreCheckoutQuery

import keyboards.keyboards as kb

user = Router()


@user.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в бот по покупке звёзд.", reply_markup=kb.main
    )


class Stars(
    StatesGroup,
):
    Number_of_stars = State()


@user.callback_query(F.data == "stars")
async def chose_stars(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Stars.Number_of_stars)
    await callback.message.answer(
        "Нажмите на кнопку с нужным кол-вом звёзд:", reply_markup=kb.stars
    )


@user.message(Stars.Number_of_stars)
async def buy_stars(message: Message, state: FSMContext):
    await state.update_data(Number_of_stars=kb.number)
    star_num = await state.get_data()
    print(star_num)
    await message.bot.send_invoice(
        message.from_user.id,
        title="Оплата звёзд",
        description="Оплата звёзд",
        provider_token=(os.getenv("STARS_PAYSMENTS")),
        currency="rub",
        photo_url="https://cs15.pikabu.ru/post_img/big/2024/08/24/10/1724515420160483017.png",  # Картинка
        photo_width=416,  # Ширина картинки
        photo_height=234,  # Высота картинки
        photo_size=416,  # Размер картинки
        is_flexible=False,
        prices=[LabeledPrice(label="Покупка стольки-то звёзд", amount=50 * 100)],
        start_parameter="",
        protect_content=True,
        payload="test-invoice-payload",
    )


@user.pre_checkout_query()
async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@user.message(F.successful_payment)
async def payment(message: Message):
    await message.answer(
        f"Спасибо за оплату, {message.from_user.first_name}\n",
        "Если появятся вопросы, обращайтесь в поддержку",
    )
