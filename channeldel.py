import asyncio
import random
import discord
from typing import Union
client = discord.Client(self_bot=True)
token = input("Token : ")
channel_id: Union[int, str] = input("Channel ID: ")
@client.event
async def on_ready():
    print(f"Logged in as '{client.user}'")
    try:
        counter = 0
        print(f"Fetching channel with ID '{channel_id}'")
        await asyncio.sleep(random.uniform(0.4, 0.6))
        channel = await client.fetch_channel(channel_id)
        if not isinstance(channel, discord.TextChannel):
            raise Exception(f"Channel with ID '{channel_id}' is not a text channel")
        print("Starting message deletion")
        async for msg in channel.history(limit=None):
            if msg.author.id == client.user.id:
                try:
                    await msg.delete()
                    counter += 1
                    print(f"Deleted message {counter}")
                    await asyncio.sleep(random.uniform(0.6, 0.9))
                    if counter % 10 == 0:
                        print("Pausing for 10 seconds...")
                        await asyncio.sleep(10)
                except discord.Forbidden as e:
                    print(f"Skipping message due to error: {e}")
        print(f"Finished deleting {counter} messages.")
    except Exception as e:
        print(f"Error: {str(e)}")
        await asyncio.sleep(10)
        exit()
    finally:
        print("Finished deleting all messages! The script will close in 10s")
        await asyncio.sleep(10)
        exit()
if __name__ == '__main__':
    try:
        client.run(token)
    except discord.errors.LoginFailure:
        print("Login failure: improper token")
        exit()
