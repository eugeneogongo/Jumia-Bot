from flask import Flask
from jumiascrapper import JumiaScrapper
from facebook import FaceBook
import settings
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    scrapper: JumiaScrapper = JumiaScrapper()
    fb_bot = FaceBook(os.getenv("app_id"),os.getenv("app_secret"))
    response = fb_bot.post_to_fb(desc=scrapper.createpost(), link=scrapper.productlink())
    return response


if __name__ == '__main__':
    app.run()
