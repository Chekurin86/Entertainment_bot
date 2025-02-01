from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Создаем объекты инлайн-кнопок стартового меню
button_yes = InlineKeyboardButton(
    text="Да, хочу",
    callback_data="yes_button_pressed"
)
button_no = InlineKeyboardButton(
    text="Нет, не хочу",
    callback_data="no_button_pressed"
)
# Создаем объект инлайн-клавиатуры
yes_no_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_yes, button_no]]
)

# Создаем объекты инлайн-кнопок
button_cat = InlineKeyboardButton(
    text="Кошка",
    callback_data="cat_button_pressed"
)
button_dog = InlineKeyboardButton(
    text="Собака",
    callback_data="dog_button_pressed"
)
button_fox = InlineKeyboardButton(
    text="Лиса",
    callback_data="fox_button_pressed"
)
button_kapibara = InlineKeyboardButton(
    text="Капибара",
    callback_data="kapibara_button_pressed"
)

# Создаем объект инлайн-клавиатуры
animal_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_cat, button_dog],
                    [button_fox, button_kapibara]]
)






















