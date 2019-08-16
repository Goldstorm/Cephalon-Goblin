from components.brain.goblinbrain import GoblinBrain
import json
import requests
import random


class Parser(GoblinBrain):
    def __init__(self):
        super().__init__()
        print("Getting the weapons ready...")
        self.weapons = json.loads(requests.get(url='https://ws.warframestat.us/weapons').content)
        with open(f'{self.path}warframe/data/weapons.json', 'w') as outfile:
            json.dump(self.weapons, outfile)
        # WarframeDB().updateWeapons(self.weapons)
        print("Getting the warframes ready...")
        self.frames = json.loads(requests.get(url='https://ws.warframestat.us/warframes').content)
        with open(f'{self.path}warframe/data/frames.json', 'w') as outfile:
            json.dump(self.frames, outfile)
        print("Frames and weapons online!")

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
