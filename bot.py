import random
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7272422270:AAF0N1amKeXf74HSP3l0QJcjCxyEc5BIvzQ'

bot = telebot.TeleBot(TOKEN)

# Лексика по темам
vocabulary = {
    'Спорт (스포츠)': ['футбол — 축구', 'баскетбол — 농구', 'волейбол — 배구', 'теннис — 테니스', 'бег — 달리기', 'лыжи — 스키', 'плавание — 수영', 'бокс — 상자', 'велосипед — 자전거', 'гимнастика — 체조 선수'],
    'Еда (식사)': ['рис — 쌀', 'лапша — 국수', 'суп — 수프', 'мясо — 고기', 'овощи — 야채', 'фрукты — 과일', 'рыба — 물고기', 'чай — 차', 'кофе — 커피', 'сок — 주스'],
    'Здоровье (건강)': ['больница — 병원', 'врач — 의사', 'лекарство — 의학', 'температура — 온도', 'грипп — 독감', 'кашель — 기침', 'головная боль — 두통', 'вакцина — 백신', 'маска — 마스크', 'гигиена — 위생'],
    'Путешествия (여행)': ['самолет — 비행기', 'поезд — 기차', 'отель — 호텔 정보', 'багаж — 수하물', 'паспорт — 여권', 'виза — 비자', 'экскурсия — 여행', 'карта — 지도', 'пляж — 해변', 'горы — 산'],
    'Учеба (연구)': ['учебник — 교과서', 'школа — 학교', 'университет — 대학', 'экзамен — 시험', 'урок — 수업', 'учитель — 교사', 'студент — 학생', 'домашнее задание — 숙제', 'класс — 클래스', 'перемена — 변경']
}

# Тексты для чтения
texts = {
    'Текст 1. 제 1 절': ('사람들은 결혼할 때 보통 많은 사람들을 초대합니다. 다른 사람들에게 결혼하는 모습을 보여 주고 싶기 때문입니다. 그런데 요즘에는 가족과 가까운 친구들만  초대해서  ‘작은 결혼식’을 하는 사람들이 생겼습니다. 이런 결혼식을 하는 사람들은 적은 돈으로 결혼을 준비합니다. 이렇게 하면서 가까운 사람들과 함께 결혼의 기쁨을 나눕니다.', 'Когда люди женятся, то обычно приглашают много людей. Потому что хотят показать другим людям свадебный облик. Но в последнее время появились люди, которые справляют «маленькую свадьбу», приглашая только семью и близких друзей. Люди, справляющие подобные свадьбы, готовят свадьбу за небольшие деньги. Таким образом делят радость свадьбы с близкими людьми.'),
    'Текст 2. 제 2 절': ('아버지는 요리에 관심이 없어서 거의 요리를 하지 않으셨습니다. 그런데 지난달에 어머니가 다리를 다쳐서   요리를 못 하게 되었습니다. 그때부터 아버지는 요리를 하시기 시작했습니다 . 아버지의 요리는 맛있을 때도 있고 맛없을 때도 있었습니다. 그런데 음식의 맛과 관계없이 어머니는 항상 맛있게 드셨습니다. 그 후로         아버지는 요리하는 것을 좋아하게 되셨습니다.', 'Папа почти не готовил, так как у него не было интереса к готовке. Но в прошлом месяце мама повредила ногу, поэтому не могла больше готовить. С тех пор папа начал готовить. Папина еда бывала вкусной, а бывала невкусной. Но независимо от вкуса, мама всегда ела с удовольствием. После этого папа полюбил готовить.'),
    'Текст 3. 제 3 절': ('제 이름은 폴 스미스입니다. 87년 생, 스물두 살입니다. 모내시 대학교 2학년입니다. 대학교에서 경제학하고 한국어를 전공해요. 저는 부모님과 여동생이 두 명 있어요. 여동생들은 고등학생인데, 아주 귀여워요. ^-^ 제 취미는 호주 축구입니다. 일요일에 친구들하고 같이 축구를 해요. 저는 비빔밥과 떡볶이를 좋아해요. 그래서 한국 식당에 자주 가요. 저는 바다를 좋아해요. 가끔 바다에서 수상스키를 해요. 저녁에는 카페에서 아르바이트해요. 그래서 아주 피곤해요. 하지만 돈 필요해요.', 'Меня зовут Пол Смит. 1987 гр, 22 года. Учусь в университете, второй год. Изучаю экономику и корейский язык. Семья: родители и 2 младшие сестры. Сестры учатся в старшей школе. Они очень милые. Мое хобби - футбол. По воскресеньям играем в футбол вместе с друзьями. Люблю пипимпаб и ттокпокки. Поэтому часто хожу в корейский ресторан. По вечерам подрабатываю в кафе. Поэтому очень устаю. Но нужны деньги.')
}

