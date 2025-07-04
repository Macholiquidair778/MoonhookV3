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
            print("couldnt delete channel")

async def create_channels(guild, amount, name):
    for i in range(amount):
        try:
            await guild.create_text_channel(name)
        except Exception:
            print("couldnt create a channel")

async def delete_roles(guild):
    for role in guild.roles:
        try:
            if role.name != "@everyone":
                await role.delete()
        except Exception:
            print("couldnt delete a role")

async def create_roles(guild, role_name, amount):
    for i in range(amount):
        try:
            new_role = await guild.create_role(name=role_name)
        except Exception:
            print("couldnt make a role")

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
client = discord.Client(intents=intents)

async def start_bot(DiscordToken):
    try:
        await client.start(DiscordToken)
    except discord.LoginFailure:
        print("invalid bot token dumbass")
