import tweepy
import os
import random
from datetime import datetime

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(
    API_KEY,
    API_SECRET,
    ACCESS_TOKEN,
    ACCESS_SECRET
)
api = tweepy.API(auth)

def send_random_photo():
    folder = "images"
    images = os.listdir(folder)
    if not images:
        print("Fotoğraf klasörü boş!")
        return

    img = random.choice(images)
    img_path = f"{folder}/{img}"

    time_text = datetime.now().strftime("%d %B %Y • %H:%M")
    text = f"Günlük otomatik paylaşım 📸\n{time_text}"

    api.update_status_with_media(status=text, filename=img_path)
    print("Tweet atıldı:", img)

if __name__ == "__main__":
    send_random_photo()
