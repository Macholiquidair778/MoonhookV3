# // MoonHook V3 1.0.0
    # Original by Tobias, V3 by Jasper

        # NOTE: Most of the code is inside the libraries

from datetime import datetime
from moonhook_logging import Logger
from moonhook_webhooks import DiscordWebhook
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

def intInput(t):
    try:
        return int(input(t))
    except:
        return 1

def WebhookPanel(url: str):
    Logger.clear()

    rgbGradientStart = (255, 255, 255)
    rgbGradientEnd = (66, 135, 245)

    Logger.print_gradient_ascii(WebhooksBanner, rgbGradientStart, rgbGradientEnd)
    print("\nMoonHook Webhook Panel\n 1. Send Message\n 2. Webhook Spam\n 3. Change Webhook Name\n 4. Change Webhook Avatar\n 5. Delete Webhook")

    selection = intInput(f"{mainColor}MoonHook | Select Option (1-5): {rst}")

    hook = DiscordWebhook(url)
    
    if selection == 1:
        print("Select Content Type\n 1. Plain Text\n 2. JSON string")
        cType = intInput(f"{mainColor}MoonHook | Select Content Type (1-2): {rst}")
        content = input(f"{mainColor}MoonHook | Content to send: {rst}")

        if cType == 1:
            Logger.Log("MoonHook", "Sending webhook message..")
            code, result = hook.SendMessage(content)

            if result != "":
                Logger.Log("MoonHook", f"{Logger.rgb_to_ansi(255, 0, 0)}Sending error: {result}{rst}")
                os.system("pause")
                main()
            
            Logger.Log("MoonHook", "Successfully sent message!")
            os.system("pause")
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

    selection = 1

    try:
        selection = int(input(f"\n{mainColor}1. Select an option (1-2): {rst}"))
    except Exception as e:
        print(f"{Logger.rgb_to_ansi(255, 0, 0)}Looks like the text you entered wasn't a number!{rst}")
        os.system("pause")

    if selection == 1:
        wUrl = input(f"{mainColor}MoonHook | Enter your Discord webhook URL: {rst}")
        WebhookPanel(wUrl)

if __name__ == "__main__":
    main()
