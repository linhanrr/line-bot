from flask import Flask, request, abort  #用flask來架設伺服器

from linebot import (
    LineBotApi, WebhookHandler,
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage
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
    msg = event.message.text
    s = '你這臭婊'

    if msg =='張維珊':
        s = '阿彌陀佛'
    elif msg == '林翰':
        s = '大帥哥'
    elif msg == '丁元掄':
        s = '你這淫魔'
    elif msg == '悠悠':
        s = '悠悠辛苦了'
    elif '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='11539',
            sticker_id='52114110')

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)

        return

    elif '想壞壞' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/jkzgwt2.png',
            preview_image_url='https://i.imgur.com/AeJ8yOR.jpg')

        line_bot_api.reply_message(
            event.reply_token,
            image_message)
        return

    elif '鄭雅如' in msg:
        s = '你好醜'

        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/ikS4Fw2.jpg',
            preview_image_url='https://i.imgur.com/PRPt0RU.jpg')

        line_bot_api.reply_message(
            event.reply_token,
            image_message)
        
        
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))




if __name__ == "__main__":   #不希望import的時候程式碼就被執行
    app.run()