# Задания и ответы
tasks = {
    'Задание 1. 작업 1': ('Переведите слово "안녕하세요".', 'Привет'),
    'Задание 2. 작업 2': ('Напишите на корейском "спасибо".', '감사합니다'),
    'Задание 3. 작업 3': ('Как будет "школа" на корейском?', '학교')
}

# Интересные факты
facts = {
    'Интересный Факт 1. 흥미로운 사실 1': 'Корейский алфавит был создан в 1443 году.',
    'Интересный Факт 2. 흥미로운 사실 2': 'Сеул является столицей Южной Кореи.',
    'Интересный Факт 3. 흥미로운 사실 3': 'Корейская кухня известна своим острым вкусом.',
    'Интересный Факт 4. 흥미로운 사실 4': 'Корейский язык имеет 24 буквы.',
    'Интересный Факт 5. 흥미로운 사실 5': 'Тхэквондо - традиционное корейское боевое искусство.'
}

# Алфавит
alphabet = 'ГЛАСНЫЕ И ДИФТОНГИ:ㅏ[ aː ], ㅑ[ ja ], ㅓ[ ɔː ], ㅕ[ jɔ ], ㅗ [ oː ], ㅛ [ jo ], ㅜ [ uː ], ㅠ [ ju ], ㅡ [ ɯː ], ㅣ[ iː ], ㅐ [ ɛː ], ㅒ [ jɛː ], ㅔ [ eː ], ㅖ [ jeː ], ㅘ [ waː ], ㅙ [ wɛː ], ㅚ [ weː ], ㅝ [ wɔː ], ㅞ [ we ], ㅟ [ wiː ], ㅢ[ ɯiː ] СОГЛАСНЫЕ: ㄱ [ ɡ ] [ k ], ㄴ [ n ], ㄷ [ t ], ㄹ [ r ] [ l ], ㅁ [ m ], ㅂ [ p ], ㅅ [ s ], ㅇ [ ŋ ], ㅈ [ tʃ ], ㅊ [ tɕʰ ], ㅋ [ kʰ ], ㅌ[ tʰ ], ㅍ [ pʰ ], ㅎ [ h ], ㄲ [ k’ ], ㄸ [ t’ ], ㅃ [ p’ ], ㅆ [ s’ ], ㅉ [ tʃ ’ ]'

