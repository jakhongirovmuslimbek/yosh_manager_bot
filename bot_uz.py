import logging

from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttons_uz import *
from buttons_en import *

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help', 'restart'])
async def send_welcome(message: types.Message):
    await message.reply("Tilni tanlang! / Choose language!", reply_markup=language)

@dp.callback_query_handler(text='ozbekcha')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

 Sizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!
    
 Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!
    
 Ushbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.""", reply_markup=main_menu)

# about_the_project
@dp.callback_query_handler(text='loyiha_haqida')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Loyiha haqida!", reply_markup=loyiha_haqida)

@dp.callback_query_handler(text='orqaga')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

 Sizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!
    
 Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!
    
Ushbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.""", reply_markup=main_menu)    

# aim_project
@dp.callback_query_handler(text='loyiha_maqsadi')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""🔰 Yosh Menejerlar dasturi nima maqsadda tashkil etilmoqda?

Mazkur loyiha 17 yoshdan 25 yoshgacha bo'lgan yoshlar qatlamini loyihalar boshqaruvi bo'yicha nazariy jihatdan o'qitish, /
amaliy jihatdan yoshlarga ish tajribasini ulashish, turli fikr va dunyoqarashga ega shaxslar orasida muloqot almashinuvini /
yo'lga qo'yish maqsadida tashkil etilgan.""", reply_markup=orqaga_1)

@dp.callback_query_handler(text='orqaga1')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Loyiha haqida!", reply_markup=loyiha_haqida)

# project_task
@dp.callback_query_handler(text='loyiha_vazifasi')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""🔰 Loyihaning vazifalari nimalardan iborat?

• Boshqaruv sohasida malakaga ega, xalqaro doirada faoliyat yurita oladigan mutaxassislar tayyorlab, davlat va nodavlat sektoridagi subyekt/obyektlar uchun salohiyatli kadrlar tizimini yaratib berish;

• Yoshlarning bilim va ko'nikmasini oshirib, yuqori daromad keltiradigan ish bilan ta'minlash;

• Kattalar va yoshlar orasida kommunikatsiya jarayonini shakllantirib, o'rtadagi "jarlik"ka ma'lum /
ma'noda chek qo'yish, ularning o'zaro hamkorligini ta'minlashga ko'maklashish.""", reply_markup=orqaga_2)

@dp.callback_query_handler(text='orqaga2')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Loyiha haqida!", reply_markup=loyiha_haqida)

# order_process
@dp.callback_query_handler(text='otkazilish_tartibi')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""🔰 Loyiha qancha vaqt davom etadi va o'tkazilish tartibi qanday?

📝Yosh menejerlar dasturining o’tkazilish tartibi:

Loyiha 10 hafta davomida bo'lib o'tadi: amaliy va nazariy darslar olib boriladi.

📋 Avgust oyining 25-sanasidan boshlab 10-Sentabr kuniga qadar loyihada ishtirok etishga nomzod shaxslarni ro'yxatdan o'tkazish va saralash jarayoni tashkil etiladi:

• 1-bosqichi saralashdan o’tganlar: 13 Sentabr e’lon qilinadi. (100 ta ishtirokchi);
• 2-saralash bosqichi: 15-16 Sentabr kuni bo’lib o’tadi;
• Javoblar: 18 Sentabr kuni e’lon qilinadi (50 ta ishtirokchi).

💡 Nomzodlar ichidan 50 nafar kuchga to'la, ingliz tilini yaxshi biluvchi,/
o'z ambitsiyalariga ega va kelajakda katta maqsadlari bor yoshlar tanlab olinadi.""", reply_markup=orqaga_3)

@dp.callback_query_handler(text='orqaga3')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Loyiha haqida!", reply_markup=loyiha_haqida)

# requirements
@dp.callback_query_handler(text='talablar')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""🔰 Loyihada qatnashish uchun nomzodlarga qanday talablar qo'yiladi?

— ingliz, rus, o'zbek tilida ish yuritish: erkin so'zlashish va yoza olish;
— IT texnologiyalari hamda mediasavodxonlik bo'yicha bilimga egalik;
— 17-25 yosh orasida bo'lish;
— Toshkent shahri va viloyati hududida istiqomat qilish.""", reply_markup=orqaga_4)

@dp.callback_query_handler(text='orqaga4')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Loyiha haqida!", reply_markup=loyiha_haqida)

# registration
@dp.callback_query_handler(text='royxatdan_otish')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""Siz ro'yxatga olindingiz!""", reply_markup=orqaga_6)

