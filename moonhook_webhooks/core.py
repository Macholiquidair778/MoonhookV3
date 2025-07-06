# // core.py for moonhook_webhooks

from moonhook_logging import Logger
from PIL import Image
import requests
import base64
import time
import io

class InvalidContentTypeError(Exception):
    pass

class DiscordWebhook:
    def __init__(self, WebhookUrl: str):
        self.WebhookURL = WebhookUrl

    def SendMessage(self, Text: str):
        Req = requests.post(
            url=self.WebhookURL,
            json={
                "content": Text
            }
        )

        return Req.status_code, Req.text
    
    def SendRawContent(self, Content: str):
        Req = requests.post(
            url=self.WebhookURL,
            data=Content,
            headers={
                "Content-Type": "application/json"
            }
        )

        return Req.status_code, Req.text
    
    def WebhookSpam(self, ContentType: int, Content: str, DelaySeconds: int):
        # // Type 1 is text, type 2 is raw json
        while True:
            Logger.Log("Sending message..")
            if ContentType == 1:
                code, result = self.SendMessage(Content)
                
                if result != "":
                    Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}Sending error: {result}!{Logger.ColorReset()}")
                else:
                    Logger.Log(f"Successfully sent, result(text): {result}")
            elif ContentType == 2:
                code, result = self.SendRawContent(Content)
                
                if result != "":
                    Logger.Log(f"{Logger.rgb_to_ansi(255, 0, 0)}Sending error: {result}!{Logger.ColorReset()}")
                else:
                    Logger.Log(f"Successfully sent, result(text): {result}")
            else:
                raise InvalidContentTypeError("Invalid content type!")

            time.sleep(DelaySeconds)

    def ChangeWebhookName(self, NewName: str):
        resp = requests.patch(
            url=self.WebhookURL,
            json={
                "name": NewName
            }
        )

        return resp.status_code, resp.text
    
    def ChangeWebhookAvatar(self, ImagePath: str):
        try:
            with Image.open(ImagePath) as img:
                img = img.resize((128, 128))
                img_byte_array = io.BytesIO()
                img.save(img_byte_array, format="PNG")
                avatar_base64 = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

                resp = requests.patch(
                    url=self.WebhookURL,
                    json={
                        "avatar": f"data:image/png;base64,{avatar_base64}"
                    }
                )

                return resp.status_code, resp.text
        except Exception as e:
            return False, e
        
    def DeleteWebhook(self):
        resp = requests.delete(self.WebhookURL)
        return resp.status_code, resp.text
