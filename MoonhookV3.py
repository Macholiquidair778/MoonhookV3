# // MoonHook V3
# Original by Tobias, V3 by Jasper

from datetime import datetime
from moonhook_bots.core import (
    GetBotClient,
    GetGuildByID,
    ban_everyone,
    spam_messages,
    start_bot,
    stop_bot,
)
from moonhook_logging import Logger
from moonhook_webhooks import DiscordWebhook
import moonhook_bots
import asyncio
import threading
import os
import sys

mainColor = Logger.rgb_to_ansi(255, 225, 0)
rst = Logger.ColorReset()


Banner = """
 __       __                                __    __                      __       
/  \     /  |                              /  |  /  |                    /  |      
$$  \   /$$ |  ______    ______   _______  $$ |  $$ |  ______    ______  $$ |   __ 
$$$  \ /$$$ | /      \  /      \ /       \ $$ |__$$ | /      \  /      \ $$ |  /  |
$$$$  /$$$$ |/$$$$$$  |/$$$$$$  |$$$$$$$  |$$    $$ |/$$$$$$  |/$$$$$$  |$$ |_/$$/ 
$$ $$ $$/$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |$$   $$<  
$$ |$$$/ $$ |$$ \__$$ |$$ \__$$ |$$ |  $$ |$$ |  $$ |$$ \__$$ |$$ \__$$ |$$$$$$  \ 
$$ | $/  $$ |$$    $$/ $$    $$/ $$ |  $$ |$$ |  $$ |$$    $$/ $$    $$/ $$ | $$  |
$$/      $$/  $$$$$$/   $$$$$$/  $$/   $$/ $$/   $$/  $$$$$$/   $$$$$$/  $$/   $$/   V3.0.0!

"""

WebhooksBanner = """
 __       __            __        __                            __                 
/  |  _  /  |          /  |      /  |                          /  |                
$$ | / \ $$ |  ______  $$ |____  $$ |____    ______    ______  $$ |   __   _______ 
$$ |/$  \$$ | /      \ $$      \ $$      \  /      \  /      \ $$ |  /  | /       |
$$ /$$$  $$ |/$$$$$$  |$$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |$$ |_/$$/ /$$$$$$$/ 
$$ $$/$$ $$ |$$    $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$   $$<  $$      \ 
$$$$/  $$$$ |$$$$$$$$/ $$ |__$$ |$$ |  $$ |$$ \__$$ |$$ \__$$ |$$$$$$  \  $$$$$$  |
$$$/    $$$ |$$       |$$    $$/ $$ |  $$ |$$    $$/ $$    $$/ $$ | $$  |/     $$/ 
$$/      $$/  $$$$$$$/ $$$$$$$/  $$/   $$/  $$$$$$/   $$$$$$/  $$/   $$/ $$$$$$$/    MoonHook V3

"""

BotsBanner = """
 _______   __                                                __        _______               __              
/       \ /  |                                              /  |      /       \             /  |             
$$$$$$$  |$$/   _______   _______   ______    ______    ____$$ |      $$$$$$$  |  ______   _$$ |_    _______ 
$$ |  $$ |/  | /       | /       | /      \  /      \  /    $$ |      $$ |__$$ | /      \ / $$   |  /       |
$$ |  $$ |$$ |/$$$$$$$/ /$$$$$$$/ /$$$$$$  |/$$$$$$  |/$$$$$$$ |      $$    $$< /$$$$$$  |$$$$$$/  /$$$$$$$/ 
$$ |  $$ |$$ |$$      \ $$ |      $$ |  $$ |$$ |  $$/ $$ |  $$ |      $$$$$$$  |$$ |  $$ |  $$ | __$$      \ 
$$ |__$$ |$$ | $$$$$$  |$$ \_____ $$ \__$$ |$$ |      $$ \__$$ |      $$ |__$$ |$$ \__$$ |  $$ |/  |$$$$$$  |
$$    $$/ $$ |/     $$/ $$       |$$    $$/ $$ |      $$    $$ |      $$    $$/ $$    $$/   $$  $$//     $$/ 
$$$$$$$/  $$/ $$$$$$$/   $$$$$$$/  $$$$$$/  $$/        $$$$$$$/       $$$$$$$/   $$$$$$/     $$$$/ $$$$$$$/  
        MoonHook V3                                                                                                                                                                                                                     
"""


