"Fichier pour les fonctions d'affichage"
import pygame

class Display():
    """ Définit l'affichage des textures """
    def __init__(self, game):
        self.game = game
        # Définit les couleurs
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (111, 210, 100)

        self.stats_window = False
        self.inventory_window = False
        self.objects = 0
        self.used = 0
        self.phase = 0
        self.text_log1, self.color1 = ("", self.black)
        self.text_log2, self.color2 = ("", self.black)
        self.text_log3, self.color3 = ("", self.black)
        self.text_log4, self.color4 = ("", self.black)
        self.text_log5, self.color5 = ("", self.black)

    def text_objects(self, text, font, color):
        """ Renvoie un texte sur une surface et ses coordonnées """
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_display(self, screen, text, size, x, y, color):
        """ Affiche le message 'text' en 'x' et 'y' """
        twcenmtcd = pygame.font.Font("assets/font/twcenmtcd.ttf", size)
        text_surf, text_rect = self.text_objects(text, twcenmtcd, color)
        text_rect.x, text_rect.y = (x,y)
        screen.blit(text_surf, text_rect)

    def message_display_right(self, screen, text, size, x, y, color):
        """ Affiche le message 'text' avec pour droite 'x' et 'y' """
        twcenmtcd = pygame.font.Font("assets/font/twcenmtcd.ttf", size)
        text_surf, text_rect = self.text_objects(text, twcenmtcd, color)
        text_rect.topright = (x, y)
        screen.blit(text_surf, text_rect)

    def message_display_center(self, screen, text, size, x, y, color, y_offset = 0):
        """ Affiche le message 'text' avec pour centre 'x' et 'y' """
        twcenmtcd = pygame.font.Font("assets/font/twcenmtcd.ttf", size)
        text_surf, text_rect = self.text_objects(text, twcenmtcd, color)
        text_rect.center = (x,y + y_offset)
        screen.blit(text_surf, text_rect)

    def load_image(self, image_path, dim_x, dim_y):
        """ Affiche une image provenant de 'image_path' aux dimensions 'dim_x', 'dim_y' """
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (dim_x, dim_y))
        return image

    def load_image_position(self, screen, image_path, dim_x, dim_y, x, y):
        """ Affiche une image provenant de 'image_path' aux dimensions 'dim_x', 'dim_y' en 'x','y' """
        image = self.load_image(image_path, dim_x, dim_y)
        screen.blit(image, (x, y))

    def load_image_rect(self, image_path, dim_x, dim_y, x, y):
        """ Permet d'avoir le rectangle de l'image provenant de 'image_path' aux dimensions 'dim_x', 'dim_y' en 'x','y' """
        image = self.load_image(image_path, dim_x, dim_y)
        image = pygame.transform.scale(image, (dim_x, dim_y))
        image_rect = image.get_rect()
        image_rect.x = x
        image_rect.y = y
        return image_rect

    def chat_logs(self, screen, text_log_new, offset=0, color=(0, 0, 0)):
        """ Affiche les logs sur l'écran et à chaque nouveau texte les fait monter """
        self.text_log5, self.color5 = (self.text_log4, self.color4)
        self.text_log4, self.color4 = (self.text_log3, self.color3)
        self.text_log3, self.color3 = (self.text_log2, self.color2)
        self.text_log2, self.color2 = (self.text_log1, self.color1)
        self.text_log1, self.color1 = (text_log_new, color)
        self.load_image_position(screen, "assets/lower_screen/drawbar_2.png", 736, 158, 313+offset, 551)
        self.message_display(screen, self.text_log1, 24, 321+offset, 648, self.color1)
        self.message_display(screen, self.text_log2, 24, 321+offset, 626, self.color2)
        self.message_display(screen, self.text_log3, 24, 321+offset, 604, self.color3)
        self.message_display(screen, self.text_log4, 24, 321+offset, 582, self.color4)
        self.message_display(screen, self.text_log5, 24, 321+offset, 560, self.color5)

    def lower_screen(self, screen):
        """ Affiche le bas de l'écran """
        # Affiche le profile et le background du bas
        self.load_image_position(screen, "assets/lower_screen/drawbar_1.png", 1280, 180, 0, 540)
        self.load_image_position(screen, "assets/lower_screen/drawbar_2.png", 736, 158, 313, 551)
        pygame.draw.rect(screen, (255, 255, 255), [1055, 553, 213, 156])
        self.load_image_position(screen, "assets/lower_screen/bag.png", 45, 45, 8, 552)
        self.load_image_position(screen, "assets/lower_screen/stats.png", 45, 45, 8, 603)
        self.load_image_position(screen, f"assets/player/{self.game.player.gender}/{self.game.player.gender}_head.png", 100, 100, 60, 548)
        self.message_display_center(screen, "PV", 20, 34, 682, (255, 255, 255))
        self.message_display_center(screen, "Énergie", 20, 32, 702, (255, 255, 255))
        self.message_display(screen, self.game.player.name, 24, 169, 570, (255, 255, 255))
        self.message_display(screen, f"Niveau {self.game.player.level} - H{self.game.player.rank}", 24, 170, 610, (255, 255, 255))
        self.message_display(screen, self.game.player.role, 24, 170, 630, (255, 255, 255))

        # Affiche les barres de status
        self.game.player.update_stats_bar(screen)
        self.status_update(screen)

        # Affiche la minimap
        self.minimap(screen)

    def status_update(self, screen, mode="normal"):
        """ Affiche la vie et la concentration du joueur en nombre """
        self.message_display_center(screen, f"{self.game.player.health} / {self.game.player.max_health}", 16, 175, 682, self.black)
        self.message_display_center(screen, f"{self.game.player.energy} / {self.game.player.max_energy}", 16, 175, 702, self.black)
        if mode == "fight":
            self.message_display_center(screen, f"{self.game.player.health} / {self.game.player.max_health}", 16, 175, 682, self.black)
            self.message_display_center(screen, f"{self.game.player.energy} / {self.game.player.max_energy}", 16, 175, 702, self.black)

    def minimap(self, screen):
        """ Met à jour la minimap """
        self.load_image_position(screen, f"assets/map/{self.game.map_y}-{self.game.map_x}.jpg", 200, 145, 1061, 559)
        self.game.minimap_update = False

    def show_stats(self, screen):
        """ Affiche la fenêtre des stats """
        self.load_image_position(screen, "assets/menu/home/background_menu.png", 256, 332, 275, 130)
        self.load_image_position(screen, "assets/menu/home/background_menu.png", 427, 382, 600, 100)
        self.load_image_position(screen, f"assets/player/{self.game.player.gender}/{self.game.player.gender}_front.png", 213, 270, 295, 165)
        self.message_display(screen, f"{self.game.player.name} - {self.game.player.role}", 30, 640, 143, (255, 255, 255))
        self.message_display(screen, f"Level : {self.game.player.level}", 30, 640, 183, (255, 255, 255))
        self.message_display(screen, f"Rang : H{self.game.player.rank}", 30, 830, 183, (255, 255, 255))
        self.game.player.update_stats_bar(screen, "status")
        self.message_display(screen, f"Expérience : {self.game.player.xp} / {self.game.player.max_xp}", 24, 640, 233, (255, 255, 255))
        self.message_display(screen, f"PV: {self.game.player.health} / {self.game.player.max_health}", 30, 640, 273, (255, 255, 255))
        self.message_display(screen, f"Énergie: {self.game.player.energy} / {self.game.player.max_energy}", 30, 830, 267, (255, 255, 255))
        self.message_display(screen, f"Attaque: {self.game.player.attack}", 30, 640, 303, (255, 255, 255))
        self.message_display(screen, f"Défense: {self.game.player.defence}", 30, 830, 303, (255, 255, 255))
        self.load_image_position(screen, "assets/fight/button.png", 100, 30, 760, 435)
        self.message_display_center(screen, "Retour", 30, 810, 450, self.black)

        if self.game.player.rank == 2:
            self.message_display(screen, "Attaque spéciale :", 30, 640, 343, (255, 255, 255))
            self.message_display(screen, list(self.game.skills.skills)[0], 24, 640, 373, (255, 255, 255))

        elif self.game.player.rank > 2:
            self.message_display(screen, "Attaques spéciales :", 30, 640, 343, (255, 255, 255))
            self.message_display(screen, list(self.game.skills.skills)[0], 24, 640, 373, (255, 255, 255))
            self.message_display(screen, list(self.game.skills.skills)[1], 24, 830, 373, (255, 255, 255))

            if self.game.player.rank >= 4:
                self.message_display(screen, list(self.game.skills.skills)[2], 24, 640, 403, (255, 255, 255))

            if self.game.player.rank == 5:
                self.message_display(screen, list(self.game.skills.skills)[3], 24, 830, 403, (255, 255, 255))

    def show_inventory(self, screen):
        """ Affiche la fenêtre de l'inventaire """
        if self.objects == 0:
            self.load_image_position(screen, "assets/shop/interface.jpg", 1000, 300, 140, 120)
            self.load_image_position(screen, "assets/fight/open_bag.png", 180, 164, 200, 158)
            self.load_image_position(screen, "assets/fight/button.png", 150, 30, 230, 352)
            self.message_display_center(screen, f"Solde : {self.game.inventory.money}€", 24, 305, 367, self.black)
            self.load_image_position(screen, "assets/fight/button.png", 150, 30, 901, 352)
            self.message_display_center(screen, "Fermer", 24, 976, 367, self.black)
            self.four_choice(screen, "Nouritture", "Boisson", "Boost d'attaque", "Boost de défense")
            self.show_icon(screen, "food", "drinks", "attack_boost", "defence_boost", "fight")

        elif self.objects == 1:
            self.four_choice(screen, "Burger", "Panini", "Pizza", "Tacos", -10)
            self.desc_item(screen, "Burger", "Panini", "Pizza", "Tacos")
            self.show_icon(screen, "Burger", "Panini", "Pizza", "Tacos", "inventory")
            self.load_image_position(screen, "assets/fight/button.png", 150, 30, 901, 352)
            self.message_display_center(screen, "Précédent", 24, 976, 367, self.black)

        elif self.objects == 2:
            self.four_choice(screen, "Eau", "Thé", "Coca", "Café", -10)
            self.desc_item(screen, "Eau", "Thé", "Coca", "Café")
            self.show_icon(screen, "Eau", "Thé", "Coca", "Café", "inventory")
            self.load_image_position(screen, "assets/fight/button.png", 150, 30, 901, 352)
            self.message_display_center(screen, "Précédent", 24, 976, 367, self.black)

        elif self.objects == 3:
            self.four_choice(screen, "Tic Tac", "Miel", "Vin", "Vodka", -10, "button_off")
            self.desc_item(screen, "Tic Tac", "Miel", "Vin", "Vodka", 3)
            self.show_icon(screen, "Tic Tac", "Miel", "Vin", "Vodka", "inventory")
            self.load_image_position(screen, "assets/fight/button.png", 150, 30, 901, 352)
            self.message_display_center(screen, "Précédent", 24, 976, 367, self.black)

        elif self.objects == 4:
            self.four_choice(screen, "Pommade", "Vitamine C", "Doliprane", "Gingembre", -10, "button_off")
            self.desc_item(screen, "Pommade", "Vitamine C", "Doliprane", "Gingembre", 4)
            self.show_icon(screen, "Pommade", "Vitamine C", "Doliprane", "Gingembre", "inventory")
            self.load_image_position(screen, "assets/fight/button.png", 150, 30, 901, 352)
            self.message_display_center(screen, "Précédent", 24, 976, 367, self.black)

        # Utilise l'objet si il y en a au moins 1
        if self.used != 0:
            if self.objects == 3:
                self.chat_logs(screen, "Vous ne pouvez pas utiliser de boost d'attaque en dehors des combats.", 0, self.red)

            elif self.objects == 4:
                self.chat_logs(screen, "Vous ne pouvez pas utiliser de boost de défense en dehors des combats.", 0, self.red)

            else:
                item_name = list(self.game.inventory.inventory)[self.objects * 4 + self.used - 5]
                item_number = self.game.inventory.inventory[item_name]["number"]
                if item_number != 0:
                    if item_number <= 2 and item_number > 0:
                        self.game.display.chat_logs(screen, f"{self.game.player.name} utilise l'objet {item_name}, vous n'en avez plus que {item_number - 1} exemplaire.")

                    elif item_number > 2:
                        self.game.display.chat_logs(screen, f"{self.game.player.name} utilise l'objet {item_name}, vous n'en avez plus que {item_number - 1} exemplaires.")

                    if self.objects == 1:
                        effect = self.game.inventory.inventory[item_name]["PV"]

                        if self.game.player.health == self.game.player.max_health:
                            self.game.display.chat_logs(screen, f"Les points de vie de {self.game.player.name} sont déja au maximum, l'objet {item_name} ne fait rien.")

                        elif self.game.player.health + effect <= self.game.player.max_health:
                            self.game.display.chat_logs(screen, f"{self.game.player.name} récupère {effect} points de vie.", -41)

                        elif self.game.player.health + effect > self.game.player.max_health:
                            self.game.display.chat_logs(screen, f"{self.game.player.name} récupère {self.game.player.max_health - self.game.player.health} points de vie.")

                    elif self.objects == 2:

                        effect = self.game.inventory.inventory[item_name]["E"]

                        if self.game.player.energy == self.game.player.max_energy:
                            self.game.display.chat_logs(screen, f"Les points de vie de {self.game.player.name} sont déja au maximum.")

                        elif self.game.player.energy + effect <= self.game.player.max_energy:
                            self.game.display.chat_logs(screen, f"{self.game.player.name} récupère {effect} points d'énergie.")

                        elif self.game.player.energy + effect > self.game.player.max_energy:
                            self.game.display.chat_logs(screen, f"{self.game.player.name} récupère {self.game.player.max_energy - self.game.player.energy} points d'énergie.")
                    self.game.inventory.use_item(item_name)
                    self.game.save.save_game()
                    self.lower_screen(screen)
                    self.chat_logs(screen, "")

                else:
                    self.game.display.chat_logs(screen, f"Vous avez 0 exemplaire de l'objet {item_name} dans votre inventaire.")
            self.used = 0

    def four_choice(self, screen, first_choice, second_choice, third_choice, fourth_choice, y_offset = 0, button = "button"):
        """ Affiche quatres boutons avec leur texte centré """
        self.game.display.load_image_position(screen, f"assets/fight/{button}.png", 300, 60, 427, 168)
        self.game.display.message_display_center(screen, first_choice, 24, 577, 198 + y_offset, self.black)
        self.game.display.load_image_position(screen, f"assets/fight/{button}.png", 300, 60, 751, 168)
        self.game.display.message_display_center(screen, second_choice, 24, 901, 198 + y_offset, self.black)
        self.game.display.load_image_position(screen, f"assets/fight/{button}.png", 300, 60, 427, 252)
        self.game.display.message_display_center(screen, third_choice, 24, 577, 282 + y_offset, self.black)
        self.game.display.load_image_position(screen, f"assets/fight/{button}.png", 300, 60, 751, 252)
        self.game.display.message_display_center(screen, fourth_choice, 24, 901, 282 + y_offset, self.black)

    def desc_item(self, screen, item_name1, item_name2, item_name3, item_name4, negative = 0):
        """ Affiche le nombre d'exemplaire des objets, leur effets """
        # Affiche le nombre d'exemplaire des objets
        if self.game.inventory.inventory[item_name1]["number"] != 0:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name1]["number"]), 24, 577, 208, self.black)
        else:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name1]["number"]), 24, 577, 208, self.red)
        if self.game.inventory.inventory[item_name2]["number"] != 0:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name2]["number"]), 24, 901, 208, self.black)
        else:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name2]["number"]), 24, 901, 208, self.red)
        if self.game.inventory.inventory[item_name3]["number"] != 0:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name3]["number"]), 24, 577, 292, self.black)
        else:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name3]["number"]), 24, 577, 292, self.red)
        if self.game.inventory.inventory[item_name4]["number"] != 0:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name4]["number"]), 24, 901, 292, self.black)
        else:
            self.game.display.message_display_center(screen, str(self.game.inventory.inventory[item_name4]["number"]), 24, 901, 292, self.red)

        # Affiche les effets des différents objets
        effect = list(list(self.game.inventory.inventory.values())[(self.objects - 1) * 4])[1]
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name1][effect]} {effect}", 24, 650, 178, self.green)
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name2][effect]} {effect}", 24, 970, 178, self.green)
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name3][effect]} {effect}", 24, 650, 262, self.green)
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name4][effect]} {effect}", 24, 970, 262, self.green)
        if negative == 3:
            side_effect = list(list(self.game.inventory.inventory.values())[(self.objects - 1) * 4])[2]
            self.game.display.message_display(screen, f"   {self.game.inventory.inventory[item_name3][side_effect]} {side_effect}", 24, 650, 282, self.red)
            self.game.display.message_display(screen, f"   {self.game.inventory.inventory[item_name4][side_effect]} {side_effect}", 24, 970, 282, self.red)
        elif negative == 4:
            side_effect = list(list(self.game.inventory.inventory.values())[(self.objects - 1) * 4])[2]
            self.game.display.message_display(screen, f"   {self.game.inventory.inventory[item_name4][side_effect]} {side_effect}", 24, 970, 282, self.red)

    def show_icon(self, screen, icon_name1, icon_name2, icon_name3, icon_name4, category):
        """ Affiche l'image des objets """
        self.game.display.load_image_position(screen, f"assets/{category}/{icon_name1}.png", 50, 50, 435, 173)
        self.game.display.load_image_position(screen, f"assets/{category}/{icon_name2}.png", 50, 50, 759, 173)
        self.game.display.load_image_position(screen, f"assets/{category}/{icon_name3}.png", 50, 50, 435, 257)
        self.game.display.load_image_position(screen, f"assets/{category}/{icon_name4}.png", 50, 50, 759, 257)

    def tutorial(self, screen):
        """ Affiche le tutoriel écrit """
        if self.phase == 0:
            self.load_image_position(screen, "assets/map/5_2.jpg", 1280, 540, 0, 0)
            self.lower_screen(screen)
            self.load_image_position(screen, "assets/tutorial/input_tutorial.jpg", 1121, 426, 80, 57)
            self.phase = -1

        elif self.phase == 1:
            self.load_image_position(screen, "assets/tutorial/interaction_tutorial.jpg", 1121, 426, 80, 57)
            self.phase = -2

        elif self.phase == 2:
            self.chat_logs(screen, f"Bienvenue à Hetic cher étudiant {self.game.player.name}.")
            self.chat_logs(screen, f"Tu es désormais un {self.game.player.role} en H1, ton but étant de devenir plus fort.")
            self.chat_logs(screen, "Pourquoi me-dis tu ? Afin de survivre dans ce lieu où terreur et compétition reigne")
            if self.game.player.mode == "Normal":
                self.chat_logs(screen, "Tout ca depuis que M. Martinez a prit le pouvoir.")
            elif self.game.player.mode == "Hardcore":
                self.chat_logs(screen, "Tout ca depuis que M. Bourienne a prit le pouvoir.")
            self.chat_logs(screen, "Peut-être arriveras-tu à le détronner et à créer un nouvel ère.")
            self.game.is_playing = True
