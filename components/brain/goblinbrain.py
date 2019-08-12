import json


class GoblinBrain:

    def __init__(self):
        self.secrets = json.load(open('components/token.json', 'r'))
        self.andrew = 203717140493238273
        print("Brain run by goblin.")
