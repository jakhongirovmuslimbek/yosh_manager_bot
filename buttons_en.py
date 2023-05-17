
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# main menu
main_menuu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "📒 About the Project", callback_data = "about_the_project"),
            InlineKeyboardButton(text = "📋 Registration", callback_data = "registration")
        ],
        [
            InlineKeyboardButton(text = "📝 Send questions", callback_data = "send_questions")
        ]
    ]
)

# about_the_project
about_the_project = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Aim of the project", callback_data = "aim_project"), 
            InlineKeyboardButton(text = "Project task", callback_data = "project_task") 
        ],
        [
            InlineKeyboardButton(text = "The order of process", callback_data = "order_process"),
            InlineKeyboardButton(text = "Requirements", callback_data = "requirements")
        ],
        [
            InlineKeyboardButton(text = "⬅️ Back", callback_data = "back")
        ]
    ]
)

# aim_project back
back_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Back", callback_data = "back1")
        ]
    ]
)

# project_task back
back_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Back", callback_data = "back2")
        ]
    ]
)

# order_process back
back_3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Back", callback_data = "back3")
        ]
    ]
)

# requirements back
back_4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Back", callback_data = "back4")
        ]
    ]
)
# registration back
back_5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Back", callback_data = "back5")
        ]
    ]
)

# send_questions back
back_6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "⬅️ Back", callback_data = "back6")
        ]
    ]
)