@dp.callback_query_handler(text='orqaga6')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

Sizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!
    
Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!
    
Ushbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.""", reply_markup=main_menu)


# send_questions
@dp.callback_query_handler(text='savollar_yollash')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""Assalomu alaykum!

Savollaringizni @jakhongirov9001 ga yo'llashingiz mumkin. Sizga tez orada javob beramiz!

E'tiboringiz uchun rahmat.""", reply_markup=orqaga_5)

@dp.callback_query_handler(text='orqaga5')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

Sizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!
    
Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!
    
Ushbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.""", reply_markup=main_menu)


# english
@dp.callback_query_handler(text='english')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

We are glad to see you among our observers! 
    
The Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company! 
    
Through this program personnel management skills system will be formed in the international arena.""", reply_markup=main_menuu)

# about_the_project
@dp.callback_query_handler(text='about_the_project')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("About the project!", reply_markup=about_the_project)

# back
@dp.callback_query_handler(text='back')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

We are glad to see you among our observers! 
    
The Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company! 
    
Through this program personnel management skills system will be formed in the international arena.""", reply_markup=main_menuu)


# aim_project
@dp.callback_query_handler(text='aim_project')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""🔰 What is the main purpose of the Young Managers Program?

Project is designed to provide theoretical training in project management to young people from aged 17 to 25, to share practical work experience with / 
young people, and to establish a community between people with different ideas and worldviews.""", reply_markup=back_1)

    @dp.callback_query_handler(text='back1')
    async def my_func(call: types.CallbackQuery):
        await call.message.answer("About the project!", reply_markup=about_the_project)

# project_task
@dp.callback_query_handler(text='project_task')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""🔰 What are the objectives of project? 

• Training of specialists with international qualifications in the field of management and creation of a potential human resources system for entities and objects in the public and private sectors;

• Providing high-paid jobs to increase the knowledge and skills of youth; 

• To form a process of communication between the older and younger generations, /
to put an end to the "cliff" between them, to help them to ensure their interaction.""", reply_markup=back_2)

@dp.callback_query_handler(text='back2')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("About the project!", reply_markup=about_the_project)

# order_process
@dp.callback_query_handler(text='order_process')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""🔰 How long will the project last and what is the procedure?

📝 Procedure for the Young Managers Program:

The project will last for 10 weeks: practical and theoretical lessons will be conducted.

📋 From August 25 to September 10, the process of registration and selection of candidates for participation in the project will be organized:

• Round 1 qualifiers: September 13 will be announced. (100 participants);
• Qualifying Round 2: September 15-16;
• Answers: to be announced on September 18 (50 participants).

💡 Out of the candidates, 50 young people who are strong, fluent in/
English, have their own ambitions and have big goals for the future will be selected.""", reply_markup=back_3)

@dp.callback_query_handler(text='back3')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("About the project!", reply_markup=about_the_project)

# requirements
@dp.callback_query_handler(text='requirements')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""🔰 What are the requirements for candidates to participate?

— Office work in English, Russian, Uzbek: fluent speaking and writing skills;
— Knowledge of IT and media; 
— 17-25 years old;
— Resident of Tashkent city and region.""", reply_markup=back_4)

@dp.callback_query_handler(text='back4')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("About the project!", reply_markup=about_the_project)

# registration
@dp.callback_query_handler(text='registration')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("You are registered!", reply_markup=back_5)

@dp.callback_query_handler(text='back5')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

We are glad to see you among our observers! 
    
The Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company! 
    
Through this program personnel management skills system will be formed in the international arena.""", reply_markup=main_menuu)

# send_questions
@dp.callback_query_handler(text='send_questions')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""Assalamu alaikum!

You can send your questions to @jakhongirov9001. We will reply you soon.

Thank you for your attention.""", reply_markup=back_6)

@dp.callback_query_handler(text='back6')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""👋Assalomu alaykum!

We are glad to see you among our observers! 
    
The Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company! 
    
Through this program personnel management skills system will be formed in the international arena.""", reply_markup=main_menuu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
