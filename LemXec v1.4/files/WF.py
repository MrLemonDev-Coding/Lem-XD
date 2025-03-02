import requests
import discord
from discord import channel
from discord import message

WEBHOOK_URL = input("webhook url:")
opt = input("Delete webhook: 1, Spam: 2 : ")

if opt == "1":
    response = requests.delete(WEBHOOK_URL)
    if response.status_code == 204:
        print("deleted.")
    else:
        print(f"Failed to delete webhook: {response.status_code}")
elif opt == "2":
    text = input("msg to spam:")
    requests.post(WEBHOOK_URL, data={'contents': text})