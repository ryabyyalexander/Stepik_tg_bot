from aiogram import Router, F, Bot
from aiogram.types import (CallbackQuery, InputMediaAudio,
                           InputMediaAnimation, InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.exceptions import TelegramBadRequest

from keyboards import ikb

router = Router()
v1 = 'BAACAgIAAxkBAAIcGmVHiZq-AreHSC6VmtUR8NNiVmzYAAJpNAAC_4hBSn0eQv-9BjlFMwQ'
v2 = 'BAACAgIAAxkBAAIcG2VHiag3YYdWVqeRIpmsZX1X357TAAJtNAAC_4hBSuHwaSeSuRKJMwQ'
d1 = 'BQACAgIAAxkBAAIcJGVH_Ssy6A_K6oNYR666E0W0QyvbAAJROQAC_4hBSpn-RRcwW_BzMwQ'
d2 = 'BQACAgIAAxkBAAIcJWVH_TaerIy6bi9SrbBOdqVkvD8WAAJSOQAC_4hBSl67emTu27U3MwQ'
a1 = 'CQACAgIAAxkBAAIcYWVIC6jzvuKFEwVlcZZF_jnk-7D5AALqOQAC_4hBSgeX32oF4oc0MwQ'
a2 = 'CQACAgIAAxkBAAIcJ2VH_bbpE8cAARDMDQvlIJJHqa4cBAACVjkAAv-IQUq03ry-9QABA04zBA'
ph1 = 'AgACAgIAAxkBAAIcKmVH_usfG2a0fAz5hCCnKvygRN-CAAKU0zEb_4hBSomVhnlDI70QAQADAgADeQADMwQ'
ph2 = 'AgACAgIAAxkBAAIcK2VH_wpN3q2j6ylFbjReNCmLYrmbAAKV0zEb_4hBSspkZIYseXqIAQADAgADeQADMwQ'
g1 = 'CgACAgIAAxkBAAIcRGVIB3yfF8fmuX0R56VVHgkE3DqHAAI3NAACf8XRSbuAV4YGegc2MwQ'
g2 = 'CgACAgIAAxkBAAIcRWVIB4MXhwj8KA8D4TOQlP3U_bNoAAJHMQACRWX5SpLiGvQ9pzK7MwQ'


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(F.text == '/video')
async def process_sl(message: Message):
    markup = ikb(2, 'video')
    print(f'video: {v1}')
    await message.answer_video(video=v1,
                               caption='Это video 1',
                               reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['video']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = ikb(2, 'video')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaVideo(
                media=v2,
                caption='Это video 2'),
            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaVideo(
                media=v1,
                caption='Это video 1'),
            reply_markup=markup)


@router.message(F.text == '/photo')
async def process_sl(message: Message):
    markup = ikb(2, 'photo')
    await message.answer_photo(photo=ph1,
                               caption='Это photo 1',
                               reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['photo']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = ikb(2, 'photo')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=ph2,
                caption='Это photo 2'),
            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaPhoto(
                media=ph1,
                caption='Это photo 1'),
            reply_markup=markup)


@router.message(F.text == '/audio')
async def process_sl(message: Message):
    markup = ikb(2, 'audio')
    await message.answer_audio(audio=a1,
                               caption='Это audio 1',
                               reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['audio']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = ikb(2, 'audio')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaAudio(
                media=a2,
                caption='Это audio 2'),
            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaAudio(
                media=a1,
                caption='Это audio 1'),
            reply_markup=markup)


@router.message(F.text == '/animation')
async def process_sl(message: Message):
    markup = ikb(2, 'animation')
    await message.answer_animation(animation=g1,
                                   caption='Это animation 1',
                                   reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['animation']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = ikb(2, 'animation')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaAnimation(
                media=g2,
                caption='Это animation 2'),
            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaAnimation(
                media=g1,
                caption='Это animation 1'),
            reply_markup=markup)


@router.message(F.text == '/document')
async def process_sl(message: Message):
    markup = ikb(2, 'document')
    await message.answer_document(document=d1,
                                  caption='Это document 1',
                                  reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(F.data.in_(['document']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = ikb(2, 'document')
    try:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaDocument(
                media=d2,
                caption='Это document 2'),
            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            media=InputMediaDocument(
                media=d1,
                caption='Это document 1'),
            reply_markup=markup)
