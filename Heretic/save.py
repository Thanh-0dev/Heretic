"Fichier permettant de sauvegarder la progression"
from pickle import dump,load
import os.path

class Save():
    """ Définit les informations à sauvegarder """
    def __init__(self, game):
        self.game = game
        self.player_information = ()
        self.player_inventory = {}
        self.name = None
        self.mode = None
        self.role = None
        self.level = None
        self.rank = None

    def save_game(self):
        """ Sauvegarde toutes les informations de la partie """
        self.player_information = (
            self.game.player.gender,
            self.game.player.name,
            self.game.player.level,
            self.game.player.xp,
            self.game.player.max_xp,
            self.game.player.rank,
            self.game.player.role,
            self.game.player.mode,
            self.game.player.health,
            self.game.player.max_health,
            self.game.player.energy,
            self.game.player.max_energy,
            self.game.player.attack,
            self.game.player.defence,
            self.game.player.rect.x,
            self.game.player.rect.y,
            self.game.map_x,
            self.game.map_y,
            self.game.display.text_log1,
            self.game.display.text_log2,
            self.game.display.text_log3,
            self.game.display.text_log4,
            self.game.display.text_log5,
            self.game.display.color1,
            self.game.display.color2,
            self.game.display.color3,
            self.game.display.color4,
            self.game.display.color5,
            self.game.inventory.money,
            self.game.player.rank_change,
            self.game.skills.skills
        )

        if not os.path.isdir("save"):
            os.mkdir("save")
        if os.path.isfile("save/player_save.heretic"):
            os.remove("save/player_save.heretic")
            os.remove("save/inventory_save.heretic")
        dump(self.player_information, open("save/player_save.heretic", "wb"))
        dump(self.game.inventory.inventory, open("save/inventory_save.heretic", "wb"))

    def load_save(self):
        """ Charge les informations de la sauvegarde """
        self.game.player.gender = self.player_information[0]
        self.game.player.name = self.player_information[1]
        self.game.player.level = self.player_information[2]
        self.game.player.xp = self.player_information[3]
        self.game.player.max_xp = self.player_information[4]
        self.game.player.rank = self.player_information[5]
        self.game.player.role = self.player_information[6]
        self.game.player.mode = self.player_information[7]
        self.game.player.health = self.player_information[8]
        self.game.player.max_health = self.player_information[9]
        self.game.player.energy = self.player_information[10]
        self.game.player.max_energy = self.player_information[11]
        self.game.player.attack = self.player_information[12]
        self.game.player.defence = self.player_information[13]
        self.game.player.rect.x = self.player_information[14]
        self.game.player.rect.y = self.player_information[15]
        self.game.map_x = self.player_information[16]
        self.game.map_y = self.player_information[17]
        self.game.inventory.money = self.player_information[28]
        self.game.player.rank_change = self.player_information[29]
        self.game.skills.skills = self.player_information[30]
        self.game.inventory.inventory = load(open("save/inventory_save.heretic", "rb"))

    def load_chat(self):
        """ Charge les anciens messages de la sauvegardes """
        self.game.display.text_log1 = self.player_information[19]
        self.game.display.text_log2 = self.player_information[20]
        self.game.display.text_log3 = self.player_information[21]
        self.game.display.text_log4 = self.player_information[22]
        self.game.display.color1 = self.player_information[24]
        self.game.display.color2 = self.player_information[25]
        self.game.display.color3 = self.player_information[26]
        self.game.display.color4 = self.player_information[27]

    def show_save(self):
        """ Permet d'afficher les informations de la sauvegarde sur le menu """
        self.player_information = load(open("save/player_save.heretic", "rb"))
        self.name = self.player_information[1]
        self.level = self.player_information[2]
        self.rank = self.player_information[5]
        self.role = self.player_information[6]
        self.mode = self.player_information[7]
