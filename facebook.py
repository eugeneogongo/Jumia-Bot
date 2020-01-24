import requests
import settings
import os


class FaceBook:
    token = ""

    def __init__(self, app_id, app_secret):
        # self.token = self.get_fb_token(app_id, app_secret)
        print(self.token)

    def get_fb_token(self, app_id, app_secret):
        url = 'https://graph.facebook.com/oauth/access_token'
        payload = {
            'grant_type': 'client_credentials',
            'client_id': app_id,
            'client_secret': app_secret
        }
        response = requests.post(url, params=payload)
        personal = response.json()['access_token']
        params = {
            "fields": personal
        }
        r = requests.get(
            "https://graph.facebook.com/" + os.getenv("fb_pageid") + "?fields=access_token&access_token=" + personal)
        print(r.text)
        return r.json()['access_token']

    def post_to_fb(self, desc, link):
        link = "https://c.jumia.io/?a=119339&c=9&p=r&E=kkYNyk2M4sk%3D&ckmrdr=" + link + "&utm_campaign=119339"
        params = {
            "message": desc,
            "link": link,
            "access_token": os.getenv("access_token")
        }
        r = requests.post("https://graph.facebook.com/v5.0/" + os.getenv("fb_pageid") + "/feed", data=params)

        return "Facebook Post is = " + r.text + "<br> The post content is " + desc + "<br><br>The Link is :<a href='" + link + "'> Jumia postlink</a>"
