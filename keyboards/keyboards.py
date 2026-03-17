from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Профиль", callback_data="profile"), InlineKeyboardButton(text="Купить звёзды", callback_data="stars")]
])

stars = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="50 ⭐️", callback_data="50"), InlineKeyboardButton(text="100 ⭐️", callback_data="100")],
    [InlineKeyboardButton(text="150 ⭐️", callback_data="150"), InlineKeyboardButton(text="200 ⭐️", callback_data="200")],
    [InlineKeyboardButton(text="250 ⭐️", callback_data="250"), InlineKeyboardButton(text="300 ⭐️", callback_data="300")],
    [InlineKeyboardButton(text="350 ⭐️", callback_data="350"), InlineKeyboardButton(text="400 ⭐️", callback_data="400")],
    [InlineKeyboardButton(text="450 ⭐️", callback_data="450"), InlineKeyboardButton(text="500 ⭐️", callback_data="500")]
])