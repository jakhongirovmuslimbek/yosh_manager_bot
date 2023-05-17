
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# tilni tanlash
language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "🇺🇿 O'zbekcha", callback_data = "ozbekcha"),
            InlineKeyboardButton(text = "🇬🇧 English", callback_data = "english")
        ]
    ]
)

# bosh menu
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

# loyiha haqida
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
# loyiha_maqsadi back
orqaga_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga1")
        ]
    ]
)
# loyiha_vazifasi back
orqaga_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga2")
        ]
    ]
)

# otkazilish_tartibi back
orqaga_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga3")
        ]
    ]
)
# talablar back
orqaga_4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga4")
        ]
    ]
)


# savollar_yollash back
orqaga_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga5")
        ]
    ]
)

# royxatdan_otish back
orqaga_6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "orqaga6")
        ]
    ]
)
