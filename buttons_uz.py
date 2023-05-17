
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# choosing language
language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "🇺🇿 O'zbekcha", callback_data = "ozbekcha"),
            InlineKeyboardButton(text = "🇬🇧 English", callback_data = "english")
        ]
    ]
)

# main menu
main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "📒 Loyiha haqida", callback_data = "loyiha_haqida"),
            InlineKeyboardButton(text = "📋 Ro'yxatdan o'tish", callback_data = "royxatdan_otish")
        ],
        [
            InlineKeyboardButton(text = "📝 Savollar yo'llash", callback_data = "savollar_yollash")
        ]
    ]
)

# about_the_project
loyiha_haqida = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Loyiha maqsadi", callback_data = "loyiha_maqsadi"), 
            InlineKeyboardButton(text = "Loyiha vazifasi", callback_data = "loyiha_vazifasi") 
        ],
        [
            InlineKeyboardButton(text = "O'tkazilish tartibi", callback_data = "otkazilish_tartibi"),
            InlineKeyboardButton(text = "Talablar", callback_data = "talablar")
        ],
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga")
        ]
    ]
)
# aim_project back
orqaga_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga1")
        ]
    ]
)
# project_task back
orqaga_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga2")
        ]
    ]
)

# order_process back
orqaga_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga3")
        ]
    ]
)
# requirements back
orqaga_4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga4")
        ]
    ]
)


# registration back
orqaga_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga5")
        ]
    ]
)

# send_questions back
orqaga_6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga6")
        ]
    ]
)
