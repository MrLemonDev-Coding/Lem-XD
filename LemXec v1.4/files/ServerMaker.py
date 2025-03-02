import discord
from discord.ext import commands
import random
import string

TOKEN = input("bot Token:")
GUILD_ID = input("server id:")

# Using old intents (default)
intents = discord.Intents.default()

bot = commands.Bot(command_prefix=".", intents=intents)


def generate_random_name(length=15):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    guild = bot.get_guild(GUILD_ID)

    if guild is None:
        print(f"❌ Guild with ID {GUILD_ID} not found!")
        return

    # ➕ Create 10 random categories
    for i in range(10):
        try:
            category_name = generate_random_name()
            await guild.create_category(category_name)
            print(f"✅ Created category: {category_name}")
        except Exception as e:
            print(f"⚠ Error creating category {i+1}: {e}")

    # ➕ Create 10 random roles
    for i in range(10):
        try:
            role_name = generate_random_name()
            await guild.create_role(name=role_name)
            print(f"✅ Created role: {role_name}")
        except Exception as e:
            print(f"⚠ Error creating role {i+1}: {e}")

    # ➕ Create 10 random text channels
    for i in range(10):
        try:
            channel_name = generate_random_name()
            await guild.create_text_channel(channel_name)
            print(f"✅ Created channel: {channel_name}")
        except Exception as e:
            print(f"⚠ Error creating channel {i+1}: {e}")

            bot.close()

bot.run(TOKEN)