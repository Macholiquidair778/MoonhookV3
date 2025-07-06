# // MoonHook V3 1.0.0
    # Original by Tobias, V3 by Jasper

        # NOTE: Most of the code is inside the libraries

from datetime import datetime
from moonhook_logging import Logger
from moonhook_webhooks import DiscordWebhook
import moonhook_bots
import threading
import os

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
$$/      $$/  $$$$$$/   $$$$$$/  $$/   $$/ $$/   $$/  $$$$$$/   $$$$$$/  $$/   $$/   V3 1.0.0!

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
    except:
        return 1
    
def strInput(t):
    return input(f"{mainColor}MoonHook | {t}{rst}")

def BotsPanel(Token: str, GuildID: int):
    Logger.clear()

    rgbGradientStart = (250, 102, 102)
    rgbGradientEnd = (255, 0, 0)

    botRunning = False

    Logger.print_gradient_ascii(BotsBanner, rgbGradientStart, rgbGradientEnd)
    print(f"\nMoonHook Bot Panel\n 1. Activate Bot\n 2. Delete All Channels\n 3. Channel Spam\n 4. Delete All Roles\n 5. Role Spam\n {Logger.rgb_to_ansi(255, 0, 0)}6. ⚠️ Full Server Nuke{rst}\n 7. Exit back to menu")

    selection = intInput("Select Option (1-7): ")
    
    if selection == 1:
        Logger.Log("Attempting to start bot..")
        threading.Thread()
        Logger.Log("If you got no error messages, this means that the bot had started.")
        os.system("pause")
        BotsPanel(Token, GuildID)

def WebhookPanel(url: str):
    Logger.clear()

    rgbGradientStart = (255, 255, 255)
    rgbGradientEnd = (66, 135, 245)

    Logger.print_gradient_ascii(WebhooksBanner, rgbGradientStart, rgbGradientEnd)
    print("\nMoonHook Webhook Panel\n 1. Send Message\n 2. Webhook Spam\n 3. Change Webhook Name\n 4. Change Webhook Avatar\n 5. Delete Webhook\n 6. Exit back to main panel")

    selection = intInput("Select Option (1-6): ")

    hook = DiscordWebhook(url)
    
    if selection == 1:
        print("Select Content Type\n 1. Plain Text\n 2. JSON string")
        cType = strInput("Select Content Type (1-2): ")
        content = strInput("Content to send: ")

        if cType == 1:
            Logger.Log("Sending webhook message..")
            code, result = hook.SendMessage(content)

            if result != "":
                Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}Sending error: {result}{rst}")
                os.system("pause")
                main()
            
            Logger.Log("Successfully sent message!")
            os.system("pause")
            WebhookPanel(url)
        else:
            Logger.Log("Sending webhook message..")
            code, result = hook.SendRawContent(content)

            if result != "":
                Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}Sending error: {result}{rst}")
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

        Logger.Log("Beginning webhook spam...")

        try:
            hook.WebhookSpam(cType, content, delay) 
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
        confirmation = strInput("Are you sure you want to delete this webhook? (Y/N): ").lower()
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

    print("MoonHook Panel\n 1. Webhooks\n 2. Bots")

    selection = intInput("Select an option (1-2): ")

    if selection == 1:
        wUrl = strInput("Enter your webhook URL: ")
        WebhookPanel(wUrl)
    elif selection == 2:
        token = strInput("Enter your bot token: ")
        guildID = intInput("Enter your guild / server ID: ")
        BotsPanel(token, guildID)
    else:
        print(f"{Logger.rgb_to_ansi(255, 0, 0)}Invalid selection!{rst}")

if __name__ == "__main__":
    main()
