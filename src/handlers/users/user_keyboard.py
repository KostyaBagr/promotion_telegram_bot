from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_buttons():
    """Кнопки, которые показываются при команде start"""
    investment_portfolio_1 = KeyboardButton(text='Портфель 1', callback_data='portfolio_1')
    investment_portfolio_2 = KeyboardButton(text='Портфель 2', callback_data='portfolio_2')
    not_interesting = KeyboardButton(text='Мне неинтересно', callback_data='not_interesting')

    menu = ReplyKeyboardMarkup(keyboard=[[investment_portfolio_1], [investment_portfolio_2], [not_interesting]],
                               resize_keyboard=True)

    return menu