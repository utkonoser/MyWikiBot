from aiogram import types
import wikipedia



async def start(message: types.Message):
    await message.answer("Hi! Press to select language:\n"
    " - /language_ru выбери русский\n - /language_en choose english\n After language selection  write what you want to know . Specify your requirements immediately, for example: \n"
" - python (programming language) or python (snake).")

async def language_ru(message: types.Message):
    await message.answer('У тебя получилось, ты выбрал русский язык для поиска!')
    wikipedia.set_lang('ru')

async def language_en(message: types.Message):
    await message.answer('You did it, you choose English!')
    wikipedia.set_lang('en')

async def help(message: types.Message):
    await message.answer('How to write a request correctly:\n    "what you are looking for (clarification)", for example: \n'
                            '        - python (snake)\n'
                            '        - python (programming language)\n'
                            'Press to select language:\n'
    ' - /language_ru выбери русский\n - /language_en choose english')

async def search(message: types.Message):
    try:
        await message.answer(f'Summary:\n {wikipedia.summary(message.text,sentences=4)}')
        await message.answer(f'Link:\n {wikipedia.page(message.text).url}')
        
    except wikipedia.exceptions.DisambiguationError:
        search = ', '.join(wikipedia.search(message.text))
        await message.answer(f'OOOPS! Try again and specify what you wanted to find: \n'
                            f'{search}')
        
    
 

