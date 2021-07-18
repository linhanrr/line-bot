from flask import Flask, request, abort  #用flask來架設伺服器

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('25/1W5qDMalZO93YqLc/fGkntrHzXiujsZTaedTyMoLbxGw0tnPRVJrNFCHKWl5RMWhIcX3QxHYdsezeCXdy6yMMddC3dcHAW/qvWZWPFPV7Ly+JXScJU8ntD7dV7PsXK9+SkacCFTC3CtXyEKHkuwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('742b339d7b22f4c79946ac12a367074d')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":   #不希望import的時候程式碼就被執行
    app.run()