from pyrogram import *
import files.Rand as Rand
import tokens


api_id = tokens.api_id
api_hash = tokens.api_hash
token = tokens.token


bot = Client("olip", 
             api_id=api_id, 
             api_hash=api_hash, 
             bot_token=token)


imdb = "https://www.imdb.com/title/"


main_keyboard = types.ReplyKeyboardMarkup(keyboard= [['Roll']], resize_keyboard=1)


start_keyboard_buttons = [[types.InlineKeyboardButton(text="🔠 Random Word", callback_data="word"),
                            types.InlineKeyboardButton(text="📷 Random Pic",  callback_data="pic")],
                            [types.InlineKeyboardButton(text="🎞 Random Movie",  callback_data="movie"),
                             types.InlineKeyboardButton(text="🎵 Random Song",  callback_data="song")]]

word_again_button = types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="🔃 Again", callback_data="word")]])
pic_again_button = types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="🔃 Again", callback_data="pic")]])
movie_again_button = types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="🔃 Again", callback_data="movie")]])
song_again_button = types.InlineKeyboardMarkup([[types.InlineKeyboardButton(text="🔃 Again", callback_data="song")]])

start_keyboard = types.InlineKeyboardMarkup(start_keyboard_buttons)


@bot.on_callback_query()
async def main(client, cq):
    if cq.data == "word":
        word = Rand.rand_word(mean=1)
        await bot.send_message(cq.from_user.id,word, reply_markup=word_again_button)
        
    elif cq.data == "pic":
        pic = Rand.rand_pic()
        await bot.send_photo(cq.from_user.id,pic, reply_markup=pic_again_button)

    elif cq.data == "movie":
        movie = Rand.rand_movie()
        try:
            movie_name = movie['titleNameText']+"  "+movie['titleReleaseText']+"\n"+imdb+movie['id']
        except:
            movie_name = movie['titleNameText']+"  "+"\n"+imdb+movie['id']
        try:
            movie_pic = movie['titlePosterImageModel']['url']
        except:
            movie_pic = "https://upload.wikimedia.org/wikipedia/commons/a/a3/Image-not-found.png"
        await bot.send_photo(cq.from_user.id,movie_pic,movie_name, reply_markup=movie_again_button)

    elif cq.data == "song":
        song = Rand.rand_music()
        song_name = song['artist'] + " - " + song['title'] + "\n" + song['url']
        await bot.send_photo(cq.from_user.id, song['thumb'], song_name, reply_markup=song_again_button)



@bot.on_message(filters.command(["start"]))
async def start(c, m):
    await bot.send_message(m.chat.id, 'Hey! ', reply_markup=main_keyboard)


@bot.on_message(filters.regex("Roll"))
async def roll(c, m):
    await bot.send_message(m.chat.id, "\n🎲 Roll it! \n",reply_markup=start_keyboard)


print("i'm alive! ")
bot.run()