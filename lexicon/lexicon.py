import random

LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n\nЯ бот который может показать тебе иображения разных животных.\n'
              'Хотите посмотреть на случайное изображение выбранного животного?\n'
              'Или можете отправить команду /help, если захотите узнать как я работаю.',
    '/help': 'Если вы захотите увидеть случайную фотографию из списка доступных животных,\n'
            'то нажмите кнопку "Да, хочу", после чего появится меню в котором вы сможете выбрать животное\n'
             ' и увидеть его случайную фотографию.\n'
              'Все очень просто:)',
    'error': 'Извините, я умею только показывать изображения животных....',
    'CATS_API_URL' : "https://api.thecatapi.com/v1/images/search",
    'DOGS_API_URL' : "https://random.dog/woof.json",
    'FOXES_API_URL' : "https://randomfox.ca/floof/",
    'CAPYBARA_API_URL' : "https://api.capy.lol/v1/capybara?json=true"
}

