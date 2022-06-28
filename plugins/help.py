from pyrogram import Client, Filters

#by programIT Acedemy (MR.THANUWA)
@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"දැනට සහය දක්වන්නේ  Youtube Single Video එකකට පමණි (Playlist නොමැතිව) Youtube Url එවන්න \nby programIT Acedemy"
    await message.reply_text(helptxt)
