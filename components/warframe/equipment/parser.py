from components.warframe.equipment import *
import json
import requests
import random

class Parser:
    def __init__(self):
        print("Getting the weapons ready...")
        self.weapons = json.loads(requests.get(url='https://ws.warframestat.us/weapons').content)
        print("Getting the warframes ready...")
        self.frames = json.loads(requests.get(url='https://ws.warframestat.us/warframes').content)
        print("Frames and weapons online!")

    def primary(self):
        pass

    def secondary(self):
        pass

    def melee(self):
        pass

    async def oldFrame(self):
        frame = random.randint(0, len(self.frames))
        frame_name = self.frames[frame]['name']
        random_frame = "Use " + frame_name + " this mission!"
        return random_frame

    async def oldWeapon(self):
        weapon = random.randint(0, len(self.weapons))
        weapon_name = self.weapons[weapon]['name']
        random_weapon = "Use the weapon " + weapon_name + "!"
        return random_weapon


