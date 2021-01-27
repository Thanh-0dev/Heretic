"Fichier pour le combat"
from random import randint

class Fight():
    """ Définit les informations du combat """
    def __init__(self, game):
        self.game = game
        self.enemy = None
        self.phase = 0
        self.action = 0
        self.objects = 0
        self.used = 0
        self.heal = False
        self.boost = {"Atk" : False , "Def" : False}
        self.in_fight = False
        self.dead_player = False
        self.dead_enemy = False

        # Définit les couleurs
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (111, 210, 100)
        self.blue = (0, 0, 255)

    def fight_enemy(self, screen):
        """ Permet de se battre avec l'ennemie rencontré """
        if self.game.player.health == 0 and not self.dead_player:
            self.dead_player = True

        elif self.enemy.health == 0 and not self.dead_enemy:
            self.dead_enemy = True

        # Phase d'affichage
        if self.phase == 0:
            # Affiche toutes les images et textes sur le haut de l'écran
            self.game.display.load_image_position(screen, "assets/menu/home/fill.jpg", 1280, 540, 0, 0)
            self.game.display.load_image_position(screen, "assets/fight/ground.png", 460, 150, 730, 160)
            self.game.display.load_image_position(screen, self.enemy.path, 143, 210, 887, 37)
            self.game.display.load_image_position(screen, "assets/fight/ground.png", 460, 150, 90, 465)
            self.game.display.load_image_position(screen, f"assets/player/{self.game.player.gender}/{self.game.player.gender}_right.png", 191, 280, 227, 296)
            self.combat_update(screen)

            # Affiche toutes les images et textes sur le bas de l'écran
            self.game.display.load_image_position(screen, "assets/lower_screen/drawbar_1.png", 1280, 180, 0, 540)
            self.game.display.load_image_position(screen, "assets/lower_screen/drawbar_2.png", 736, 158, 272, 551)
            self.next_button(screen)
            self.game.display.chat_logs(screen, "", -41)
            self.game.display.chat_logs(screen, f"Vous avez bousculé {self.enemy.name}.", -41, self.black)
            self.game.display.chat_logs(screen, "...", -41, self.black)
            self.game.display.chat_logs(screen, f"{self.enemy.name} vous regarde d'un oeil irrité.", -41, self.black)
            self.game.display.chat_logs(screen, "...", -41, self.black)
            self.game.display.chat_logs(screen, f"{self.enemy.name} vous provoque en duel !", -41, self.red)
            self.phase = -1

        # Phase d'action du joueur
        if self.phase == 1:
            if self.action == 0:
                self.four_choice(screen, "Attaque de base", "Attaque spéciale", "Objets", "Fuite")
                self.show_icon(screen, "basic_attack", "special_attack", "open_bag", "escape", "fight")

            # Le joueur fait une attaque normale
            elif self.action == 1:
                self.game.display.load_image_position(screen, "assets/lower_screen/drawbar_1.png", 1280, 180, 0, 540)
                self.next_button(screen)
                luck_player = randint(0, 100)
                self.game.display.chat_logs(screen, "", -41)
                self.game.display.chat_logs(screen, f"{self.game.player.name} attaque avec {self.game.player.weapon}.", -41)
                self.game.display.chat_logs(screen, "...", -41)

                # Fait une attaque réussie à 85%
                if luck_player < 90 and luck_player > 5:
                    # Calcule et affiche les dégats donnés
                    amount_dealt = int(self.game.player.attack + self.game.player.attack_boost - self.enemy.defence)

                # Fait un coup critique à 10%
                elif luck_player >= 90:
                    # Calcule et affiche les dégats donnés
                    amount_dealt = int((self.game.player.attack + self.game.player.attack_boost - self.enemy.defence) * 2)
                    self.game.display.chat_logs(screen, "Coup critique !", -41, self.red)

                # Fait un échec à 5%
                elif luck_player <= 5:
                    self.game.display.chat_logs(screen, f"Ebloui par la lumière, {self.game.player.name} perd la vision pendant un bref instant.", -41)
                    self.game.display.chat_logs(screen, f"{self.enemy.name} a esquivé votre attaque.", -41)

                # Enregistre et affiche les dégats infligé
                if luck_player > 5:
                    if amount_dealt < 0:
                        amount_dealt = 0
                    self.enemy.damage(amount_dealt)
                    self.combat_update(screen, "enemy")
                    self.game.display.chat_logs(screen, f"Vous avez infligé {amount_dealt} points de dégats à {self.enemy.name}.", -41)
                    self.game.display.chat_logs(screen, f"{self.enemy.name} n'a plus que {self.enemy.health} points de vie.", -41)
                self.action = 0
                self.phase = -2

            # Le joueur rentre dans les attaques spéciales
            elif self.action == 2:
                self.game.skills.skills_update()
                self.four_choice(screen, list(self.game.skills.skills)[0], list(self.game.skills.skills)[1], list(self.game.skills.skills)[2], list(self.game.skills.skills)[3], -10)
                self.game.display.load_image_position(screen, "assets/fight/special_attack.png", 164, 147, 22, 557)
                self.desc_skill(screen, list(self.game.skills.skills)[0], list(self.game.skills.skills)[1], list(self.game.skills.skills)[2], list(self.game.skills.skills)[3])
                self.show_icon(screen, list(self.game.skills.skills)[0], list(self.game.skills.skills)[1], list(self.game.skills.skills)[2], list(self.game.skills.skills)[3], "skills")
                self.previous_button(screen)

                if self.used != 0:
                    skill_name = list(self.game.skills.skills)[self.used-1]
                    self.game.display.load_image_position(screen, "assets/lower_screen/drawbar_1.png", 1280, 180, 0, 540)
                    self.next_button(screen)

                    if skill_name in ["?", "??", "???", "????"]:
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "Vous n'avez pas encore débloqué cette attaque spéciale.", -41)
                        self.game.display.chat_logs(screen, f"Passez en année H{self.used+1} pour la débloquer.", -41)
                        self.phase = -3

                    elif self.game.player.energy < self.game.skills.skills[skill_name]["cost"]:
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "Vous n'avez pas assez d'énergie pour utilser cette attaque spéciale.", -41)
                        self.phase = -3

                    elif self.game.player.energy >= self.game.skills.skills[skill_name]["cost"]:
                        self.game.player.energy -= self.game.skills.skills[skill_name]["cost"]
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, f"{self.game.player.name} utilise l'attaque spéciale {skill_name}.", -41)
                        self.game.display.chat_logs(screen, self.game.skills.skills[skill_name]["desc"], -41)

                        if self.game.player.role == "Designer" and self.used in [1, 2]:
                            if self.used == 1:
                                if self.game.player.weapon != "un wireframe d'épée":
                                    self.game.player.weapon = "un wireframe d'épée"
                                    number = self.game.skills.skills["Wireframe d'épée"]["Atk"]
                                    self.game.player.attack_boost += number
                                    self.game.display.chat_logs(screen, f"L'attaque de {self.game.player.name} augmente de {number} jusqu'à la fin du combat.", -41)

                                else:
                                    self.game.display.chat_logs(screen, f"L'attaque de {self.game.player.name} ne change pas ayant déja un wireframe d'épée en main.", -41)

                            elif self.used == 2:
                                if not self.game.player.shield:
                                    self.game.player.shield = True
                                    number = self.game.skills.skills["Prototype de bouclier"]["Def"]
                                    self.game.player.defence_boost += number
                                    self.game.display.chat_logs(screen, f"La défense de {self.game.player.name} augmente de {number} jusqu'à la fin du combat.", -41)

                                else:
                                    self.game.display.chat_logs(screen, f"L'attaque de {self.game.player.name} ne change pas ayant déja un prototype de bouclier en main.", -41)

                            self.phase = -2

                        else:
                            luck_player = randint(0, 100)
                            skill_damage = int(self.game.skills.skills[skill_name]["damage"] * (self.game.player.attack + self.game.player.attack_boost))

                            # Fait une attaque réussie à 85%
                            if luck_player < 90 and luck_player > 5:
                                # Calcule et affiche les dégats donnés
                                amount_dealt = int(skill_damage - self.enemy.defence)

                            # Fait un coup critique à 10%
                            elif luck_player >= 90:
                                # Calcule et affiche les dégats donnés
                                amount_dealt = int((skill_damage - self.enemy.defence) * 2)
                                self.game.display.chat_logs(screen, "Coup critique !", -41, self.red)

                            # Fait un échec à 5%
                            elif luck_player <= 5:
                                self.game.display.chat_logs(screen, f"Ebloui par la lumière, {self.game.player.name} perd la vision pendant un bref instant.", -41)
                                self.game.display.chat_logs(screen, f"{self.enemy.name} a esquivé votre attaque spéciale.", -41)

                            # Enregistre et affiche les dégats infligé
                            if luck_player > 5:
                                if amount_dealt < 0:
                                    amount_dealt = 0
                                self.enemy.damage(amount_dealt)

                                if self.used == 3:
                                    self.phase = -3

                                self.combat_update(screen, "enemy")
                                self.game.display.chat_logs(screen, f"Vous avez infligé {amount_dealt} points de dégats à {self.enemy.name}.", -41)
                                self.game.display.chat_logs(screen, f"{self.enemy.name} n'a plus que {self.enemy.health} points de vie.", -41)

                            if self.used == 4 and self.game.player.role == "Designer":
                                self.game.player.health = 1

                            self.phase = -2
                        self.combat_update(screen, "player")
                    self.action = 0
                    self.used = 0

            # Le joueur rentre dans l'inventaire
            elif self.action == 3:

                # Affichage des différentes catégories
                if self.objects == 0:
                    self.four_choice(screen, "Nouritture", "Boisson", "Boost d'attaque", "Boost de défense")
                    self.game.display.load_image_position(screen, "assets/fight/open_bag.png", 164, 147, 22, 557)
                    self.show_icon(screen, "food", "drinks", "attack_boost", "defence_boost", "fight")
                    self.previous_button(screen)

                # Affichage de la nourriture
                if self.objects == 1:
                    self.four_choice(screen, "Burger", "Panini", "Pizza", "Tacos", -10)
                    self.game.display.load_image_position(screen, "assets/fight/open_bag.png", 164, 147, 22, 557)
                    self.desc_item(screen, "Burger", "Panini", "Pizza", "Tacos")
                    self.show_icon(screen, "Burger", "Panini", "Pizza", "Tacos", "inventory")
                    self.previous_button(screen)

                # Affichage des boissons
                elif self.objects == 2:
                    self.four_choice(screen, "Eau", "Thé", "Coca", "Café", -10)
                    self.game.display.load_image_position(screen, "assets/fight/open_bag.png", 164, 147, 22, 557)
                    self.desc_item(screen, "Eau", "Thé", "Coca", "Café")
                    self.show_icon(screen, "Eau", "Thé", "Coca", "Café", "inventory")
                    self.previous_button(screen)

                # Affichage des boosts d'attaques
                elif self.objects == 3:
                    self.four_choice(screen, "Tic Tac", "Miel", "Vin", "Vodka", -10)
                    self.game.display.load_image_position(screen, "assets/fight/open_bag.png", 164, 147, 22, 557)
                    self.desc_item(screen, "Tic Tac", "Miel", "Vin", "Vodka", 3)
                    self.show_icon(screen, "Tic Tac", "Miel", "Vin", "Vodka", "inventory")
                    self.previous_button(screen)

                # Affichage des boosts de défense
                elif self.objects == 4:
                    self.four_choice(screen, "Pommade", "Vitamine C", "Doliprane", "Gingembre", -10)
                    self.game.display.load_image_position(screen, "assets/fight/open_bag.png", 164, 147, 22, 557)
                    self.desc_item(screen, "Pommade", "Vitamine C", "Doliprane", "Gingembre", 4)
                    self.show_icon(screen, "Pommade", "Vitamine C", "Doliprane", "Gingembre", "inventory")
                    self.previous_button(screen)

                # Utilise l'objet si il y en a au moins 1
                if self.used != 0:
                    item_name = list(self.game.inventory.inventory)[self.objects * 4 + self.used - 5]
                    item_number = self.game.inventory.inventory[item_name]["number"]
                    self.game.display.load_image_position(screen, "assets/lower_screen/drawbar_1.png", 1280, 180, 0, 540)
                    self.next_button(screen)
                    self.game.display.chat_logs(screen, "", -41)
                    self.game.display.chat_logs(screen, "", -41)

                    if item_name not in ["Vin", "Vodka", "Gingembre"]:
                        self.game.display.chat_logs(screen, "", -41)

                    # Si c'est un boost d'attaque et qu'il est déja booster, ne l'utilise pas
                    if item_number != 0 and self.objects == 3 and self.boost["Atk"]:
                        self.phase = -3
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, f"{self.game.player.name} a déja boosté son attaque pendant le combat.", -41)

                    # Si c'est un boost de défense et qu'il est déja booster, ne l'utilise pas
                    elif item_number != 0 and self.objects == 4 and self.boost["Def"]:
                        self.phase = -3
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, f"{self.game.player.name} a déja boosté sa défense pendant le combat.", -41)

                    elif item_number != 0:
                        if item_number <= 2 and item_number > 0:
                            self.game.display.chat_logs(screen, f"{self.game.player.name} utilise l'objet {item_name}, vous n'en avez plus que {item_number - 1} exemplaire.", -41)

                        elif item_number > 2:
                            self.game.display.chat_logs(screen, f"{self.game.player.name} utilise l'objet {item_name}, vous n'en avez plus que {item_number - 1} exemplaires.", -41)

                        if self.objects == 1:
                            effect = self.game.inventory.inventory[item_name]["PV"]

                            if self.game.player.health == self.game.player.max_health:
                                self.game.display.chat_logs(screen, f"Les points de vie de {self.game.player.name} sont déja au maximum, l'objet {item_name} ne fait rien.", -41)

                            elif self.game.player.health + effect <= self.game.player.max_health:
                                self.game.display.chat_logs(screen, f"{self.game.player.name} récupère {effect} points de vie.", -41)

                            elif self.game.player.health + effect > self.game.player.max_health:
                                self.game.display.chat_logs(screen, f"{self.game.player.name} récupère {self.game.player.max_health - self.game.player.health} points de vie.", -41)

                        elif self.objects == 2:
                            effect = self.game.inventory.inventory[item_name]["E"]

                            if self.game.player.energy == self.game.player.max_energy:
                                self.game.display.chat_logs(screen, f"Les points de vie de {self.game.player.name} sont déja au maximum.", -41)

                            elif self.game.player.energy + effect <= self.game.player.max_energy:
                                self.game.display.chat_logs(screen, f"{self.game.player.name} récupère {effect} points d'énergie.", -41)

                            elif self.game.player.energy + effect > self.game.player.max_energy:
                                self.game.display.chat_logs(screen, f"{self.game.player.name} récupère {self.game.player.max_energy - self.game.player.energy} points d'énergie.", -41)

                        elif self.objects == 3:
                            effect = self.game.inventory.inventory[item_name]["Atk"]
                            self.game.display.chat_logs(screen, f"{self.game.player.name} se sent plus fort et augmente son attaque de {effect}.", -41)
                            self.boost["Atk"] = True

                            if item_name in ["Vin", "Vodka"]:
                                effect = self.game.inventory.inventory[item_name]["Def"]
                                self.game.display.chat_logs(screen, f"{self.game.player.name} est négligent et sa défense baisse de {effect}.", -41)

                        elif self.objects == 4:
                            effect = self.game.inventory.inventory[item_name]["Def"]
                            self.game.display.chat_logs(screen, f"{self.game.player.name} se sent plus résistant et augmente sa défense de {effect}.", -41)
                            self.boost["Def"] = True

                            if item_name == "Gingembre":
                                effect = self.game.inventory.inventory[item_name]["PV"]

                                if self.game.player.health + effect > 0:
                                    self.game.display.chat_logs(screen, f"{self.game.player.name} se sent plus chaud et perd {effect} points de vie.", -41)

                                elif self.game.player.health + effect <= 0:
                                    self.game.display.chat_logs(screen, f"{self.game.player.name} se sent plus chaud et perd {self.game.player.health} points de vie.", -41)
                                    self.game.display.chat_logs(screen, f"{self.game.player.name} s'est suicidé sans le savoir en mangeant du gingembre.", -41)
                                    self.boost["Def"] = True
                        self.game.inventory.use_item(item_name)
                        self.combat_update(screen, "player")
                        self.phase = -2
                        self.action = 0
                        self.objects = 0

                    else:
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, "", -41)
                        self.game.display.chat_logs(screen, f"Vous avez 0 exemplaire de l'objet {item_name} dans votre inventaire.", -41)
                        self.phase = -3

                    self.used = 0

            # Le joueur fuit
            elif self.action == 4:
                self.enemy.health = self.enemy.max_health
                self.in_fight = False
                self.game.is_playing = True
                self.game.display.lower_screen(screen)
                self.game.display.chat_logs(screen, "")
                self.game.display.chat_logs(screen, "Vous avez fuit le combat.")
                self.game.display.chat_logs(screen, f"{self.enemy.name} vous crache dessus.")
                self.game.player.rect.x -= 100
                self.action = 0

        # Phase d'attaque de l'ennemi
        if self.phase == 2:
            self.next_button(screen)
            luck_enemy = randint(0, 100)

            # L'ennemie à 50% de chance de se soigner 25% de ses points de vie
            if luck_enemy <= 50 and self.enemy.health <= self.enemy.max_health * 0.5 and not self.heal:
                heal = int(self.enemy.max_health * 0.25)
                self.enemy.health += heal
                self.combat_update(screen, "enemy")
                self.game.display.chat_logs(screen, "", -41)
                self.game.display.chat_logs(screen, "", -41)
                self.game.display.chat_logs(screen, "", -41)
                self.game.display.chat_logs(screen, f"{self.enemy.name} sort un petit encas et commence à le déguster.", -41)
                self.game.display.chat_logs(screen, f"{self.enemy.name} récupère {heal} points de vie.", -41)
                self.heal = True

            else:
                luck_enemy = randint(0, 100)

                # Fait une attaque réussie à 85%
                if luck_enemy < 90 and luck_enemy > 5:
                    amount_received = int(self.enemy.attack - (self.game.player.defence + self.game.player.defence_boost))
                    self.game.display.chat_logs(screen, "", -41)
                    self.game.display.chat_logs(screen, "", -41)
                    self.game.display.chat_logs(screen, f"{self.enemy.name} attaque avec {self.enemy.weapon}", -41)

                # Fait un coup critique à 10%
                elif luck_enemy >= 90:
                    amount_received = int((self.enemy.attack - (self.game.player.defence + self.game.player.defence_boost)) * 2)
                    self.game.display.chat_logs(screen, f"{self.enemy.name} attaque avec {self.enemy.weapon}", -41)
                    self.game.display.chat_logs(screen, "Coup critique !", -41, self.red)
                    self.game.display.chat_logs(screen, "", -41)

                # Rate son attaque à 5%
                elif luck_enemy >= 5:
                    self.game.display.chat_logs(screen, "", -41)
                    self.game.display.chat_logs(screen, "", -41)
                    self.game.display.chat_logs(screen, f"{self.enemy.name} attaque avec {self.enemy.weapon}", -41)
                    self.game.display.chat_logs(screen, f"Eblouie par la lumière, {self.enemy.name} perd la vision pendant un bref instant.", -41)
                    self.game.display.chat_logs(screen, "Vous avez esquivé son attaque.", -41)

                # Enregistre et affiche les dégats infligé
                if luck_enemy > 5:
                    if amount_received < 0:
                        amount_received = 0
                    self.game.player.damage(amount_received)
                    self.combat_update(screen, "player")
                    self.game.display.chat_logs(screen, f"{self.enemy.name} attaque !", -41)
                    self.game.display.chat_logs(screen, f"Il vous a infligé {amount_received} points de dégats.", -41)
            self.phase = -3

        # L'ennemie est mort
        if self.phase == 777 and self.dead_enemy and self.enemy.name not in ["M. Martinez", "M. Bourienne"]:
            self.heal = False
            self.boost["Atk"] = False
            self.boost["Def"] = False
            self.game.player.attack_boost, self.game.player.defence_boost = (0, 0)
            self.game.skills.weapons()
            self.game.player.xp += self.enemy.xp
            self.game.inventory.money += self.enemy.money
            self.game.player.level_update()
            self.combat_update(screen, "player")
            self.game.display.chat_logs(screen, "", -41)
            self.game.display.chat_logs(screen, "", -41)
            self.game.display.chat_logs(screen, f"Vous avez vaincu {self.enemy.name}.", -41)
            self.game.display.chat_logs(screen, f"Vous avez gagné {self.enemy.xp} points d'expérience et {self.enemy.money}€.", -41)
            if self.game.player.level_up:
                self.game.display.chat_logs(screen, f"Vous êtes passé au niveau {self.game.player.level} !", -41, self.blue)
                if self.game.player.rank_change:
                    self.game.display.chat_logs(screen, f"Allez voir votre formateur pour passer en H{self.game.player.rank + 1} et débloquer une nouvelle attaque spéciale.", -41, self.blue)
                self.game.player.level_up = False
            self.game.display.chat_logs(screen, f"Encore {self.game.player.max_xp - self.game.player.xp} points d'expérience avant le prochain niveau.", -41)
            self.game.current_room.enemy_sprites_x.remove(self.enemy)
            self.game.current_room.enemy_sprites_y.remove(self.enemy)
            self.game.save.save_game()
            self.phase = -777

        # Le boss est mort
        elif self.phase == 777 and self.dead_enemy and self.enemy.name in ["M. Martinez", "M. Bourienne"]:
            self.game.current_room.enemy_sprites_x.remove(self.enemy)
            self.boost["Atk"] = False
            self.boost["Def"] = False
            self.game.player.attack_boost, self.game.player.defence_boost = (0, 0)
            self.game.skills.weapons()
            self.game.player.xp += self.enemy.xp
            self.game.inventory.money += self.enemy.money
            self.game.player.level_update()
            self.combat_update(screen, "player")
            self.game.map_y, self.game.map_x = (5, 2)
            self.game.player.rect.x, self.game.player.rect.y = (1180, 95)
            self.game.save.save_game()
            self.game.display.chat_logs(screen, f"Vous avez vaincu {self.enemy.name}.", -41)
            self.game.display.chat_logs(screen, f"Félicitation {self.game.player.name} vous avez réaliser un exploit en mettant fin à cette ère.", -41)
            self.game.display.chat_logs(screen, "Grâce à vous, Hetic retrouvera la paix qu'elle à d'antant eu.", -41)
            self.game.display.chat_logs(screen, f"{self.game.player.name} a obtenu son diplome du cursus Grande Ecole.", -41, self.blue)
            self.game.display.chat_logs(screen, "----------------------------------------Fin du jeu, merci d'avoir joué !----------------------------------------", -41, self.blue)
            self.phase = 13062002

        # Le joueur est mort
        if self.phase == 666 and self.dead_player:
            self.boost["Atk"] = False
            self.boost["Def"] = False
            self.game.display.chat_logs(screen, f"{self.game.player.name} n'a plus de points de vie.", -41)
            self.game.display.chat_logs(screen, "Vous avez été vaincu.", -41)
            self.game.display.chat_logs(screen, f"L'aventure de {self.game.player.name} au niveau {self.game.player.level} et au rang H{self.game.player.rank} s'arrête ici.", -41)
            self.game.display.chat_logs(screen, "", -41)
            self.game.display.chat_logs(screen, "Retour vers le menu", -41, self.green)
            self.enemy.health = self.enemy.max_health
            if self.game.player.mode == "Hardcore":
                self.enemy.reverse_hardcore_rage()
            self.phase = -666

    def combat_update(self, screen, who="both"):
        """ Affiche les status de l'ennemie et du joueur """
        if who == "enemy" or who == "both":
            self.game.display.load_image_position(screen, "assets/fight/enemy_status.png", 441, 92, 49, 68)
            self.game.display.message_display(screen, self.enemy.name, 24, 65, 83, self.black)
            self.game.display.message_display_center(screen, f"Niveau {self.enemy.level}", 24, 398, 93, self.black)
            if self.enemy.health < 0:
                self.enemy.health = 0
            self.enemy.update_stats_bar(screen)
            self.game.display.message_display_center(screen, f"{self.enemy.health}/{self.enemy.max_health}", 24, 408, 130, self.black)

        if who == "player" or who == "both":
            self.game.display.load_image_position(screen, "assets/fight/player_status.png", 447, 133, 777, 387)
            self.game.display.message_display(screen, self.game.player.name, 24, 829, 402, self.black)
            self.game.display.message_display(screen, f"Niveau {self.game.player.level} - H{self.game.player.rank}", 24, 1105, 403, self.black)
            if self.game.player.health < 0:
                self.game.player.health = 0
            self.game.player.update_stats_bar(screen, "fight")
            self.game.display.message_display_center(screen, f"{self.game.player.health}/{self.game.player.max_health}", 24, 1172, 440, self.black)
            self.game.display.message_display_center(screen, f"{self.game.player.energy}/{self.game.player.max_energy}", 24, 1172, 477, self.black)

    def next_button(self, screen):
        """ Affiche le bouton suivant """
        self.game.display.load_image_position(screen, "assets/fight/button.png", 120, 30, 1084, 679)
        self.game.display.message_display_center(screen, "Suivant", 24, 1144, 694, self.black)

    def previous_button(self, screen):
        """ Affiche le bouton précédent """
        self.game.display.load_image_position(screen, "assets/fight/button.png", 120, 30, 1084, 629)
        self.game.display.message_display_center(screen, "Précédent", 24, 1144, 644, self.black)

    def four_choice(self, screen, first_choice, second_choice, third_choice, fourth_choice, y_offset = 0):
        """ Affiche quatres boutons avec leur texte centré """
        self.game.display.load_image_position(screen, "assets/lower_screen/drawbar_1.png", 1280, 180, 0, 540)
        self.game.display.load_image_position(screen, "assets/fight/button.png", 420, 60, 210, 560)
        self.game.display.message_display_center(screen, first_choice, 24, 420, 590 + y_offset, self.black)
        self.game.display.load_image_position(screen, "assets/fight/button.png", 420, 60, 650, 560)
        self.game.display.message_display_center(screen, second_choice, 24, 865, 590 + y_offset, self.black)
        self.game.display.load_image_position(screen, "assets/fight/button.png", 420, 60, 210, 640)
        self.game.display.message_display_center(screen, third_choice, 24, 420, 670 + y_offset, self.black)
        self.game.display.load_image_position(screen, "assets/fight/button.png", 420, 60, 650, 640)
        self.game.display.message_display_center(screen, fourth_choice, 24, 865, 670 + y_offset, self.black)

    def desc_skill(self, screen, skill_name1, skill_name2, skill_name3, skill_name4):
        """ Affiche le coût des attaques spéciales et si le joueur n'a pas assez d'énergie passe le nom et le nombre en rouge"""
        cost = "cost"
        if skill_name1 != "?":
            if self.game.skills.skills[skill_name1][cost] <= self.game.player.energy:
                self.game.display.message_display_center(screen, f"{self.game.skills.skills[skill_name1][cost]} E", 24, 420, 600, self.black)
            else:
                self.game.display.load_image_position(screen, "assets/fight/button.png", 420, 60, 210, 560)
                self.game.display.message_display_center(screen, f"{self.game.skills.skills[skill_name1][cost]} E", 24, 420, 600, self.red)
                self.game.display.message_display_center(screen, skill_name1, 24, 420, 580, self.red)
        if skill_name2 != "??":
            if self.game.skills.skills[skill_name2][cost] <= self.game.player.energy:
                self.game.display.message_display_center(screen, f"{self.game.skills.skills[skill_name2][cost]} E", 24, 865, 600, self.black)
            else:
                self.game.display.load_image_position(screen, "assets/fight/button.png", 420, 60, 650, 560)
                self.game.display.message_display_center(screen, f"{self.game.skills.skills[skill_name2][cost]} E", 24, 865, 600, self.red)
                self.game.display.message_display_center(screen, skill_name2, 24, 865, 580, self.red)
        if skill_name3 != "???":
            if self.game.skills.skills[skill_name3][cost] <= self.game.player.energy:
                self.game.display.message_display_center(screen, f"{self.game.skills.skills[skill_name3][cost]} E", 24, 420, 680, self.black)
            else:
                self.game.display.load_image_position(screen, "assets/fight/button.png", 420, 60, 210, 640)
                self.game.display.message_display_center(screen, f"{self.game.skills.skills[skill_name3][cost]} E", 24, 420, 680, self.red)
                self.game.display.message_display_center(screen, skill_name3, 24, 420, 660, self.red)
        if skill_name4 != "????":
            if self.game.skills.skills[skill_name4][cost] <= self.game.player.energy:
                self.game.display.message_display_center(screen, f"{self.game.skills.skills[skill_name4][cost]} E", 24, 865, 680, self.black)
            else:
                self.game.display.load_image_position(screen, "assets/fight/button.png", 420, 60, 650, 640)
                self.game.display.message_display_center(screen, f"{self.game.skills.skills[skill_name4][cost]} E", 24, 865, 680, self.red)
                self.game.display.message_display_center(screen, skill_name4, 24, 865, 660, self.red)

    def desc_item(self, screen, item_name1, item_name2, item_name3, item_name4, negative = 0):
        """ Affiche le nombre d'exemplaire des objets, leur effets """
        # Affiche le nombre d'exemplaire des objets
        if self.game.inventory.inventory[item_name1]["number"] != 0:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name1]["number"]), 24, 420, 600, self.black)
        else:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name1]["number"]), 24, 420, 600, self.red)
        if self.game.inventory.inventory[item_name2]["number"] != 0:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name2]["number"]), 24, 865, 600, self.black)
        else:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name2]["number"]), 24, 865, 600, self.red)
        if self.game.inventory.inventory[item_name3]["number"] != 0:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name3]["number"]), 24, 420, 680, self.black)
        else:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name3]["number"]), 24, 420, 680, self.red)
        if self.game.inventory.inventory[item_name4]["number"] != 0:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name4]["number"]), 24, 865, 680, self.black)
        else:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name4]["number"]), 24, 865, 680, self.red)

        # Affiche les effets des différents objets
        effect = list(list(self.game.inventory.inventory.values())[(self.objects - 1) * 4])[1]
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name1][effect]} {effect}", 24, 520, 570, self.green)
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name2][effect]} {effect}", 24, 965, 570, self.green)
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name3][effect]} {effect}", 24, 520, 650, self.green)
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name4][effect]} {effect}", 24, 965, 650, self.green)
        if negative == 3:
            side_effect = list(list(self.game.inventory.inventory.values())[(self.objects - 1) * 4])[2]
            self.game.display.message_display(screen, f"   {self.game.inventory.inventory[item_name3][side_effect]} {side_effect}", 24, 520, 670, self.red)
            self.game.display.message_display(screen, f"   {self.game.inventory.inventory[item_name4][side_effect]} {side_effect}", 24, 965, 670, self.red)
        elif negative == 4:
            side_effect = list(list(self.game.inventory.inventory.values())[(self.objects - 1) * 4])[2]
            self.game.display.message_display(screen, f"   {self.game.inventory.inventory[item_name4][side_effect]} {side_effect}", 24, 965, 670, self.red)

    def show_icon(self, screen, icon_name1, icon_name2, icon_name3, icon_name4, category):
        """ Affiche l'image des objets """
        if icon_name1 != "?":
            self.game.display.load_image_position(screen, f"assets/{category}/{icon_name1}.png", 50, 50, 280, 566)
        if icon_name2 != "??":
            self.game.display.load_image_position(screen, f"assets/{category}/{icon_name2}.png", 50, 50, 720, 566)
        if icon_name3 != "???":
            self.game.display.load_image_position(screen, f"assets/{category}/{icon_name3}.png", 50, 50, 280, 646)
        if icon_name4 != "????":
            self.game.display.load_image_position(screen, f"assets/{category}/{icon_name4}.png", 50, 50, 720, 646)

    def reset(self):
        """ Remet à zéro le combat """
        self.enemy = None
        self.phase = 0
        self.action = 0
        self.objects = 0
        self.used = 0
        self.heal = False
        self.boost = {"Atk" : False , "Def" : False}
        self.in_fight = False
        self.dead_player = False
        self.dead_enemy = False