# Вопросы для теста
questions = [
    {
        'question': 'Как переводится слово "사과" на русский?',
        'options': ['Машина', 'Яблоко', 'Дом'],
        'correct_answer': 'Яблоко'
    },
    {
        'question': 'Как переводится слово "컴퓨터" на русский?',
        'options': ['Книга', 'Компьютер', 'Сумка'],
        'correct_answer': 'Компьютер'
    },
    {
        'question': 'Как переводится слово "고양이" на русский?',
        'options': ['Собака', 'Кошка', 'Мышь'],
        'correct_answer': 'Кошка'
    },
    {
        'question': 'Как переводится слово "물" на русский?',
        'options': ['Вода', 'Огонь', 'Воздух'],
        'correct_answer': 'Вода'
    },
    {
        'question': 'Как переводится слово "친구" на русский?',
        'options': ['Мама', 'Папа', 'Друг'],
        'correct_answer': 'Друг'
    }
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Начать изучение", callback_data="start_learning"))
    bot.send_message(message.chat.id, "안녕! Добро пожаловать в бот для изучения корейского языка.", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "start_learning":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Лексика", callback_data="vocabulary"))
        markup.add(InlineKeyboardButton("Чтение", callback_data="reading"))
        markup.add(InlineKeyboardButton("Задания", callback_data="tasks"))
        markup.add(InlineKeyboardButton("Алфавит", callback_data="alphabet"))
        markup.add(InlineKeyboardButton("Интересные факты", callback_data="facts"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите раздел:", reply_markup=markup)
    
    elif call.data == "vocabulary":
        markup = InlineKeyboardMarkup()
        for topic in vocabulary.keys():
            markup.add(InlineKeyboardButton(topic, callback_data=f'vocab_{topic}'))
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="start_learning"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите тему:", reply_markup=markup)
    
    elif call.data.startswith('vocab_'):
        topic = call.data.split('_')[1]
        words = vocabulary[topic]
        text = '\n'.join(words)
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="vocabulary"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Слова по теме {topic}:\n\n{text}', reply_markup=markup)
    
    elif call.data == "reading":
        markup = InlineKeyboardMarkup()
        for text in texts.keys():
            markup.add(InlineKeyboardButton(text, callback_data=f'read_{text}'))
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="start_learning"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите текст:", reply_markup=markup)
    
    elif call.data.startswith('read_'):
        text_key = call.data.split('_')[1]
        korean_text, _ = texts[text_key]
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Смотреть перевод", callback_data=f'translate_{text_key}'))
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="reading"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'{text_key}:\n\n{korean_text}', reply_markup=markup)
    
    elif call.data.startswith('translate_'):
        text_key = call.data.split('_')[1]
        _, translation = texts[text_key]
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="reading"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Перевод:\n\n{translation}', reply_markup=markup)
    
    elif call.data == "tasks":
        markup = InlineKeyboardMarkup()
        for task in tasks.keys():
            markup.add(InlineKeyboardButton(task, callback_data=f'task_{task}'))
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="start_learning"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите задание:", reply_markup=markup)
    
    elif call.data.startswith('task_'):
        task_key = call.data.split('_')[1]
        task, _ = tasks[task_key]
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Посмотреть ответ", callback_data=f'answer_{task_key}'))
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="tasks"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'{task_key}:\n\n{task}', reply_markup=markup)
    
    elif call.data.startswith('answer_'):
        task_key = call.data.split('_')[1]
        _, answer = tasks[task_key]
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="tasks"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Ответ:\n\n{answer}', reply_markup=markup)
    
    elif call.data == "alphabet":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="start_learning"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Алфавит:\n\n{alphabet}', reply_markup=markup)
    
    elif call.data == "facts":
        markup = InlineKeyboardMarkup()
        for i, fact in enumerate(facts.keys()):
            markup.add(InlineKeyboardButton(fact, callback_data=f'fact_{i+1}'))
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="start_learning"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите интересный факт:", reply_markup=markup)
    
    elif call.data.startswith('fact_'):
        fact_key = int(call.data.split('_')[1]) - 1
        fact_text = list(facts.values())[fact_key]
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Вернуться назад", callback_data="facts"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Интересный факт:\n\n{fact_text}', reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: call.data == "start_learning")
def start_learning(call):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Тест", callback_data="test"))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите тест:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "test")
def test(call):
    markup = InlineKeyboardMarkup()
    for i in range(1, 6):
        markup.add(InlineKeyboardButton(f"Вопрос {i}", callback_data=f"question_{i}"))
    markup.add(InlineKeyboardButton("Вернуться назад", callback_data="start_learning"))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите вопрос:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("question_"))
def question(call):
    question_index = int(call.data.split("_")[1]) - 1
    question_data = questions[question_index]
    markup = InlineKeyboardMarkup()
    for option in question_data['options']:
        markup.add(InlineKeyboardButton(option, callback_data=f"answer_{question_index}_{option}"))
    markup.add(InlineKeyboardButton("Вернуться назад", callback_data="test"))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=question_data['question'], reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("answer_"))
def answer(call):
    _, question_index, selected_option = call.data.split("_", 2)
    question_index = int(question_index)
    correct_option = questions[question_index]['correct_option']
    if selected_option == correct_option:
        bot.answer_callback_query(call.id, "Ты молодец! 잘했어! ")
        test(call)
    else:
        bot.answer_callback_query(call.id, "잘못된... Попробуй ещё раз...")
        test(call)
      
bot.polling(none_stop=True)

