from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

#by programIT Acedemy (MR.THANUWA)
@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Subscribe Channel", url="https://www.youtube.com/channel/UCNNO4kjUpcBYnJ4WI2igdEg")],
        [InlineKeyboardButton(
            "Bot Owner", url="https://t.me/MR_THANUWA")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help වැඩිදුර විස්තර සදහා....."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
