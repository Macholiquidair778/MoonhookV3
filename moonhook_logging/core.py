# // core.py for moonhook_logging

from datetime import datetime
import os
import random

class Logger:
    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
    
    @staticmethod
    def enable_ascii():
        os.system("chcp 65001")

    @staticmethod
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
    
    @staticmethod
    def ColorReset():
        return "\033[0m"

    @staticmethod
    def print_random_message():
        messageList = ["MoonHook V3 BETA!!!", "Now works with discord bots!", "Original by @_tobiaszeq_", "V3 written by Jasper", "Open-Source!"]
        print(f"{Logger.rgb_to_ansi(0, 204, 255)}{messageList[random.randint(0, len(messageList))]}\n{Logger.ColorReset()}")

    @staticmethod
    def print_gradient_ascii(text, start_color, end_color):
        lines = text.strip().split('\n')
        max_length = max(len(line) for line in lines) if lines else 0

        for line in lines:
            gradient_line = ""
            line_length = len(line)
            if line_length == 0:
                print()
                continue

            for i, char in enumerate(line):
                progress = i / max_length if max_length > 0 else 0

                r = int(start_color[0] + (end_color[0] - start_color[0]) * progress)
                g = int(start_color[1] + (end_color[1] - start_color[1]) * progress)
                b = int(start_color[2] + (end_color[2] - start_color[2]) * progress)

                r = max(0, min(255, r))
                g = max(0, min(255, g))
                b = max(0, min(255, b))

                color = Logger.rgb_to_ansi(r, g, b)
                gradient_line += color + char

            print(gradient_line + "\033[0m")

    @staticmethod
    def Log(Text: str):
        print(f"{datetime.now()} [MoonHook]: {Text}")