def intInput(t):
    try:
        return int(input(f"{mainColor}MoonHook | {t}{rst}"))
    except ValueError:
        return 1


def strInput(t):
    return input(f"{mainColor}MoonHook | {t}{rst}")


def BotsPanel(Token: str, GuildID: int):
    Logger.clear()

    botClient = GetBotClient()

    rgbGradientStart = (250, 102, 102)
    rgbGradientEnd = (255, 0, 0)

    Logger.print_gradient_ascii(BotsBanner, rgbGradientStart, rgbGradientEnd)
    print(
        f"\nMoonHook Bot Panel\n 1. Activate Bot\n 2. Delete All Channels\n 3. Channel Spam\n 4. Delete All Roles\n 5. Role Spam\n {Logger.rgb_to_ansi(255, 0, 0)}6. ⚠️ Full Server Nuke{rst}\n 7. Deactivate Bot\n 8. Message Spam\n{Logger.rgb_to_ansi(255, 0, 0)} 9. ⚠️Ban Everyone\n 10. Back to main menu"
    )

    selection = intInput("Select Option (1-10): ")

    if selection in [2, 3, 4, 5, 6, 8, 9]:
        TargetGuild = GetGuildByID(GuildID)
        if TargetGuild is None or not hasattr(botClient, "loop_ref"):
            Logger.Log("Bot is not connected or Guild not found! Ensure the bot is running and wait a moment.")
            Logger.AwaitInput()
            BotsPanel(Token, GuildID)
            return

    if selection == 1:
        Logger.Log("Attempting to start bot..")

        def _cnt():
            asyncio.run(moonhook_bots.start_bot(Token))

        threading.Thread(target=_cnt, daemon=True).start()

        Logger.Log("If you got no error messages, this means that the bot had started.")
        Logger.AwaitInput()
        BotsPanel(Token, GuildID)
    elif selection == 2:
        Logger.Log("Attempting to delete every channel..")

        future = asyncio.run_coroutine_threadsafe(
            moonhook_bots.delete_channels(TargetGuild), botClient.loop_ref
        )
        future.result()

        Logger.AwaitInput()
        BotsPanel(Token, GuildID)
    elif selection == 3:
        cspmtxt = strInput("Channel name: ")
        cspmamnt = intInput("Amount of channels: ")
        Logger.Log("Attempting to channel spam..")

        future = asyncio.run_coroutine_threadsafe(
            moonhook_bots.create_channels(TargetGuild, cspmamnt, cspmtxt),
            botClient.loop_ref,
        )
        future.result()
        Logger.AwaitInput()
        BotsPanel(Token, GuildID)
    elif selection == 4:
        Logger.Log("Attempting to delete roles..")

        future = asyncio.run_coroutine_threadsafe(
            moonhook_bots.delete_roles(TargetGuild), botClient.loop_ref
        )
        future.result()
        Logger.AwaitInput()
        BotsPanel(Token, GuildID)
    elif selection == 5:
        rspmtxt = strInput("Role name: ")
        rspmamnt = intInput("Amount of roles: ")

        Logger.Log("Attempting to role spam..")

        future = asyncio.run_coroutine_threadsafe(
            moonhook_bots.create_roles(TargetGuild, rspmtxt, rspmamnt),
            botClient.loop_ref,
        )
        future.result()
        Logger.AwaitInput()
        BotsPanel(Token, GuildID)
    elif selection == 6:
        messagespamtext = strInput("Message to spam: ")
        messagespamcooldown = intInput("Message spam cooldown(s): ")
        channelspamtext = strInput("Channel, Role, Webhook names: ")
        amounttospam = intInput("Amount of channels, roles, webhooks to spam: ")
        _confirmation = strInput("Are you sure you want to spam everything? (y/n)")
        Logger.Log("Performing a full server nuke.. (this may take some time so load)")

        if _confirmation.lower().strip() != "y":
            Logger.Log("Cancelled.")
            Logger.AwaitInput()
            BotsPanel(Token, GuildID)

        # // Delete stuff
        asyncio.run_coroutine_threadsafe(
            moonhook_bots.delete_channels(TargetGuild), botClient.loop_ref
        ).result()

        asyncio.run_coroutine_threadsafe(
            moonhook_bots.delete_roles(TargetGuild), botClient.loop_ref
        ).result()

        # // Do stuff
        asyncio.run_coroutine_threadsafe(
            moonhook_bots.create_channels(TargetGuild, amounttospam, channelspamtext),
            botClient.loop_ref,
        ).result()

        asyncio.run_coroutine_threadsafe(
            moonhook_bots.create_roles(TargetGuild, channelspamtext, amounttospam),
            botClient.loop_ref,
        ).result()

        asyncio.run_coroutine_threadsafe(
            spam_messages(
                TargetGuild, channelspamtext, messagespamtext, messagespamcooldown
            ),
            botClient.loop_ref,
        ).result()

        Logger.AwaitInput()
        BotsPanel(Token, GuildID)
    elif selection == 7:
        if not hasattr(botClient, "loop_ref"):
            Logger.Log("Bot is not running!")
            Logger.AwaitInput()
            BotsPanel(Token, GuildID)
            return

        Logger.Log("Attempting to stop bot.. (Bot may take a bit to go offline.)")

        asyncio.run_coroutine_threadsafe(stop_bot(), botClient.loop_ref)
        Logger.AwaitInput()
        BotsPanel(Token, GuildID)
    elif selection == 8:
        messagespamtext = strInput("Text to spam: ")
        messagespamcooldown = intInput("Spam cooldown: ")
        webhooknames = strInput(
            "Webhook name(NOTE: if you previously nuked all, or message spammed, I recommend you use the same webhook name as you did previously.): "
        )
        Logger.Log("Spamming messages..")

        asyncio.run_coroutine_threadsafe(
            spam_messages(
                TargetGuild, webhooknames, messagespamtext, messagespamcooldown
            ),
            botClient.loop_ref,
        ).result()
        Logger.AwaitInput()
        BotsPanel(Token, GuildID)
    elif selection == 9:
        _confirmation = strInput("Are you sure you want to ban everyone? (y/n): ")

        if _confirmation.lower().strip() != "y":
            Logger.Log("Cancelled.")
            Logger.AwaitInput()
            BotsPanel(Token, GuildID)

        Logger.Log("Attempting to ban everyone..")
        asyncio.run_coroutine_threadsafe(ban_everyone(TargetGuild), botClient.loop_ref)
    else:
        main()


