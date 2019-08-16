import MySQLdb as sql
import json

class WarframeDB:
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.passwd = 'default'
        self.db = 'discord'
        self.weapon_table = 'goblin_weapon'
        self.frame_table = 'goblin_frame'
        self.port = 3306
        self.connection = sql.connect(host=self.host,
                    user=self.user,
                    passwd=self.passwd,
                    db=self.db,
                    port=self.port)

        self.cursor = sql.cursors.Cursor(connection=self.connection)
        print(self.cursor)

    def db_health(self, table):

        query = f"""SELECT COUNT(*) FROM {table};"""
        self.cursor.execute(query=query)
        result = self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()
        return result[0][0]

    def update_weapons(self):
        with open('./components/warframe/data/weapons.json', 'r') as json_file:
            weapons = json.load(json_file)

        for w in weapons:
            query = f"""INSERT INTO {self.db}.{self.weapon_table} (name, category) VALUES ("{w['name']}", "{w['category']}");
            """
            self.cursor.execute(query=query)
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def update_frames(self):
        with open('./components/warframe/data/frames.json', 'r') as json_file:
            frames = json.load(json_file)

        for f in frames:
            query = f"""INSERT INTO {self.db}.{self.frame_table} 
            (name, ability_1, ability_2, ability_3, ability_4) VALUES ("{f['name']}", "{f['abilities'][0]['name']}", "{f['abilities'][1]['name']}", "{f['abilities'][2]['name']}", "{f['abilities'][3]['name']}");
            """
            self.cursor.execute(query=query)
            self.connection.commit()
        self.cursor.close()
        self.connection.close()