from __future__ import unicode_literals
from pyrogram import Client, filters
from info import START_IMG, LOOK_IMG, COMMAND_HAND_LER, MOVIE_PIC, ADMINS, API_HASH, API_ID, BOT_TOKEN, MV_PIC, FSub_Channel, SESSION
from script import START_TXT, LOOK_TXT, HELP_TXT, ABOUT_TXT, SOURCE_TXT, MOVIE_ENG_TXT, MOVIE_MAL_TXT, OWNER_INFO, MV_TXT, KICKED, FSUB, COMMAND_USER, WAIT_MSG, REPLY_ERROR
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.errors import UserNotParticipant, FloodWait, MessageNotModified
from plugins.fun_strings import FUN_STRINGS
from urllib.parse import quote
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from aiohttp import ClientSession
from plugins.function import make_carbon
from yt_dlp import YoutubeDL
import youtube_dl
import math
import time
import aiohttp
import yt_dlp
import wget
import aiofiles
import requests
import random
import os
import asyncio
import users

SUPPORT_CHAT = "filmy_harbour_support"
aiohttpsession = ClientSession()

C = "**Join @filmy_harbour and @FH_MV**"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("© Fɪʟᴍʏ Hᴀʀʙᴏᴜʀ", url="https://t.me/FH_MV")
]]
)