def WebhookPanel(url: str):
    Logger.clear()

    rgbGradientStart = (255, 255, 255)
    rgbGradientEnd = (66, 135, 245)

    Logger.print_gradient_ascii(WebhooksBanner, rgbGradientStart, rgbGradientEnd)
    print(
        "\nMoonHook Webhook Panel\n 1. Send Message\n 2. Webhook Spam\n 3. Change Webhook Name\n 4. Change Webhook Avatar\n 5. Delete Webhook\n 6. Exit back to main panel"
    )

    selection = intInput("Select Option (1-6): ")

    hook = DiscordWebhook(url)

    if selection == 1:
        print("Select Content Type\n 1. Plain Text\n 2. JSON string")
        cType = intInput("Select Content Type (1-2): ")
        content = strInput("Content to send: ")

        if cType == 1:
            Logger.Log("Sending webhook message..")
            code, result = hook.SendMessage(content)

            if result != "":
                Logger.Log(
                    f"{Logger.rgb_to_ansi(255, 0, 0)}Sending error: {result}{rst}"
                )
                os.system("pause")
                main()

            Logger.Log("Successfully sent message!")
            os.system("pause")
            WebhookPanel(url)
        else:
            Logger.Log("Sending webhook message..")
            code, result = hook.SendRawContent(content)

            if result != "":
                Logger.Log(
                    f"{Logger.rgb_to_ansi(255, 0, 0)}Sending error: {result}{rst}"
                )
                os.system("pause")
                WebhookPanel(url)

            Logger.Log("Successfully sent message!")
            os.system("pause")
            WebhookPanel(url)

    elif selection == 2:
        print("Select Content Type\n 1. Plain Text\n 2. JSON string")
        cType = intInput("Select Content Type (1-2): ")
        content = strInput("Content to send: ")
        delay = intInput("Message Delay: ")
        threads = intInput("Number of threads (recommended 5-10): ")

        Logger.Log("Beginning webhook spam...")

        try:
            hook.WebhookSpam(cType, content, delay, threads)
        except KeyboardInterrupt:
            WebhookPanel(url)

    elif selection == 3:
        newName = strInput("Enter the new webhook name: ")
        Logger.Log("Attempting to change webhook name..")
        code, result = hook.ChangeWebhookName(newName)
        if code != 200:
            Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}Error: {result}!{rst}")
        else:
            Logger.Log("Successfully set username!")
        os.system("pause")
        WebhookPanel(url)

    elif selection == 4:
        filepath = strInput("Enter your image path: ")
        Logger.Log("Attempting to change webhook avatar..")
        code, result = hook.ChangeWebhookAvatar(filepath)
        if code != 200:
            Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}Error: {result}!{rst}")
        else:
            Logger.Log("Successfully set avatar!")
        os.system("pause")
        WebhookPanel(url)

    elif selection == 5:
        confirmation = strInput(
            "Are you sure you want to delete this webhook? (Y/N): "
        ).lower()
        if confirmation == "y":
            Logger.Log("Attempting to delete webhook..")
            code, result = hook.DeleteWebhook()
            if code != 200:
                Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}Error: {result}!{rst}")
            else:
                Logger.Log("Successfully deleted webhook!")
            os.system("pause")
            main()
        else:
            Logger.Log("Webhook deletion cancelled.")

    elif selection == 6:
        main()


def main():
    # // Stuff to print the banner

    rgbGradientStart = (255, 98, 0)
    rgbGradientEnd = (255, 225, 0)

    Logger.enable_ascii()
    Logger.clear()
    Logger.print_gradient_ascii(Banner, rgbGradientStart, rgbGradientEnd)
    print("""

MoonHook V3 Written by Jasper (@u235consumer)
Original moonhook by @_tobiaszeq_""")
    Logger.print_random_message()

    print("MoonHook Panel\n 1. Webhooks\n 2. Bots\n 3. Exit")

    selection = intInput("Select an option (1-3): ")

    if selection == 1:
        wUrl = strInput("Enter your webhook URL: ").strip()
        WebhookPanel(wUrl)
    elif selection == 2:
        token = strInput("Enter your bot token: ").strip()
        guildID = intInput("Enter your guild / server ID: ")

        def _cnt():
            asyncio.run(moonhook_bots.start_bot(token))

        threading.Thread(target=_cnt, daemon=True).start()

        BotsPanel(token, guildID)
    elif selection == 3:
        Logger.clear()
        sys.exit()
    else:
        print(f"{Logger.rgb_to_ansi(255, 0, 0)}Invalid selection!{rst}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Logger.Log("\nExitted.")
        sys.exit(0)
