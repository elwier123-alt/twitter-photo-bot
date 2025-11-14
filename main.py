import tweepy
import os
from datetime import datetime

def post_photo():
    api_key = os.environ["API_KEY"]
    api_secret = os.environ["API_SECRET"]
    access_token = os.environ["ACCESS_TOKEN"]
    access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    # gönderilecek fotoğrafların klasörü
    folder = "photos"
    files = os.listdir(folder)

    if not files:
        print("Foto bulunamadı!")
        return

    photo = os.path.join(folder, files[0])  # ilk foto
    api.update_status_with_media(
        status=f"Günlük foto paylaşımı - {datetime.now().strftime('%Y-%m-%d')}",
        filename=photo
    )

    print("Foto gönderildi:", photo)

post_photo()
