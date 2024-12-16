from aiogram.fsm.state import State, StatesGroup


class UstozShogirt(StatesGroup):
    ism_k = State()
    Yosh_k = State()
    Til_k = State()
    Tel_k = State()
    Vil_k = State()


class Sherikkerak(StatesGroup):
    name_k = State()
    age_k = State()
    lang_k = State()
    phone_k = State()
    city_k = State()


class Hodimkerak(StatesGroup):
    namec_k = State()
    agec_k = State()
    langc_k = State()
    phonec_k = State()
    cityc_k = State()
