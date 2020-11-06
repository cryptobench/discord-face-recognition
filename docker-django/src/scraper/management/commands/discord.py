# bot.py
import os

import discord
from discord.ext import commands, tasks
from discord.ext.tasks import loop
from discord.ext.commands import Bot
import asyncio
from django.core.management.base import BaseCommand
from discord.utils import get
import uuid
import aiofiles
import aiohttp
import face_recognition
import imageio
from PIL import Image
import glob

TOKEN = os.environ.get('DISCORD_TOKEN')
intents = discord.Intents.all()

#If you use commands.Bot()
bot = commands.Bot(command_prefix="!", intents=intents)
class Command(BaseCommand):
    help = 'kigger efter grimme adams'
    def handle(self, *args, **kwargs):
        
        @loop(seconds=600)
        async def delete_files():
            await bot.wait_until_ready()
            files = glob.glob('/src/mikkeldetect/unknown/*')
            for f in files:
                os.remove(f)

        @bot.event
        async def on_message(message):
            if message.author == bot.user:
                return
            elif message.attachments:
                async with aiohttp.ClientSession() as session:
                    url = message.attachments[0].url
                    async with session.get(url) as resp:
                        if resp.status == 200:
                            unique_id = str(uuid.uuid4())
                            saved_name = unique_id + "_" + message.attachments[0].filename
                            f = await aiofiles.open("/src/mikkeldetect/unknown/" + saved_name, mode='wb')
                            await f.write(await resp.read())
                            await f.close()
                            known_image = face_recognition.load_image_file("/src/mikkeldetect/known/9cba089e-5335-4850-aad9-2a8db784bf2f_e02f5c33-84fd-4626-85ce-28ebde2f78f0.jpg")
                            seb = face_recognition.load_image_file("/src/mikkeldetect/known/1012213b-ee5d-429c-a337-84b555166050_45831711_10215905562864673_2230478178688696320_n.jpg")
                            emil = face_recognition.load_image_file("/src/mikkeldetect/known/3bc0aaf5-2242-4dc7-bb8c-38765558b611_2.png")
                            nur = face_recognition.load_image_file("/src/mikkeldetect/known/e5d2a88d-00a7-4329-889e-61ab4c96ecc8_2.png")
                            simon = face_recognition.load_image_file("/src/mikkeldetect/known/a07fcb0d-60d1-45e9-94d5-2e0b3c0b591b_30516063_10214576452478382_7170141059618439168_n.jpg")
                            phillip = face_recognition.load_image_file("/src/mikkeldetect/known/3d081327-638a-4929-99ac-2a57d56460b6_14022349_1244419688904217_1236347110488693907_n.jpg")
                            ajo = face_recognition.load_image_file("/src/mikkeldetect/known/72dc232a-c7f4-4708-b13f-f03383552357_99c2beed-a76c-4411-8f09-7c4dd7e757af.jpg")
                            oscar = face_recognition.load_image_file("/src/mikkeldetect/known/9b1ac0bd-d795-4fb5-b595-c8153ee2d085.jpg")
                            magnus = face_recognition.load_image_file("/src/mikkeldetect/known/d92c137b-18e7-4873-8844-2411d294df81.jpg")
                            unknown_image = face_recognition.load_image_file("/src/mikkeldetect/unknown/" + saved_name)
                            biden_encoding = face_recognition.face_encodings(known_image)[0]
                            seb_encoding = face_recognition.face_encodings(seb)[0]
                            emil_encoding = face_recognition.face_encodings(emil)[0]
                            nur_encoding = face_recognition.face_encodings(nur)[0]
                            simon_encoding = face_recognition.face_encodings(simon)[0]
                            phillip_encoding = face_recognition.face_encodings(phillip)[0]
                            ajo_encoding = face_recognition.face_encodings(ajo)[0]
                            oscar_encoding = face_recognition.face_encodings(oscar)[0]
                            magnus_encoding = face_recognition.face_encodings(magnus)[0]
                    

                            face_locations = face_recognition.face_locations(unknown_image)
                            for face_location in face_locations:
                                unique_name = str(uuid.uuid4())
                                top, right, bottom, left = face_location
                                face_image = unknown_image[top:bottom, left:right]
                                imageio.imwrite("/src/mikkeldetect/unknown/" + unique_name + ".jpg", face_image)
                                unknown_cut = face_recognition.load_image_file("/src/mikkeldetect/unknown/" + unique_name + ".jpg")
                                unknown_encoding = face_recognition.face_encodings(unknown_cut)[0]
                                results = face_recognition.compare_faces([biden_encoding, seb_encoding, emil_encoding, nur_encoding, simon_encoding, phillip_encoding, ajo_encoding, oscar_encoding, magnus_encoding], unknown_encoding)
                                for idx,val in enumerate(results):
                                    if val == True:
                                        if idx == 0:
                                            await message.channel.send("**mikkel du har sæd mellem tænderne**")
                                        if idx == 1:
                                            await message.channel.send("**sæbe du et fuckhoved!!**")
                                        if idx == 2:
                                            await message.channel.send("**SIV EMIL !!!**")
                                        if idx == 3:
                                            await message.channel.send("**skal jeg blaf dig en eller hvad nur**")
                                        if idx == 4:
                                            await message.channel.send("**skal du ikke have din middagslur gamle?**")
                                        if idx == 5:
                                            await message.channel.send("**PJ in the house**")
                                        if idx == 6:
                                            await message.channel.send("**ajo skal du ikke lege med tissemandfrej**")
                                        if idx == 7:
                                            await message.channel.send("**BRICKHEAD NELSON**")
                                        if idx == 8:
                                            await message.channel.send("**Long neck looking sonnyboy**")
        delete_files.start()
        bot.run(TOKEN)

