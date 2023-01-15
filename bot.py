import os
import discord
import requests
import json
import random
from replit import db

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tamim = ["nigga", "Nigga", "NIGGA", "tamim", "TAMIM"]

tamim_reply = [
  "He's doing NIGGA dance", "He's doing NIGGA dance in toilet",
  "YO NIGGA NIGGA NIGGA!", "Maybe he got married that's why he isn't here"
]

maourex = ["Fish", "fish", "maoufish", "Maoufish", "depressing", "maourex"]

maourex_reply = [
  "Here fishy fishy fishy", "Maoufish where are you?", "He is watching Hentai",
  "He should get married"
]

tonmoy = ["kobi", "tokai", "tonmoy", "angry", "depressing"]

tonmoy_reply = [
  "Hey bot where are you", "Ore garani na dile thik hoibo na",
  "I need to wear mask now", "Trash hacker?"
]

game = ["apex", "warframe", "paladin", "angry", "depressing"]

game_reply = [
  "Why you wanna suffer", "Didn't like your good time?",
  "Don't drown others with you"
]

if "responding" not in db.keys():
  db["responding"] = True


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return (quote)


@client.event
async def on_ready():
  print("We have been logged in as {0.user}", format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if db["responding"]:
    if message.content.startswith("!hello"):
      await message.channel.send("What the HELL")

    if message.content.startswith("!inspire"):
      quote = get_quote()
      await message.channel.send(quote)

    if any(word in msg for word in game):
      await message.channel.send(random.choice(game_reply))

    if any(word in msg for word in tamim):
      await message.channel.send(random.choice(tamim_reply))

    if any(word in msg for word in maourex):
      await message.channel.send(random.choice(maourex_reply))

    if msg.startswith("!list"):
      encouragements = []
      if "encouragements" in db.keys():
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)

  if msg.startswith("!responding"):
    value = msg.split("!responding ", 1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding in on")
    else:
      db["responding"] = False
      await message.channel.send("Responding in off")


client.run(os.getenv("Maoufish"))
