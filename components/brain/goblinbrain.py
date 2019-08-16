from dataclasses import dataclass
import json
import requests
import random

from components.warframe.equipment.importer import WarframeDB

class GoblinBrain(object):

    def __init__(self):
        self.secrets = json.load(open('components/token.json', 'r'))
        self.andrew = 203717140493238273
        import os
        if os.name == 'nt':
            self.path = './components/'
        else:
            self.path = '/opt/goblin/components/'
        print("Brain run by goblin.")
        self.goblin_says = [
            "Ketchup good! Goblin wife bad.",
            "No! Not my face!",
            "Operator like this face?",
            "Operator not like last face?",
            "Operator take a !chance next mission? No bamboozle.",
            "37"
        ]
        print("Getting the weapons ready...")
        self.weapons = json.loads(requests.get(url='https://ws.warframestat.us/weapons').content)
        with open(f'{self.path}warframe/data/weapons.json', 'w') as outfile:
            json.dump(self.weapons, outfile)
        weapons = WarframeDB().db_health('goblin_weapon')
        if weapons == 0:
            WarframeDB().update_weapons()
            print("Weapons updated and online!")
        else:
            print("Weapons do not need to be updated.")
        print("Getting the warframes ready...")
        self.frames = json.loads(requests.get(url='https://ws.warframestat.us/warframes').content)
        with open(f'{self.path}warframe/data/frames.json', 'w') as outfile:
            json.dump(self.frames, outfile)
        frames = WarframeDB().db_health('goblin_frame')
        if frames == 0:
            WarframeDB().update_frames()
            print("Frames updated and online!")
        else:
            print("Frames do not need to be updated.")
        print("Goblin have data. Ready to serve.")

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


@dataclass
class GoblinDataClass:
    category: str
    weapon_name: str
    frame: str
