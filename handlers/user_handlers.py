from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import yes_no_keyboard, animal_keyboard
from lexicon.lexicon import LEXICON_RU
import requests

router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_keyboard)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_keyboard)


# Этот хэндлер срабатывает на согласие пользователя посмотреть животных
# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'yes_button_pressed'
@router.callback_query(F.data == "yes_button_pressed")
async def process_button_1_press(callback: CallbackQuery):
    await callback.message.answer(text='Выберите, какое вы хотите увидеть животное.',
                                  reply_markup=animal_keyboard)


# Этот хэндлер срабатывает на отказ пользователя посмотреть животных
# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'no_button_pressed'
@router.callback_query(F.data == "no_button_pressed")
async def process_no_answer(callback: CallbackQuery):
    await callback.message.answer(text="Ваше право, но если все-таки захотите, нажмите кнопку 'Да, хочу'.",
                                  reply_markup=yes_no_keyboard)


# Этот хэндлер срабатывает на на нажатие кнопки с выбором животного - кошки
@router.callback_query(F.data == "cat_button_pressed")
async def process_cat_button(callback: CallbackQuery):
    animal_response = requests.get(LEXICON_RU['CATS_API_URL'])
    await callback.message.answer_photo(photo=animal_response.json()[0]['url'])
    await callback.message.answer(text="Хочешь еще посмотреть изображения животных?", reply_markup=yes_no_keyboard)

# Этот хэндлер срабатывает на на нажатие кнопки с выбором животного - собаки
@router.callback_query(F.data == "dog_button_pressed")
async def process_cat_button(callback: CallbackQuery):
    animal_response = requests.get(LEXICON_RU['DOGS_API_URL'])
    await callback.message.answer_photo(photo=animal_response.json()['url'])
    await callback.message.answer(text="Хочешь еще посмотреть изображения животных?", reply_markup=yes_no_keyboard)

# Этот хэндлер срабатывает на на нажатие кнопки с выбором животного - лисы
@router.callback_query(F.data == "fox_button_pressed")
async def process_cat_button(callback: CallbackQuery):
    animal_response = requests.get(LEXICON_RU['FOXES_API_URL'])
    await callback.message.answer_photo(photo=animal_response.json()['link'])
    await callback.message.answer(text="Хочешь еще посмотреть изображения животных?", reply_markup=yes_no_keyboard)

# Этот хэндлер срабатывает на на нажатие кнопки с выбором животного - капибары
@router.callback_query(F.data == "kapibara_button_pressed")
async def process_cat_button(callback: CallbackQuery):
    animal_response = requests.get(LEXICON_RU["CAPYBARA_API_URL"])
    await callback.message.answer_photo(photo=animal_response.json()['data']['url'])
    await callback.message.answer(text="Хочешь еще посмотреть изображения животных?", reply_markup=yes_no_keyboard)

