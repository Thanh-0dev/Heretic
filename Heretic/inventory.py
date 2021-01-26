"Fichier pour l'inventaire"

class Inventory():
    """ Définit les informations de l'inventaire """
    def __init__(self, game):
        self.game = game
        self.money = 0
        self.inventory = {
            # Nourriture
            "Burger" : {"number" : 2, "PV" : 10, "price" : 3},
            "Panini" : {"number" : 0, "PV" : 25, "price" : 8},
            "Pizza" : {"number" : 0, "PV" : 50, "price" : 15},
            "Tacos" : {"number" : 0, "PV" : 100, "price" : 25},

            # Boisson
            "Eau" : {"number" : 2, "E" : 10, "price" : 3},
            "Thé" : {"number" : 0, "E" : 25, "price" : 8},
            "Coca" : {"number" : 0, "E" : 50, "price" : 15},
            "Café" : {"number" : 0, "E" : 100, "price" : 25},

            # Boost d'attaque
            "Tic Tac" : {"number" : 0, "Atk" : 3, "Def" : -0, "price" : 5},
            "Miel" : {"number" : 0, "Atk" : 5, "Def" : -0, "price" : 10},
            "Vin" : {"number" : 0, "Atk" : 10, "Def" : -5, "price" : 15},
            "Vodka" : {"number" : 0, "Atk" : 25, "Def" : -10, "price" : 30},

            # Boost de défense
            "Pommade" : {"number" : 0, "Def" : 3, "PV" : 0, "price" : 5},
            "Vitamine C" : {"number" : 0, "Def" : 5, "PV" : 0, "price" : 10},
            "Doliprane" : {"number" : 0, "Def" : 8, "PV" : 0, "price" : 15},
            "Gingembre" : {"number" : 0, "Def" : 15, "PV" : -50, "price" : 30},
        }

    def use_item(self, item_name):
        """ Utilise un objet de l'inventaire """
        item_number = self.inventory[item_name]["number"]

        # Si il n'y a pas 0 fois l'objet demandé
        if item_number > 0:
            # Applique les effets de la nourriture
            if item_name in ["Burger", "Panini", "Pizza", "Tacos"]:
                self.game.player.health += self.inventory[item_name]["PV"]
                if self.game.player.health > self.game.player.max_health:
                    self.game.player.health = self.game.player.max_health

            # Applique les effets de la boisson
            elif item_name in ["Eau", "Thé", "Coca", "Café"]:
                self.game.player.energy += self.inventory[item_name]["E"]
                if self.game.player.energy > self.game.player.max_energy:
                    self.game.player.energy = self.game.player.max_energy

            # Applique les effets du boost d'attaque
            elif item_name in ["Tic Tac", "Miel", "Vin", "Vodka"]:
                self.game.player.attack_boost += self.inventory[item_name]["Atk"]
                self.game.player.defence_boost += self.inventory[item_name]["Def"]

            # Applique les effets du boost de défense
            elif item_name in ["Pommade", "Vitamine C", "Doliprane", "Gingembre"]:
                self.game.player.defence_boost += self.inventory[item_name]["Def"]
                self.game.player.health += self.inventory[item_name]["PV"]

            # Retire une unité de l'objet demandé
            self.inventory[item_name]["number"] = item_number - 1

    def add_item(self, item_name):
        """ Ajoute un objet à l'inventaire """
        item_number = self.inventory[item_name]["number"]

        # Vérifie qu'il n'y a pas plus de 5 exemplaires de l'objet et en ajoute un
        if item_number < 5:
            self.inventory[item_name]["number"] += 1

    def reset_inventory(self):
        """ Remet à zéro l'inventaire """
        self.money = 0
        self.inventory = {
            # Nourriture
            "Burger" : {"number" : 2, "PV" : 10, "price" : 5},
            "Panini" : {"number" : 0, "PV" : 25, "price" : 15},
            "Pizza" : {"number" : 0, "PV" : 50, "price" : 30},
            "Tacos" : {"number" : 0, "PV" : 100, "price" : 50},

            # Boisson
            "Eau" : {"number" : 2, "E" : 10, "price" : 5},
            "Thé" : {"number" : 0, "E" : 25, "price" : 15},
            "Coca" : {"number" : 0, "E" : 50, "price" : 30},
            "Café" : {"number" : 0, "E" : 100, "price" : 50},

            # Boost d'attaque
            "Tic Tac" : {"number" : 0, "Atk" : 3, "Def" : -0, "price" : 10},
            "Miel" : {"number" : 0, "Atk" : 5, "Def" : -0, "price" : 20},
            "Vin" : {"number" : 0, "Atk" : 10, "Def" : -5, "price" : 50},
            "Vodka" : {"number" : 0, "Atk" : 25, "Def" : -10, "price" : 100},

            # Boost de défense
            "Pommade" : {"number" : 0, "Def" : 3, "PV" : 0, "price" : 10},
            "Vitamine C" : {"number" : 0, "Def" : 5, "PV" : 0, "price" : 20},
            "Doliprane" : {"number" : 0, "Def" : 8, "PV" : 0, "price" : 50},
            "Gingembre" : {"number" : 0, "Def" : 15, "PV" : -50, "price" : 100}
        }
