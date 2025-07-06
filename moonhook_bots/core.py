from moonhook_logging import Logger

import discord
# nectarinekooky
class DiscordToken:
    def __init__(self, DiscordToken, guild: str):
        self.DiscordToken = DiscordToken
        self.guild = guild

async def delete_channels(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception:
            Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}couldnt delete channel{Logger.ColorReset()}")

async def create_channels(guild, amount, name):
    for i in range(amount):
        try:
            await guild.create_text_channel(name)
        except Exception:
            Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}couldnt create a channel{Logger.ColorReset()}")

async def delete_roles(guild):
    for role in guild.roles:
        try:
            if role.name != "@everyone":
                await role.delete()
        except Exception:
            Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}couldnt delete a role{Logger.ColorReset()}")

async def create_roles(guild, role_name, amount):
    for i in range(amount):
        try:
            new_role = await guild.create_role(name=role_name)
        except Exception:
            Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}couldnt make a role{Logger.ColorReset()}")

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
client = discord.Client(intents=intents)

async def start_bot(DiscordToken):
    try:
        await client.start(DiscordToken)
        Logger.Log(f"Bot started successfully!")
    except discord.LoginFailure:
        Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}invalid bot token dumbass{Logger.ColorReset()}")