tgbot=Client(
    session_name=SESSION,
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@tgbot.on_message(filters.command("start"))
async def start_message(bot, message):
    usr = open("users.txt", "w")
    if message.from_user.id not in users.txt:
        usr.write("New User "+str(message.from_user.mention)+"with ID: "+str(message.from_user.id))
        usr.close()
    else:
        usr.close()
    if FSub_Channel:
        try:
            user = await bot.get_chat_member(FSub_Channel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text(KICKED.format(message.from_user.mention))
                return
        except UserNotParticipant:
            await message.reply_text(
                text=(FSUB.format(message.from_user.mention)),
                reply_markup=InlineKeyboardMarkup(
                  [[
                    InlineKeyboardButton("Join Our Updates Channel 📢", url=f"t.me/{FSub_Channel}")
                 ],[
                    InlineKeyboardButton("Try Again 🔄", url="t.me/the_fun_mallu_bot?start")
                  ]]
                )
            )

            return
    n = await message.reply_text("<b>Processing</b>")
    await asyncio.sleep(0.5)
    await n.edit_text("<b>Processing.</b>")
    await asyncio.sleep(0.5)
    await n.edit_text("<b>Processing..</b>")
    await asyncio.sleep(0.5)
    await n.edit_text("<b>Processing...</b>")
    await asyncio.sleep(1)
    await n.delete()

    await message.reply_photo(
            photo=random.choice(START_IMG),
            caption=(START_TXT.format(message.from_user.mention)),
            reply_markup=InlineKeyboardMarkup(
                      [[
                        InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                     ],[
                        InlineKeyboardButton('🤴ʙᴏᴛ ᴏᴡɴᴇʀ🤴', callback_data="owner_info"),
                        InlineKeyboardButton('🍿ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ🍿', callback_data="movie_grp")
                     ],[
                        InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', callback_data='help'),
                        InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
                     ],[
                        InlineKeyboardButton('💥 ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 💥', url='https://t.me/+LJRsBp82HiJhNDhl')
                      ]]
            
            ),
            parse_mode='html'

)



@tgbot.on_message(filters.regex("movie") | filters.regex("Movie") & filters.group)
async def filter_handler(bot, message):
    if message.from_user.id not in ADMINS:
        await message.reply_photo(
            photo=(MOVIE_PIC),
            caption=(MOVIE_ENG_TXT.format(message.from_user.mention)),
            reply_markup=InlineKeyboardMarkup(
                      [[
                        InlineKeyboardButton('🇮🇳 Translate to Malayalam 🇮🇳', callback_data='movie_mal_txt')
                      ]]
            
            ),
            parse_mode="html"
)
    else:
        pro = await message.reply_text(f"<b>Hey {message.from_user.mention}, You are approved as Admin ✅</b>")
        await asyncio.sleep(5)
        await pro.delete()



@tgbot.on_callback_query()
async def cb_checker(bot, query: CallbackQuery):
        if query.data == "close_data":
            await query.message.delete()

        elif query.data == "start":
            buttons = [[
                        InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url=f'https://t.me/auto_m4_mallumovies_bot?startgroup=true')
                     ],[
                        InlineKeyboardButton('🤴ʙᴏᴛ ᴏᴡɴᴇʀ🤴', callback_data="owner_info"),
                        InlineKeyboardButton('🍿ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ🍿', callback_data="movie_grp")
                     ],[
                        InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', callback_data='help'),
                        InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
                     ],[
                        InlineKeyboardButton('💥 ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ 💥', url='https://t.me/+LJRsBp82HiJhNDhl')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(START_TXT.format(query.from_user.mention)),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "help":
            buttons = [[
                          InlineKeyboardButton('🏠 ʜᴏᴍᴇ', callback_data='start'),
                          InlineKeyboardButton('😊 ᴀʙᴏᴜᴛ', callback_data='about')
                      ],[
                          InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close_data'),
                          InlineKeyboardButton('❤️ sᴏᴜʀᴄᴇ', callback_data='sourcehelp')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(HELP_TXT.format(query.from_user.mention)),
                reply_markup=reply_markup,
                parse_mode='html'
            )
            await query.answer('Wᴇʟᴄᴏᴍᴇ Tᴏ Mʏ Hᴇʟᴘ Mᴏᴅᴜʟᴇ')

        elif query.data == "about":
            buttons = [[
                          InlineKeyboardButton('🏠 ʜᴏᴍᴇ', callback_data='start'),
                          InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', callback_data='help')
                      ],[
                          InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close_data'),
                          InlineKeyboardButton('❤️ sᴏᴜʀᴄᴇ', callback_data='source')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(ABOUT_TXT.format(query.from_user.mention)),
                reply_markup=reply_markup,
                parse_mode='html'
            )
            await query.answer("Wᴇʟᴄᴏᴍᴇ Tᴏ Mʏ Aʙᴏᴜᴛ Mᴏᴅᴜʟᴇ")

        elif query.data == "source":
            buttons = [[
                        InlineKeyboardButton('🔙 ʙᴀᴄᴋ', callback_data='about'),
                        InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close_data')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(SOURCE_TXT),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "sourcehelp":
            buttons = [[
                        InlineKeyboardButton('🔙 ʙᴀᴄᴋ', callback_data='help'),
                        InlineKeyboardButton('🔐 ᴄʟᴏsᴇ', callback_data='close_data')
                      ]]
            
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=(SOURCE_TXT),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "owner_info":
            btn = [[
                    InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="start"),
                    InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ", url="t.me/creatorbeatz")
                  ]]
            reply_markup = InlineKeyboardMarkup(btn)
            await query.message.edit_text(
                text=(OWNER_INFO),
                reply_markup=reply_markup,
                parse_mode='html'
            )

        elif query.data == "movie_mal_txt":
            btn = [[
                    InlineKeyboardButton("🇺🇲 Translate to English 🇺🇲", callback_data="movie_eng_txt")
                  ]]
            reply_markup = InlineKeyboardMarkup(btn)
            try:
                if query.from_user.id == query.message.reply_to_message.from_user.id:
                    await query.message.edit_text(
                        text=(MOVIE_MAL_TXT.format(query.from_user.mention)),
                        reply_markup=reply_markup,
                        parse_mode='html'
                    )
                
                else:
                    await query.answer("This is not for you !", show_alert=True)
            except AttributeError:
                    await query.answer("Button Expired !", show_alert=True)

        elif query.data == "movie_eng_txt":
            btn = [[
                    InlineKeyboardButton("🇮🇳 Translate to Malayalam 🇮🇳", callback_data="movie_mal_txt")
                  ]]
            reply_markup = InlineKeyboardMarkup(btn)
            try:
                if query.from_user.id == query.message.reply_to_message.from_user.id:
                    await query.message.edit_text(
                        text=(MOVIE_ENG_TXT.format(query.from_user.mention)),
                        reply_markup=reply_markup,
                        parse_mode='html'
                    )
                
                else:
                    await query.answer("This is not for you !", show_alert=True)
            except AttributeError:
                    await query.answer("Button Expired !", show_alert=True)

        elif query.data == "movie_grp":
            btn = [[
                    InlineKeyboardButton("ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ᴊᴏɪɴ ɢʀᴏᴜᴘ", url="https://t.me/+5olNhPeyW31jYjBl"),
                    InlineKeyboardButton("ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ", url="https://t.me/+asOwq8hpxSgwOTY9")
                 ],[
                    InlineKeyboardButton("ɴᴇᴡ ʀᴇʟᴇᴀsᴇs", url="https://t.me/+1Zr7U1TCCMw2YmJl"),
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_data")
                  ]]
            reply_markup = InlineKeyboardMarkup(btn)
            await query.message.reply_photo(
                photo=(MV_PIC),
                caption=(MV_TXT),
                reply_markup=reply_markup,
                parse_mode='html'
            )           

@tgbot.on_message(filters.command("howilook"))
async def howilook_message(bot, message):
    await message.reply_photo(
            photo=random.choice(LOOK_IMG),
            caption=(LOOK_TXT.format(message.from_user.first_name)),
            parse_mode='html'
)

# EMOJI CONSTANTS
DICE_E_MOJI = "🎲"
# EMOJI CONSTANTS


@tgbot.on_message(
    filters.command(["roll", "dice"], COMMAND_HAND_LER)
)
async def roll_dice(client, message):
    """ @RollaDie """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DICE_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
# EMOJI CONSTANTS


@tgbot.on_message(
    filters.command(["throw", "dart"], COMMAND_HAND_LER)
)
async def throw_dart(client, message):
    """ /throw an @AnimatedDart """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
GOAL_E_MOJI = "⚽"
# EMOJI CONSTANTS


@tgbot.on_message(
    filters.command(["goal", "shoot"], COMMAND_HAND_LER)
)
async def roll_dice(client, message):
    """ @Goal """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=GOAL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
PIN_BALL = "🎳"
# EMOJI CONSTANTS

@tgbot.on_message(
    filters.command(["pinball", "tenpin"])
)
async def pinball_tenpin(client, message):
    """ /pinball an @animatedpinball """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=PIN_BALL,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )

# EMOJI CONSTANTS
TRY_YOUR_LUCK = "🎰"
# EMOJI CONSTANTS

@tgbot.on_message(
    filters.command(["luck", "cownd"])
)
async def luck_cownd(client, message):
    """ /luck an @animatedluck """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


@tgbot.on_message(
    filters.command("fun", COMMAND_HAND_LER)
)
async def runs(_, message):
    await message.reply_chat_action("Typing")
    await asyncio.sleep(2)
    """ /fun strings """
    effective_string = random.choice(FUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

def share_link(text: str) -> str:
    return "**Here is Your Sharing Text 👇**\n\nhttps://t.me/share/url?url=" + quote(text)

@tgbot.on_message(filters.command(["share", "sharetext", "st", "stxt", "shtxt", "shtext"]))
async def share_text(client, message):
    reply = message.reply_to_message
    reply_id = message.reply_to_message.message_id if message.reply_to_message else message.message_id
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text(
            text=f"**Notice:**\n\n1. Reply Any Messages.\n2. No Media Support\n\n**Any Question Join Support Chat**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Support Chat", url=f"https://t.me/{SUPPORT_CHAT}")
                    ]                
                ]
            ),
            reply_to_message_id=reply_id
        )
        return
    await message.reply_text(share_link(input_text), reply_to_message_id=reply_id)

@tgbot.on_message((filters.command(["report"]) | filters.regex("@admins") | filters.regex("@admin")) & filters.group)
async def report_user(bot, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        admins = await bot.get_chat_members(chat_id=chat_id, filter="administrators")
        success = True
        report = f"𝖱𝖾𝗉𝗈𝗋𝗍𝖾𝗋 : {mention} ({reporter})" + "\n"
        report += f"𝖬𝖾𝗌𝗌𝖺𝗀𝖾 : {message.reply_to_message.link}"
        for admin in admins:
            try:
                reported_post = await message.reply_to_message.forward(admin.user.id)
                await reported_post.reply_text(
                    text=report,
                    chat_id=admin.user.id,
                    disable_web_page_preview=True
                )
                success = True
            except:
                pass
        if success:
            await message.reply_text(f"Hey {message.from_user.mention}, Your Report Has Been Sent T𝗈 𝖠𝖽𝗆𝗂𝗇𝗌!")    
            
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@tgbot.on_message(filters.command('song') & ~filters.private & ~filters.channel)
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("**ѕєαrchíng чσur ѕσng...!**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        performer = f"[ᗩᒍᗩ᙭]" 
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "**𝙵𝙾𝚄𝙽𝙳 𝙽𝙾𝚃𝙷𝙸𝙽𝙶 𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙾𝚁𝚁𝙴𝙲𝚃 𝚃𝙷𝙴 𝚂𝙿𝙴𝙻𝙻𝙸𝙽𝙶 𝙾𝚁 𝚂𝙴𝙰𝚁𝙲𝙷 𝙰𝙽𝚈 𝙾𝚃𝙷𝙴𝚁 𝚂𝙾𝙽𝙶**"
        )
        print(str(e))
        return
    m.edit("**dσwnlσαdíng чσur ѕσng...!**")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = '**𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴 ›› [𝙾𝙿𝚄𝚂-𝚃𝙴𝙲𝙷𝚉](https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA)**\n**𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 ›› [muѕíc вσч](https://t.me/OPMusicBoy_Bot)**'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit("**🚫 𝙴𝚁𝚁𝙾𝚁 🚫**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

def get_text(message: Message) -> [None,str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None


@tgbot.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    urlissed = get_text(message)

    pablo = await client.send_message(
        message.chat.id, f"**𝙵𝙸𝙽𝙳𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚅𝙸𝙳𝙴𝙾** `{urlissed}`"
    )
    if not urlissed:
        await pablo.edit("Invalid Command Syntax Please Check help Menu To Know More!")
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await event.edit(event, f"**𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙵𝚊𝚒𝚕𝚎𝚍 𝙿𝚕𝚎𝚊𝚜𝚎 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗..♥️** \n**Error :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""
**𝚃𝙸𝚃𝙻𝙴 :** [{thum}]({mo})
**𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :** {message.from_user.mention}
"""
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,        
        reply_to_message_id=message.message_id 
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)

@tgbot.on_inline_query()
async def inline(bot, query: InlineQuery):
    await query.answer(
        results = [
            InlineQueryResultArticle(
                title = "Movies",
                description = "For new and old movies and series in all languages, CLICK ME !",
                thumb_url = "https://telegra.ph/file/7c924bffb69a01d834ba4.jpg",
                input_message_content = InputTextMessageContent(
                    message_text = (MV_TXT)
                ),
                reply_markup = InlineKeyboardMarkup(
                [[
                  InlineKeyboardButton("ᴊᴏɪɴ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ", url="https://t.me/+5olNhPeyW31jYjBl"),
                  InlineKeyboardButton("ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ", url="https://t.me/+asOwq8hpxSgwOTY9")
               ],[
                  InlineKeyboardButton("ɴᴇᴡ ʀᴇʟᴇᴀsᴇs", url="https://t.me/+1Zr7U1TCCMw2YmJl")
                ]]
                )
            )
        ],
        cache_time = 0
    )

@tgbot.on_message(filters.command("trash") & filters.group)
async def trash_handler(bot, message):
    if message.from_user.id not in ADMINS:
        await message.reply_text("<b>Hey bro, This is an Admin Command !</b>")
    else:
        try:
            await message.reply_to_message.delete()
            await message.delete()
        except AttributeError:
            await message.reply_text("<b>Hey, Use this command as a reply to any message...</b>")

@tgbot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    user_id = message.from_user.id
    m = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("ᴜᴘʟᴏᴀᴅɪɴɢ..")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()

tgbot.run()
