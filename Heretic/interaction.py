"Fichier pour les intéractions avec les pnj"

class Interaction():
    """ Définit les informations de l'intéractions """
    def __init__(self, game):
        self.game = game
        self.interaction = False
        self.npc_name = None
        self.show = -1
        self.action = 0

        # Définit les couleurs
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (111, 210, 100)
        self.blue = (0, 0, 255)

    def npc_interaction(self, screen):
        """ Permet d'intéragir avec un pnj """
        # Le pnj est le vendeur
        if self.npc_name == "Vendeur":
            # Bienvenue
            if self.show == -1:
                self.game.display.chat_logs(screen, "Vendeur : Salut l'ami, bienvenue au Gaby cook !")
                self.game.display.chat_logs(screen, "Vendeur : Que veux-tu acheter ?")
                self.show = 0

            # Affichage de la boutique
            if self.show == 0:
                self.game.display.load_image_position(screen, "assets/shop/interface.jpg", 1121, 426, 80, 64)
                self.game.display.load_image_position(screen, "assets/npc/shop_keeper.png", 135, 182, 115, 185)
                self.game.display.load_image_position(screen, f"assets/player/{self.game.player.gender}/{self.game.player.gender}_front.png", 135, 180, 1030, 187)
                self.game.display.message_display_center(screen, "Gaby cook", 64, 640, 120, self.white)
                self.game.display.message_display(screen, "Vendeur", 30, 145, 153, self.white)
                self.game.display.message_display_center(screen, self.game.player.name, 30, 1097.5, 162.7, self.white)
                self.game.display.load_image_position(screen, "assets/fight/button.png", 150, 30, 1023, 374)
                self.game.display.message_display_center(screen, f"Solde : {self.game.inventory.money}€", 24, 1098, 389, self.black)
                self.game.display.load_image_position(screen, "assets/shop/coins.png", 57, 47, 500, 248)
                self.game.display.load_image_position(screen, "assets/shop/red_arrow.png", 100, 30, 572, 256)
                self.game.display.load_image_position(screen, "assets/shop/green_arrow.png", 100, 30, 590, 194)
                self.game.display.load_image_position(screen, "assets/fight/open_bag.png", 91, 82, 701, 168)
                self.four_choice(screen, "Nourriture", "Boisson", "Boost d'attaque", "Boost de défense")
                self.show_icon(screen, "food", "drinks", "attack_boost", "defence_boost", "fight")
                self.game.display.load_image_position(screen, "assets/fight/button.png", 150, 30, 1023, 410)
                self.game.display.message_display_center(screen, "Partir", 24, 1098, 425, self.black)
                self.show = -2

            # Affichage de la nourriture
            if self.show == 1:
                self.four_choice(screen, "Burger", "Panini", "Pizza", "Tacos", -10)
                self.show_icon(screen, "Burger", "Panini", "Pizza", "Tacos", "inventory")
                self.desc_item(screen, "Burger", "Panini", "Pizza", "Tacos")
                self.previous_button(screen)

            # Affichage des boissons
            elif self.show == 2:
                self.four_choice(screen, "Eau", "Thé", "Coca", "Café", -10)
                self.show_icon(screen, "Eau", "Thé", "Coca", "Café", "inventory")
                self.desc_item(screen, "Eau", "Thé", "Coca", "Café")
                self.previous_button(screen)

            # Affichage des boosts d'attaque
            elif self.show == 3:
                self.four_choice(screen, "Tic Tac", "Miel", "Vin", "Vodka", -10)
                self.show_icon(screen, "Tic Tac", "Miel", "Vin", "Vodka", "inventory")
                self.desc_item(screen, "Tic Tac", "Miel", "Vin", "Vodka", 3)
                self.previous_button(screen)

            # Affichage des boosts de défense
            elif self.show == 4:
                self.four_choice(screen, "Pommade", "Vitamine C", "Doliprane", "Gingembre", -10)
                self.show_icon(screen, "Pommade", "Vitamine C", "Doliprane", "Gingembre", "inventory")
                self.desc_item(screen, "Pommade", "Vitamine C", "Doliprane", "Gingembre", 4)
                self.previous_button(screen)

            # Achète un objet
            if self.action != 0:
                item_bought = list(self.game.inventory.inventory)[self.show * 4 + self.action - 5]
                item_number = self.game.inventory.inventory[item_bought]["number"]
                price = self.game.inventory.inventory[item_bought]["price"]

                if self.action > self.game.player.rank - 1:
                    self.game.display.chat_logs(screen, f"Vendeur : Tu ne peux pas acheter cet objet, il te faut être au rang H{self.action + 1}.", 0, self.red)
                    self.game.display.chat_logs(screen, "Vendeur : Reviens me voir lorsque tu seras plus expérimenté pour utiliser l'objet.")

                elif self.game.inventory.money < price:
                    difference = price - self.game.inventory.money
                    self.game.display.chat_logs(screen, f"Vendeur : Tu n'as pas assez d'argent pour acheter l'objet {item_bought} !", 0, self.red)
                    self.game.display.chat_logs(screen, f"Vendeur : Il te manque {difference}€, rien de plus, rien de moins.", 0, self.red)

                elif item_number == 5:
                    self.game.display.chat_logs(screen, f"Vendeur : Tu ne peux pas porter plus de 5 exemplaires de l'objet {item_bought}.", 0, self.red)

                else:
                    self.game.inventory.money -= price
                    self.game.display.load_image_position(screen, "assets/fight/button.png", 150, 30, 1023, 374)
                    self.game.display.message_display_center(screen, f"Solde : {self.game.inventory.money}€", 24, 1098, 389, self.black)
                    self.game.inventory.inventory[item_bought]["number"] += 1
                    self.game.display.chat_logs(screen, f"Vous avez payé {price}€ au vendeur.", 0, self.red)
                    self.game.display.chat_logs(screen, f"Vous avez obtenu 1 {item_bought}, vous en avez maintenant {item_number + 1} exemplaires.", 0, self.green)
                    self.game.display.chat_logs(screen, "Vendeur : Que veux-tu acheter d'autre ?")

                self.action = 0

        # Le pnj est M. Janin
        elif self.npc_name == "M. Janin":

            # Si le joueur est de la bonne classe
            if self.game.player.role == "Développeur" and self.show == -1:

                # Affiche la discussion et la nouvelle attaque spéciale
                if self.game.player.rank_change > 0 and self.game.player.rank != 5:
                    self.game.player.rank += 1
                    self.game.display.lower_screen(screen)
                    self.game.skills.skills_update()
                    skill_name = list(self.game.skills.skills_Développeur)[self.game.player.rank - 2]
                    self.game.display.chat_logs(screen, f"M. Janin : Bonjour {self.game.player.name}, tu as bien fait de venir me voir.")
                    self.game.display.chat_logs(screen, f"M. Janin : Tu as passé avec brio avec ton année de développeur H{self.game.player.rank - 1} !")
                    self.new_skill(screen, skill_name)
                    self.game.display.chat_logs(screen, f"M. Janin : Bienvenue en H{self.game.player.rank}, je vais t'apprendre l'attaque spéciale spécifique à ce rang.")
                    self.game.display.chat_logs(screen, f"{self.game.player.name} est passé au rang H{self.game.player.rank}.", 0, self.blue)
                    self.game.display.chat_logs(screen, f"{self.game.player.name} a appris l'attaque spéciale {skill_name}.", 0, self.blue)
                    self.game.player.rank_change -= 1
                    self.show = 0

                # Affiche la fin de discussion à cause d'un niveau pas assez élevé
                elif self.game.player.rank != 5:
                    self.game.display.chat_logs(screen, f"M. Janin : Bonjour {self.game.player.name}, tu n'es pas assez haut niveau.", 0, self.red)
                    self.game.display.chat_logs(screen, f"M. Janin : Reviens me voir quand tu seras au niveau {self.game.player.rank * 2} pour passer au rang H{self.game.player.rank + 1}.")
                    self.game.is_playing = True
                    self.interaction = False

                # Affiche la fin de discussion si le joueur est déja au rang max
                else:
                    if self.game.player.gender == "boy":
                        self.game.display.chat_logs(screen, f"M. Janin : Bonjour {self.game.player.name}, tu es déja un étudiant en H5.")
                        self.game.display.chat_logs(screen, "M. Janin : Etant désormais un développeur aguéri, je n'ai plus rien à t'apprendre.")
                    else:
                        self.game.display.chat_logs(screen, f"M. Janin : Bonjour {self.game.player.name}, tu es déja une étudiante en H5.")
                        self.game.display.chat_logs(screen, "M. Janin : Etant désormais une développeur aguérie, je n'ai plus rien à t'apprendre.")
                    self.game.display.chat_logs(screen, "M. Janin : Il ne te reste plus qu'à affronter le monde professionnel, bonne chance !")
                    self.game.is_playing = True
                    self.interaction = False

            # Affiche la fin de discussion si le joueur n'est pas de la bonne classe
            elif self.game.player.role != "Développeur":
                if self.game.player.gender == "boy":
                    self.game.display.chat_logs(screen, f"M. Janin : Bonjour {self.game.player.name}, tu n'es pas un développeur.", 0, self.red)
                else:
                    self.game.display.chat_logs(screen, f"M. Janin : Bonjour {self.game.player.name}, tu n'es pas une développeur.", 0, self.red)
                self.game.display.chat_logs(screen, "M. Janin : N'étant pas ton formateur, je ne peux rien faire pour t'aider dans ta voie.")
                self.game.display.chat_logs(screen, "M. Janin : Demande à Mme. Marty ou M. Charassin, ils pourront peut-être t'aider.")
                self.game.is_playing = True
                self.interaction = False

            self.game.player.rect.x, self.game.player.rect.y = (390, 250)

        # Le pnj est Mme. Marty
        elif self.npc_name == "Mme. Marty":

            # Si le joueur est de la bonne classe
            if self.game.player.role == "Philosophe" and self.show == -1:

                # Affiche la discussion et la nouvelle attaque spéciale
                if self.game.player.rank_change > 0 and self.game.player.rank != 5:
                    self.game.player.rank += 1
                    self.game.display.lower_screen(screen)
                    self.game.skills.skills_update()
                    skill_name = list(self.game.skills.skills_Philosophe)[self.game.player.rank - 2]
                    self.game.display.chat_logs(screen, f"Mme. Marty : Salutation {self.game.player.name}, tu as bien fait de venir me voir.")
                    self.game.display.chat_logs(screen, f"Mme. Marty : Tu as passé avec brio ton année de philosophe H{self.game.player.rank - 1} !")
                    self.new_skill(screen, skill_name)
                    self.game.display.chat_logs(screen, f"Mme. Marty : Bienvenue en H{self.game.player.rank}, je vais t'apprendre l'attaque spéciale spécifique à ce rang.")
                    self.game.display.chat_logs(screen, f"{self.game.player.name} est passé au rang H{self.game.player.rank}.", 0, self.blue)
                    self.game.display.chat_logs(screen, f"{self.game.player.name} a appris l'attaque spéciale {skill_name}.", 0, self.blue)
                    self.game.player.rank_change -= 1
                    self.show = 0

                # Affiche la fin de discussion à cause d'un niveau pas assez élevé
                elif self.game.player.rank != 5:
                    self.game.display.chat_logs(screen, f"Mme. Marty : Salutation {self.game.player.name}, tu n'es pas assez haut niveau.", 0, self.red)
                    self.game.display.chat_logs(screen, f"Mme. Marty : Reviens me voir quand tu seras au niveau {self.game.player.rank * 2} pour passer au rang H{self.game.player.rank + 1}.")
                    self.game.is_playing = True
                    self.interaction = False

                # Affiche la fin de discussion si le joueur est déja au rang max
                else:
                    if self.game.player.gender == "boy":
                        self.game.display.chat_logs(screen, f"Mme. Marty : Salutation {self.game.player.name}, tu es déja un étudiant en H5.")
                        self.game.display.chat_logs(screen, "Mme. Marty : Etant désormais un philosophe aguéri, je n'ai plus rien à t'apprendre.")
                    else:
                        self.game.display.chat_logs(screen, f"Mme. Marty : Salutation {self.game.player.name}, tu es déja une étudiante en H5.")
                        self.game.display.chat_logs(screen, "Mme. Marty : Etant désormais une philosophe aguéri, je n'ai plus rien à t'apprendre.")
                    self.game.display.chat_logs(screen, "Mme. Marty : Il ne te reste plus qu'à affronter le monde professionnel, bonne chance !")
                    self.game.is_playing = True
                    self.interaction = False

            # Affiche la fin de discussion si le joueur n'est pas de la bonne classe
            elif self.game.player.role != "Philosophe":
                if self.game.player.gender == "boy":
                    self.game.display.chat_logs(screen, f"Mme. Marty : Salutation {self.game.player.name}, tu n'es pas un philosophe.", 0, self.red)
                else:
                    self.game.display.chat_logs(screen, f"Mme. Marty : Salutation {self.game.player.name}, tu n'es pas une philosophe.", 0, self.red)
                self.game.display.chat_logs(screen, "Mme. Marty : N'étant pas ta formatrice, je ne peux pas t'aider dans ta voie.")
                self.game.display.chat_logs(screen, "Mme. Marty : Demande à M. Janin ou M. Charrassin, ils pourront peut-être t'aider.")
                self.game.is_playing = True
                self.interaction = False

            self.game.player.rect.x, self.game.player.rect.y = (510, 240)

        # Le pnj est M. Charrassin
        elif self.npc_name == "M. Charrassin":

            # Si le joueur est de la bonne classe
            if self.game.player.role == "Designer" and self.show == -1:

                # Affiche la discussion et la nouvelle attaque spéciale
                if self.game.player.rank_change > 0 and self.game.player.rank != 5:
                    self.game.player.rank += 1
                    self.game.display.lower_screen(screen)
                    self.game.skills.skills_update()
                    skill_name = list(self.game.skills.skills_Designer)[self.game.player.rank - 2]
                    self.game.display.chat_logs(screen, f"M. Charrassin : Salut {self.game.player.name}, tu as bien fait de venir me voir.")
                    self.game.display.chat_logs(screen, f"M. Charrassin : Regarde j'ai les résultats de ton année de designer H{self.game.player.rank - 1} et tu as réussi à passer !")
                    self.new_skill(screen, skill_name)
                    self.game.display.chat_logs(screen, f"M. Charrassin : Bienvenue en H{self.game.player.rank}, je vais t'apprendre l'attaque spéciale spécifique à ce rang.")
                    self.game.display.chat_logs(screen, f"{self.game.player.name} est passé au rang H{self.game.player.rank}.", 0, self.blue)
                    self.game.display.chat_logs(screen, f"{self.game.player.name} a appris l'attaque spéciale {skill_name}.", 0, self.blue)
                    self.game.player.rank_change -= 1
                    self.show = 0

                # Affiche la fin de discussion à cause d'un niveau pas assez élevé
                elif self.game.player.rank != 5:
                    self.game.display.chat_logs(screen, f"M. Charrassin : Salut {self.game.player.name}, tu n'es pas assez haut niveau.", 0, self.red)
                    self.game.display.chat_logs(screen, f"M. Charrassin : Reviens me voir quand tu seras au niveau {self.game.player.rank * 2} pour passer au rang H{self.game.player.rank + 1}.")
                    self.game.is_playing = True
                    self.interaction = False

                # Affiche la fin de discussion si le joueur est déja au rang max
                else:
                    if self.game.player.gender == "boy":
                        self.game.display.chat_logs(screen, f"M. Charrassin : Salut {self.game.player.name}, tu es déja un étudiant en H5.")
                        self.game.display.chat_logs(screen, "M. Charrassin : Etant désormais un designer aguéri, je n'ai plus rien à t'apprendre.")
                    else:
                        self.game.display.chat_logs(screen, f"M. Charrassin : Salut {self.game.player.name}, tu es déja une étudiante en H5.")
                        self.game.display.chat_logs(screen, "M. Charassin : Etant désormais une designer aguérie, je n'ai plus rien à t'apprendre.")
                    self.game.display.chat_logs(screen, "M. Charrassin : Il ne te reste plus qu'à affronter le monde professionnel, bonne chance !")
                    self.game.is_playing = True
                    self.interaction = False

            # Affiche la fin de discussion si le joueur n'est pas de la bonne classe
            elif self.game.player.role != "Designer":
                if self.game.player.gender == "boy":
                    self.game.display.chat_logs(screen, f"M. Charrassin : Salut {self.game.player.name}, tu n'es pas un designer.", 0, self.red)
                else:
                    self.game.display.chat_logs(screen, f"M. Charrassin : Salut {self.game.player.name}, tu n'es pas une designer.", 0, self.red)
                self.game.display.chat_logs(screen, "M. Charrassin : N'étant pas ton formateur, je ne peux pas t'aider dans ta voie.")
                self.game.display.chat_logs(screen, "M. Charrassin : Demande à M. Janin ou Mme. Marty, ils pourront peut-être t'aider.")
                self.game.is_playing = True
                self.interaction = False

            self.game.player.rect.x, self.game.player.rect.y = (760, 190)

    def four_choice(self, screen, first_choice, second_choice, third_choice, fourth_choice, y_offset = 0):
        """ Affiche quatres boutons avec leur texte centré """
        self.game.display.load_image_position(screen, "assets/fight/button.png", 356, 52, 275, 321)
        self.game.display.message_display_center(screen, first_choice, 24, 453, 347 + y_offset, self.black)
        self.game.display.load_image_position(screen, "assets/fight/button.png", 356, 52, 647, 321)
        self.game.display.message_display_center(screen, second_choice, 24, 825, 347 + y_offset, self.black)
        self.game.display.load_image_position(screen, "assets/fight/button.png", 356, 52, 275, 389)
        self.game.display.message_display_center(screen, third_choice, 24, 453, 415 + y_offset, self.black)
        self.game.display.load_image_position(screen, "assets/fight/button.png", 356, 52, 647, 389)
        self.game.display.message_display_center(screen, fourth_choice, 24, 825, 415 + y_offset, self.black)

    def previous_button(self, screen):
        """ Affiche un bouton pour revenir en arrière """
        self.game.display.load_image_position(screen, "assets/fight/button.png", 150, 30, 1023, 410)
        self.game.display.message_display_center(screen, "Précédent", 24, 1098, 425, self.black)

    def desc_item(self, screen, item_name1, item_name2, item_name3, item_name4, negative = 0):
        """ Affiche le prix des objets, leur nombre d'exemplaire possédé et leurs effets """
        # Affiche le prix des objets et le nombre d'exemplaire possédé des différents objets
        price = "price"
        number = "number"
        if self.game.inventory.inventory[item_name1][number] <= 1:
            possédé = "possédé"
        else:
            possédé = "possédés"
        if self.game.inventory.inventory[item_name1][price] <= self.game.inventory.money:
            self.game.display.message_display_center(screen,
            f"{self.game.inventory.inventory[item_name1][price]}€ - {self.game.inventory.inventory[item_name1][number]} {possédé}", 24, 453, 357, self.black)

        else:
            self.game.display.message_display_center(screen,
            f"{self.game.inventory.inventory[item_name1][price]}€ - {self.game.inventory.inventory[item_name1][number]} {possédé}", 24, 453, 357, self.red)

        if self.game.inventory.inventory[item_name2][number] <= 1:
            possédé = "possédé"
        else:
            possédé = "possédés"
        if self.game.inventory.inventory[item_name2][price] <= self.game.inventory.money:
            self.game.display.message_display_center(screen,
            f"{self.game.inventory.inventory[item_name2][price]}€ - {self.game.inventory.inventory[item_name2][number]} {possédé}", 24, 825, 357, self.black)

        else:
            self.game.display.message_display_center(screen,
            f"{self.game.inventory.inventory[item_name2][price]}€ - {self.game.inventory.inventory[item_name2][number]} {possédé}", 24, 825, 357, self.red)

        if self.game.inventory.inventory[item_name3][number] <= 1:
            possédé = "possédé"
        else:
            possédé = "possédés"
        if self.game.inventory.inventory[item_name3][price] <= self.game.inventory.money:
            self.game.display.message_display_center(screen,
            f"{self.game.inventory.inventory[item_name3][price]}€ - {self.game.inventory.inventory[item_name3][number]} {possédé}", 24, 453, 425, self.black)

        else:
            self.game.display.message_display_center(screen,
            f"{self.game.inventory.inventory[item_name3][price]}€ - {self.game.inventory.inventory[item_name3][number]} {possédé}", 24, 453, 425, self.red)


        if self.game.inventory.inventory[item_name4][number] <= 1:
            possédé = "possédé"
        else:
            possédé = "possédés"
        if self.game.inventory.inventory[item_name4][price] <= self.game.inventory.money:
            self.game.display.message_display_center(screen,
            f"{self.game.inventory.inventory[item_name4][price]}€ - {self.game.inventory.inventory[item_name4][number]} {possédé}", 24, 825, 425, self.black)

        else:
            self.game.display.message_display_center(screen,
            f"{self.game.inventory.inventory[item_name4][price]}€ - {self.game.inventory.inventory[item_name4][number]} {possédé}", 24, 825, 425, self.red)

        # Affiche les effets des différents objets
        effect = list(list(self.game.inventory.inventory.values())[(self.show-1) * 4])[1]
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name1][effect]} {effect}", 24, 545, 327, self.green)
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name2][effect]} {effect}", 24, 917, 327, self.green)
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name3][effect]} {effect}", 24, 545, 395, self.green)
        self.game.display.message_display(screen, f"+{self.game.inventory.inventory[item_name4][effect]} {effect}", 24, 917, 395, self.green)
        if negative == 3:
            side_effect = list(list(self.game.inventory.inventory.values())[(self.show - 1) * 4])[2]
            self.game.display.message_display(screen, f"   {self.game.inventory.inventory[item_name3][side_effect]} {side_effect}", 24, 545, 415, self.red)
            self.game.display.message_display(screen, f"   {self.game.inventory.inventory[item_name4][side_effect]} {side_effect}", 24, 917, 415, self.red)
        elif negative == 4:
            side_effect = list(list(self.game.inventory.inventory.values())[(self.show - 1) * 4])[2]
            self.game.display.message_display(screen, f"   {self.game.inventory.inventory[item_name4][side_effect]} {side_effect}", 24, 917, 415, self.red)

    def show_icon(self, screen, icon_name1, icon_name2, icon_name3, icon_name4, category):
        """ Affiche l'image des objets """
        self.game.display.load_image_position(screen, f"assets/{category}/{icon_name1}.png", 42, 42, 337, 325)
        self.game.display.load_image_position(screen, f"assets/{category}/{icon_name2}.png", 42, 42, 710, 325)
        self.game.display.load_image_position(screen, f"assets/{category}/{icon_name3}.png", 42, 42, 337, 395)
        self.game.display.load_image_position(screen, f"assets/{category}/{icon_name4}.png", 42, 42, 710, 395)

    def new_skill(self, screen, skill_name):
        """ Affiche la nouvelle attaque spéciale apprise """
        self.game.display.load_image_position(screen, "assets/shop/interface.jpg", 750, 280, 265, 130)
        self.game.display.load_image_position(screen, f"assets/skills/{skill_name}.png", 50, 50, 400, 175)
        self.game.display.message_display_center(screen, skill_name, 48, 640, 200, self.white)
        self.game.display.load_image_position(screen, "assets/fight/button.png", 150, 30, 565, 350)
        self.game.display.message_display_center(screen, "Suivant", 30, 640, 364, self.black)

        # Affiche l'attaque spéciale
        if self.game.player.role == "Développeur":
            self.game.display.message_display_center(screen, self.game.skills.skills_Développeur[skill_name]["desc"], 30, 640, 270, self.white)

            if skill_name != "Débuggage":
                cost = self.game.skills.skills_Développeur[skill_name]["cost"]
                damage = self.game.skills.skills_Développeur[skill_name]["damage"]
                self.game.display.message_display_right(screen, f"Coût : {cost}E", 30, 585, 300, self.white)

                if skill_name != "Balise bombe HTML":
                    self.game.display.message_display(screen, f"Dégats : x{damage}", 30, 695, 300, self.white)

                else:
                    self.game.display.message_display(screen, "Dégats : x1.5 à x2.5", 30, 695, 300, self.white)

            else:
                self.game.display.message_display_center(screen, "Dégats : Augmente avec l'énergie dépensée", 30, 640, 300, self.white)

        # Affiche l'attaque spéciale
        elif self.game.player.role == "Philosophe":
            self.game.display.message_display_center(screen, self.game.skills.skills_Philosophe[skill_name]["desc"], 30, 640, 270, self.white)

            if skill_name != "Folie de Freud":
                cost = self.game.skills.skills_Philosophe[skill_name]["cost"]
                damage = self.game.skills.skills_Philosophe[skill_name]["damage"]
                self.game.display.message_display_right(screen, f"Coût : {cost}E", 30, 585, 300, self.white)

                if skill_name != "Lance-lettres":
                    self.game.display.message_display(screen, f"Dégats : x{damage}", 30, 695, 300, self.white)

                else:
                    self.game.display.message_display(screen, "Dégats : x1 à x3", 30, 695, 300, self.white)

            else:
                self.game.display.message_display_center(screen, "Dégats : Augmente plus les points de vie du joueur sont bas", 30, 640, 300, self.white)
                cost = self.game.skills.skills_Philosophe[skill_name]["cost"]
                self.game.display.message_display_center(screen, f"Coût : {cost}E", 30, 640, 330, self.white)

        # Affiche l'attaque spéciale
        elif self.game.player.role == "Designer":
            self.game.display.message_display_center(screen, self.game.skills.skills_Designer[skill_name]["desc"], 30, 640, 270, self.white)

            if skill_name != "Make the logo bigger!":
                cost = self.game.skills.skills_Designer[skill_name]["cost"]
                self.game.display.message_display_right(screen, f"Coût : {cost}E", 30, 585, 300, self.white)

                if skill_name == "Wireframe d'épée":
                    self.game.display.message_display(screen, "Effet : +(5 x Rang)Atk", 30, 695, 300, self.white)

                elif skill_name == "Prototype de bouclier":
                    self.game.display.message_display(screen, "Effet : +(3 x Rang)Def", 30, 695, 300, self.white)

                elif skill_name == "Design enemie-centric":
                    damage = self.game.skills.skills_Designer[skill_name]["damage"]
                    self.game.display.message_display(screen, f"Dégats : x{damage}", 30, 695, 300, self.white)

            else:
                self.game.display.message_display_center(screen, "Coût : Tout sauf 1HP", 30, 640, 330, self.white)
                self.game.display.message_display_center(screen, "Dégats : Augmente plus les points de vie du joueur sont haut", 30, 640, 300, self.white)

    def reset(self):
        """ Remet à zéro les intéractions """
        self.interaction = False
        self.npc_name = None
        self.show = -1
        self.action = 0
