import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN
from aiogram.fsm.context import FSMContext
from state import UstozShogirt as US
from state import Sherikkerak as ShK
from state import Hodimkerak as HK
from button import *
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command('start'))
async def CommandStart(message: Message):
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!", reply_markup=menu)


@dp.message(F.text == 'Ish Kerak')
async def start_ism(message: Message, state: FSMContext):
    await state.set_state(US.ism_k)
    await message.answer(text='Ismni Kiriting')


@dp.message(US.ism_k)
async def get_ism(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data(ism=ism)
    await message.answer(text='Yoshni Kiriting')
    await state.set_state(US.Yosh_k)


@dp.message(US.Yosh_k)
async def get_yosh(message: Message, state: FSMContext):
    yosh = message.text
    await state.update_data(yosh=yosh)
    await message.answer(text='''🕑 Yosh: 

    Yoshingizni kiriting?
    Masalan, 19''')
    await state.set_state(US.Til_k)


@dp.message(US.Til_k)
async def get_til(message: Message, state: FSMContext):
    til = message.text
    await state.update_data(til=til)
    await message.answer(text='Telefonni Kiriting')
    await state.set_state(US.Tel_k)


@dp.message(US.Tel_k)
async def get_tel(message: Message, state: FSMContext):
    telefon = message.text
    await state.update_data(telefon=telefon)
    await message.answer(text='Viloyatingizni Kiriting')
    await state.set_state(US.Vil_k)


@dp.message(US.Vil_k)
async def get_viloyat(message: Message, state: FSMContext):
    viloyat = message.text
    await state.update_data(viloyat=viloyat)
    user_data = await state.get_data()
    ism = user_data.get('ism')
    yosh = user_data.get('yosh')
    til = user_data.get('til')
    telefon = user_data.get('telefon')
    viloyat = user_data.get('viloyat')

    await message.answer(text=f"Ismingiz: {ism}\nYoshingiz: {yosh}\nTil: {til}\nTelefon: {telefon}\nViloyat: {viloyat}")
    await state.clear()













@dp.message(F.text == 'Sherik kerak')
async def start_m(message: Message, state: FSMContext):
    await state.set_state(ShK.name_k)
    await message.answer(text='Ismni Kiriting')


@dp.message(ShK.name_k)
async def get_is(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(text='Yoshni Kiriting')
    await state.set_state(ShK.age_k)


@dp.message(ShK.age_k)
async def get_yos(message: Message, state: FSMContext):
    age= message.text
    await state.update_data(age=age)
    await message.answer(text='Tilni Kiriting')
    await state.set_state(ShK.lang_k)


@dp.message(ShK.lang_k)
async def get_ti(message: Message, state: FSMContext):
    lang= message.text
    await state.update_data(lang=lang)
    await message.answer(text='Telefonni Kiriting')
    await state.set_state(ShK.phone_k)


@dp.message(ShK.phone_k)
async def get_te(message: Message, state: FSMContext):
    phones= message.text
    await state.update_data(phones=phones)
    await message.answer(text='Viloyatingizni Kiriting')
    await state.set_state(ShK.city_k)


@dp.message(ShK.city_k)
async def get_viloyt(message: Message, state: FSMContext):
    cities= message.text
    await state.update_data(cities=cities)
    user_data = await state.get_data()
    name = user_data.get('name')
    age = user_data.get('age')
    lang = user_data.get('lang')
    phones = user_data.get('phones')
    cities = user_data.get('cities')

    await message.answer(text=f"Ismingiz: {name}\nYoshingiz: {age}\nTil: {lang}\nTelefon: {phones}\nViloyat: {cities}")
    await state.clear()









@dp.message(F.text == 'Hodim kerak')
async def start_m(message: Message, state: FSMContext):
    await state.set_state(HK.namec_k)
    await message.answer(text='Ismni Kiriting')


@dp.message(HK.namec_k)
async def get_s(message: Message, state: FSMContext):
    namec= message.text
    await state.update_data(namec=namec)
    await message.answer(text='Yoshni Kiriting')
    await state.set_state(HK.agec_k)


@dp.message(HK.agec_k)
async def get_ys(message: Message, state: FSMContext):
    agec= message.text
    await state.update_data(agec=agec)
    await message.answer(text='Tilni Kiriting')
    await state.set_state(HK.langc_k)


@dp.message(HK.langc_k)
async def get_t(message: Message, state: FSMContext):
    langc= message.text
    await state.update_data(langc=langc)
    await message.answer(text='Telefonni Kiriting')
    await state.set_state(HK.phonec_k)


@dp.message(HK.phonec_k)
async def get_e(message: Message, state: FSMContext):
    phoned= message.text
    await state.update_data(phoned=phoned)
    await message.answer(text='Viloyatingizni Kiriting')
    await state.set_state(HK.cityc_k)


@dp.message(HK.cityc_k)
async def get_vilot(message: Message, state: FSMContext):
    citie= message.text
    await state.update_data(citie=citie)
    user_data = await state.get_data()
    namec = user_data.get('namec')
    agec = user_data.get('agec')
    langc = user_data.get('langc')
    phonec = user_data.get('phonec')
    cityc = user_data.get('cityc')

    await message.answer(text=f"Ismingiz: {namec}\nYoshingiz: {agec}\nTil: {langc}\nTelefon: {phonec}\nViloyat: {cityc}")
    await state.clear()






async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except Exception as e:
        print(f"Xatolik: {e}")
