"Fichier principale pour le jeu Heretic"
import os.path
import pygame
from game import Game

# Initialisation
pygame.init()

# Charge le jeu
game = Game()

# Fenêtre d'affichage
pygame.display.set_caption("Heretic RPG")
screen = pygame.display.set_mode((1280, 720))
icon = pygame.image.load("assets/logo/logo.png")
pygame.display.set_icon(icon)

# Définit les couleurs••
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

def menu():
    """ Affiche le menu """
    game.display.load_image_position(screen, "assets/menu/home/fill.jpg", 1280, 720, 0, 0)
    game.display.load_image_position(screen, "assets/menu/home/heretic.png", 427, 540, 426, 100)
    game.display.load_image_position(screen, "assets/menu/home/new_button.png", 379, 57, 451, 215)
    game.display.load_image_position(screen, "assets/menu/home/about_us_button.png", 379, 57, 451, 480)
    game.display.load_image_position(screen, "assets/menu/home/exit_button.png", 379, 57, 451, 560)
    if os.path.isfile("save/player_save.heretic"):
        game.save.show_save()
        game.display.load_image_position(screen, "assets/menu/home/load_button.png", 379, 167, 451, 290)
    else:
        game.display.load_image_position(screen, "assets/menu/home/load_button_deactivated.png", 379, 167, 451, 290)
    game.display.message_display(screen, "PSEUDO", 24, 481, 330, blue)
    game.display.message_display_right(screen, f"{game.save.name}", 24, 800, 330, blue)
    game.display.message_display(screen, "MODE", 24, 481, 360, blue)
    game.display.message_display_right(screen, f"{game.save.mode}", 24, 800, 360, blue)
    game.display.message_display(screen, "Classe", 24, 481, 390, blue)
    game.display.message_display_right(screen, f"{game.save.role}", 24, 800, 390, blue)
    game.display.message_display(screen, "NIVEAU / RANG", 24, 481, 420, blue)
    if game.save.level is not None and game.save.rank is not None:
        game.display.message_display_right(screen, f"{game.save.level} / H{game.save.rank}", 24, 800, 420, blue)
    else:
        game.display.message_display_right(screen, "None / None", 24, 800, 420, blue)

def player_creation():
    """ Affiche le menu de création du personnage """
    if game.player.mode == "Normal":
        game.display.load_image_position(screen, "assets/menu/create/orange_fill.png", 1280, 720, 0, 0)
    elif game.player.mode == "Hardcore":
        game.display.load_image_position(screen, "assets/menu/create/red_fill.png", 1280, 720, 0, 0)
    else:
        game.display.load_image_position(screen, "assets/menu/home/fill.jpg", 1280, 720, 0, 0)
    game.display.load_image_position(screen, "assets/menu/home/heretic.png", 427, 540, 600, 100)
    game.display.load_image_position(screen, "assets/menu/home/background_menu.png", 256, 432, 275, 200)
    game.display.load_image_position(screen, "assets/menu/create/sign_boy.png", 66, 66, 320, 540)
    game.display.load_image_position(screen, "assets/menu/create/sign_girl.png", 66, 66, 418, 540)
    game.display.load_image_position(screen, "assets/menu/create/input_box.png", 320, 29, 653, 230)
    game.display.load_image_position(screen, "assets/menu/create/role_designer.png", 100, 100, 647, 315)
    game.display.load_image_position(screen, "assets/menu/create/role_developper.png", 100, 100, 763, 315)
    game.display.load_image_position(screen, "assets/menu/create/role_philosopher.png", 100, 100, 877, 315)
    game.display.load_image_position(screen, "assets/menu/create/normal_mode.png", 100, 100, 690, 460)
    game.display.load_image_position(screen, "assets/menu/create/hardcore_mode.png", 100, 100, 835, 460)
    if game.player.mode != ""  and game.player.role != "" and game.player.name != "" and game.player.gender != "":
        game.display.load_image_position(screen, "assets/menu/create/create_button.png", 100, 50, 760, 570)
    game.display.message_display_center(screen, "Pseudo", 24, 813, 215, white)
    game.display.message_display_center(screen, game.player.name, 24, 813, 245, black)
    game.display.message_display_center(screen, "Classe", 24, 813, 300, white)
    game.display.message_display_center(screen, "Mode", 24, 813, 445, white)
    game.display.message_display_center(screen, f"{game.player.mode}", 80, 403, 170, black)
    if game.player.role !=  "":
        game.display.message_display_center(screen, f"< {game.player.role} >", 24, 402, 520, white)
    if game.player.gender == "girl":
        game.display.load_image_position(screen, "assets/player/girl/girl_front.png", 182, 240, 310, 265)
        game.display.load_image_position(screen, "assets/menu/create/pressed_sign_girl.png", 66, 66, 418, 540)
    elif game.player.gender == "boy":
        game.display.load_image_position(screen, "assets/player/boy/boy_front.png", 213, 250, 295, 255)
        game.display.load_image_position(screen, "assets/menu/create/pressed_sign_boy.png", 66, 66, 320, 540)
    if game.player.role == "Designer":
        game.display.load_image_position(screen, "assets/menu/create/pressed_role_designer.png", 100, 100, 647, 315)
    elif game.player.role == "Développeur":
        game.display.load_image_position(screen, "assets/menu/create/pressed_role_developper.png", 100, 100, 763, 315)
    elif game.player.role == "Philosophe":
        game.display.load_image_position(screen, "assets/menu/create/pressed_role_philosopher.png", 100, 100, 877, 315)
    if game.player.mode == "Normal":
        game.display.load_image_position(screen, "assets/menu/create/pressed_normal_mode.png", 100, 100, 690, 460)
    elif game.player.mode == "Hardcore":
        game.display.load_image_position(screen, "assets/menu/create/pressed_hardcore_mode.png", 100, 100, 835, 460)
    if active:
        game.display.load_image_position(screen, "assets/menu/create/cursor.png", 40, 20, input_box_rect.centerx - 20 + len(game.player.name) * 4.3, 260)
    else:
        game.display.message_display_center(screen, game.player.name, 30, 403, 233, white)

def about_us():
    """ Affiche les informations relative au jeu """
    game.display.load_image_position(screen, "assets/menu/home/fill.jpg", 1280, 720, 0, 0)
    game.display.load_image_position(screen, "assets/menu/home/heretic.png", 427, 540, 426, 100)
    game.display.message_display(screen, "Dev: Thanh-Long Pham      Designer: Louis Leveneur", 24, 450, 210, white)
    game.display.message_display(screen, "Dans le cadre de notre projet de programmation donné", 24, 440, 255, white)
    game.display.message_display(screen, "par Mr Loïc Janin en H1, il nous a été demandé de réal-", 24, 440, 285, white)
    game.display.message_display(screen, "iser un jeu dans le style RPG textuel sur Python.", 24, 440, 315, white)
    game.display.message_display(screen, "Nous avons donc décider de pousser ce projet aux cou-", 24, 440, 345, white)
    game.display.message_display(screen, "leurs d'Hetic au maximum en utilisant le module pyga-", 24, 440, 375, white)
    game.display.message_display(screen, "me. Ce projet représente un mois entier de travail.", 24, 440, 405, white)
    game.display.message_display(screen, "Merci aux intervenants pour leur participation :", 24, 440, 450, white)
    game.display.message_display(screen, "Grégoire Charassin", 24, 470, 480, white)
    game.display.message_display(screen, "Joël Fauvelet de Charbonnière de Bourienne", 24, 470, 510, white)
    game.display.message_display(screen, "Frédéric Martinez", 24, 470, 540, white)
    game.display.message_display(screen, "Priscille Marty", 24, 470, 570, white)
    game.display.message_display(screen, "Loïc Janin", 24, 470, 600, white)

# Indique sur quel menu on est
choice = "home_menu"

# Définit que l'on est pas dans un champ de texte
active = False

# Boucle du principale du jeu
running = True
while running:

    # Raffraichie la fenêtre
    pygame.display.flip()

    # Vérifie si il faut afficher le menu de départ
    if choice == "home_menu":

        # Affiche le menu de départ
        menu()
        game.player.reset()

        # Définit les rectangles des différents boutons
        new_button_rect = game.display.load_image_rect("assets/menu/home/new_button.png", 379, 57, 451, 215)
        load_button_rect = game.display.load_image_rect("assets/menu/home/load_button.png", 379, 167, 451, 290)
        about_button_rect = game.display.load_image_rect("assets/menu/home/about_us_button.png", 379, 57, 451, 480)
        exit_button_rect = game.display.load_image_rect("assets/menu/home/exit_button.png", 379, 57, 451, 560)

    # Vérifie si on veut créer une nouvelle partie
    elif choice == "new_game":

        # Affiche la création du personnage
        player_creation()

        # Définit les rectangles des différents boutons
        sign_boy_rect = game.display.load_image_rect("assets/menu/create/sign_boy.png", 66, 66, 320, 540)
        sign_girl_rect = game.display.load_image_rect("assets/menu/create/sign_girl.png", 66, 66, 418, 540)
        input_box_rect = game.display.load_image_rect("assets/menu/create/input_box.png", 320, 29, 650, 230)
        designer_button = game.display.load_image_rect("assets/menu/create/role_designer.png", 100, 100, 640, 315)
        developper_button = game.display.load_image_rect("assets/menu/create/role_developper.png", 100, 100, 755, 315)
        philosophe_button = game.display.load_image_rect("assets/menu/create/role_philosopher.png", 100, 100, 870, 315)
        normal_button = game.display.load_image_rect("assets/menu/create/normal_mode.png", 100, 100, 690, 460)
        hardcore_button = game.display.load_image_rect("assets/menu/create/hardcore_mode.png", 100, 100, 820, 460)
        create_button = game.display.load_image_rect("assets/menu/create/create_button.png", 100, 500, 760, 570)

    # Affiche le tutoriel après la création du personnage
    elif choice == "tutorial":

        # Affiche le tutoriel
        game.display.tutorial(screen)

        # Définit les rectangles des boutons
        if game.display.phase == -1:
            next_tutorial_button_rect = game.display.load_image_rect("assets/fight/button.png", 150, 30, 565, 400)

        elif game.display.phase == -2:
            begin_button_rect = game.display.load_image_rect("assets/fight/button.png", 200, 40, 540, 395)

        elif game.display.phase == 2:
            choice = ""
            game.display.phase = 0

    # Vérifie si le jeu est lancé
    if game.is_playing:

        # Applique l'image de la map
        game.display.load_image_position(screen, f"assets/map/{game.map_y}_{game.map_x}.jpg", 1280, 540, 0, 0)

        # Appliquer l'ensemble des images des groupe de téléporteurs
        if game.current_room.warp_north is not None:
            game.current_room.warp_north.draw(screen)

        if game.current_room.warp_south is not None:
            game.current_room.warp_south.draw(screen)

        if game.current_room.warp_east is not None:
            game.current_room.warp_east.draw(screen)

        if game.current_room.warp_west is not None:
            game.current_room.warp_west.draw(screen)

        if game.current_room.warp_south_east is not None:
            game.current_room.warp_south_east.draw(screen)

        if game.current_room.warp_south_west is not None:
            game.current_room.warp_south_west.draw(screen)

        if game.current_room.warp_north_east is not None:
            game.current_room.warp_north_east.draw(screen)

        if game.current_room.warp_north_west is not None:
            game.current_room.warp_north_west.draw(screen)

        # Appliquer l'ensemble des images de mon groupe de monstre
        if game.current_room.enemy_sprites_x is not None:
            game.current_room.enemy_sprites_x.draw(screen)
        if game.current_room.enemy_sprites_y is not None:
            game.current_room.enemy_sprites_y.draw(screen)
        if game.current_room.npc_sprites is not None:
            game.current_room.npc_sprites.draw(screen)

        # Déclenche les informations de la partie
        game.update(screen)

        # Définit les rectangles des différents boutons
        stats_button_rect = game.display.load_image_rect("assets/lower_screen/stats.png", 45, 45, 8, 603)
        inventory_button_rect = game.display.load_image_rect("assets/lower_screen/bag.png", 45, 45, 8, 552)

        # Met à jour la minimap lors d'un changement de map
        if game.minimap_update:
            game.display.minimap(screen)

        # Codes spéciaux
        if game.pressed.get(pygame.K_LALT):
            # Augmente le level
            if game.pressed.get(pygame.K_t) and game.pressed.get(pygame.K_l):
                game.player.xp += game.player.max_xp
                game.inventory.money = 1000
                game.player.level_update()
                game.display.lower_screen(screen)
                game.display.chat_logs(screen, "")
                game.display.chat_logs(screen, "")
                game.display.chat_logs(screen, "#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#", 0, (blue))
                game.display.chat_logs(screen, f"Le niveau de {game.player.name} a été augmenté.", 0, (blue))
                game.display.chat_logs(screen, "#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#", 0, (blue))

            # Reset le joueur
            elif game.pressed.get(pygame.K_l):
                game.player.level = 1
                game.player.rank = 1
                game.player.rank_change = 0
                game.player.attack = 2
                game.player.defence = 0
                game.player.health = 10
                game.player.max_health = 10
                game.player.energy = 5
                game.player.max_energy = 5
                game.player.level_update()
                game.display.lower_screen(screen)
                game.display.chat_logs(screen, "")
                game.display.chat_logs(screen, "")
                game.display.chat_logs(screen, "#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#", 0, (blue))
                game.display.chat_logs(screen, f"Le niveau de {game.player.name} a été remis à zéro.", 0, (blue))
                game.display.chat_logs(screen, "#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#", 0, (blue))

            # Change la classe
            elif game.pressed.get(pygame.K_p):
                if game.player.role == "Développeur":
                    game.player.role = "Philosophe"
                elif game.player.role == "Philosophe":
                    game.player.role = "Designer"
                else:
                    game.player.role = "Développeur"
                game.display.lower_screen(screen)
                game.display.chat_logs(screen, "")
                game.display.chat_logs(screen, "")
                game.display.chat_logs(screen, "#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#", 0, (blue))
                game.display.chat_logs(screen, f"La classe de {game.player.name} a été mis à jour.", 0, (blue))
                game.display.chat_logs(screen, "#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#?!#¿¡#", 0, (blue))

    # Vérifie si le joueur est en combat
    elif game.fight.in_fight:
        # Lance le combat
        game.fight.fight_enemy(screen)

        # Définit les rectangles des différents boutons
        next_button_rect = game.display.load_image_rect("assets/fight/button.png", 120, 30, 1084, 679)
        previous_button_rect = game.display.load_image_rect("assets/fight/button.png", 120, 30, 1084, 629)
        first_button_rect = game.display.load_image_rect("assets/fight/button.png", 420, 60, 210, 560)
        second_button_rect = game.display.load_image_rect("assets/fight/button.png", 420, 60, 650, 560)
        third_button_rect = game.display.load_image_rect("assets/fight/button.png", 420, 60, 210, 640)
        fourth_button_rect = game.display.load_image_rect("assets/fight/button.png", 420, 60, 650, 640)

    # Vérifie si le joueur est en train d'intéragir
    elif game.interaction.interaction:

        # Si il intéragit avec un pnj, lance l'intéraction
        game.interaction.npc_interaction(screen)

        # Si le pnj est le vendeur
        if game.interaction.npc_name == "Vendeur":

            # Définit les rectangles des différents boutons
            previous_leave_button_rect = game.display.load_image_rect("assets/fight/button.png", 150, 30, 1023, 410)
            first_choice_button_rect = game.display.load_image_rect("assets/fight/button.png", 356, 52, 275, 321)
            second_choice_button_rect = game.display.load_image_rect("assets/fight/button.png", 356, 52, 647, 321)
            third_choice_button_rect = game.display.load_image_rect("assets/fight/button.png", 356, 52, 275, 389)
            fourth_choice_button_rect = game.display.load_image_rect("assets/fight/button.png", 356, 52, 647, 389)

        if game.interaction.npc_name in ["M. Janin", "Mme. Marty", "M. Charrassin"]:
            # Définit les rectangles des différents boutons
            skill_next_button_rect = game.display.load_image_rect("assets/fight/button.png", 150, 30, 565, 350)

    # Vérifie si la fenêtre des stats est ouverte
    elif game.display.stats_window:
        game.display.show_stats(screen)

        #Définit le rectangle du bouton retour
        stats_previous_button_rect = game.display.load_image_rect("assets/fight/button.png", 100, 30, 760, 435)

    # Vérifie si la fenêtre de l'inventaire est ouverte
    elif game.display.inventory_window:
        game.display.show_inventory(screen)

        # Définit les rectangles des différents boutons
        previous_inventory_button_rect = game.display.load_image_rect("assets/fight/button.png", 150, 30, 901, 352)
        first_inventory_button_rect = game.display.load_image_rect("assets/fight/button.png", 300, 60, 427, 168)
        second_inventory_button_rect = game.display.load_image_rect("assets/fight/button.png", 300, 60, 751, 168)
        third_inventory_button_rect = game.display.load_image_rect("assets/fight/button.png", 300, 60, 427, 252)
        fourth_inventory_button_rect = game.display.load_image_rect("assets/fight/button.png", 300, 60, 751, 252)

    # Récupère les évènements
    for event in pygame.event.get():
        # Ferme la fenêtre lorsque l'on appuie sur la croix rouge
        if event.type == pygame.QUIT :
            running = False

        # Si une touche est appuyée, la met avec la valeur True dans un dictionnaire
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if choice == "new_game":
                if active:
                    if event.key == pygame.K_RETURN:
                        active = False
                    elif game.pressed.get(pygame.K_BACKSPACE) and len(game.player.name) > 0:
                        game.player.name = game.player.name[:-1]
                    elif len(game.player.name) < 12:
                        game.player.name += event.unicode

        # Si une touche est relachée, la met avec la valeur False dans un dictionnaire
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # Si le bouton entrer est appuyé
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if choice == "home_menu":

                # Vérifie si la souris est en collision avec le bouton New Game
                if new_button_rect.collidepoint(event.pos):

                    # Ouvre la fenêtre pour créer une nouvelle partie
                    game.player.reset()
                    game.map_y, game.map_x = (5, 2)
                    game.current_room = game.rooms[5][2][0]
                    choice = "new_game"

                # Vérifie si la souris est en collision avec le bouton Load Game
                elif load_button_rect.collidepoint(event.pos):

                    # Vérifie si il y a un fichier de sauvegarde
                    if os.path.isfile("save/player_save.heretic"):
                       # Charge la sauvegarde si il y en a une
                        choice = ""
                        game.save.load_save()
                        game.current_room = game.rooms[game.map_y][game.map_x][0]
                        game.is_playing = True
                        game.display.lower_screen(screen)
                        game.save.load_chat()
                        game.display.chat_logs(screen, game.save.player_information[18], 0, game.save.player_information[23])

                # Vérifie si la souris est en collision avec le bouton d'informations
                elif about_button_rect.collidepoint(event.pos):

                    # Permet d'afficher les informations relative au jeu
                    choice = "about"
                    about_us()

                # Vérifie si la souris est en collision avec le bouton Quit
                elif exit_button_rect.collidepoint(event.pos):

                    # Quitte le jeu
                    running = False

            elif choice == "about":
                choice = "home_menu"

            elif choice == "new_game":
                # Vérifie si la souris est en collision avec le champ de pseudo
                if input_box_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                # Vérifie si la souris est en collision avec le bouton garçon
                if sign_boy_rect.collidepoint(event.pos):
                    game.player.gender = "boy"

                # Vérifie si la souris est en collision avec le bouton fille
                elif sign_girl_rect.collidepoint(event.pos):
                    game.player.gender = "girl"

                # Vérifie si la souris est en collision avec le bouton Designer
                elif designer_button.collidepoint(event.pos):
                    game.player.role = "Designer"

                # Vérifie si la souris est en collision avec le bouton Développeur
                elif developper_button.collidepoint(event.pos):
                    game.player.role = "Développeur"

                # Vérifie si la souris est en collision avec le bouton Philosophe
                elif philosophe_button.collidepoint(event.pos):
                    game.player.role = "Philosophe"

                # Vérifie si la souris est en collision avec le bouton Normal
                elif normal_button.collidepoint(event.pos):
                    game.player.mode = "Normal"

                # Vérifie si la souris est en collision avec le bouton Hardcore
                elif hardcore_button.collidepoint(event.pos):
                    game.player.mode = "Hardcore"

                # Vérifie si la souris est en collision avec le bouton créer
                elif create_button.collidepoint(event.pos):
                    if not active and game.player.role != "" and game.player.mode != "" and game.player.name != "" and game.player.gender != "":
                        choice = "tutorial"

            elif choice == "tutorial":
                if game.display.phase == -1:
                    # Vérifie si la souris est en collision avec le bouton Suivant
                    if next_tutorial_button_rect.collidepoint(event.pos):
                        game.display.phase = 1

                elif game.display.phase == -2:
                    # Vérifie si la souris est en collision avec le bouton Commencer
                    if begin_button_rect.collidepoint(event.pos):
                        game.display.phase = 2

            elif game.fight.in_fight:
                # Vérifie si la souris est en collision avec le bouton Suivant
                if next_button_rect.collidepoint(event.pos):
                    if game.fight.phase == -1:
                        game.fight.phase = 1

                    elif game.fight.phase == -2 and not game.fight.dead_enemy and not game.fight.dead_player:
                        game.fight.phase = 2

                    elif game.fight.phase == -777:
                        game.fight.in_fight = False
                        game.is_playing = True
                        game.display.lower_screen(screen)
                        game.save.load_chat()
                        game.display.chat_logs(screen, game.save.player_information[18], 0, game.save.player_information[23])

                    elif game.fight.phase == 13062002:
                        game.is_playing = False
                        game.fight.in_fight = False
                        game.display.load_image_position(screen, "assets/menu/loading_screen.jpg", 1280, 720, 0, 0)
                        game.end = True

                    elif game.fight.phase == -666:
                        game.fight.in_fight = False
                        game.player.reset()
                        game.fight.reset()
                        game.inventory.reset_inventory()
                        choice = "home_menu"

                    elif game.fight.dead_enemy:
                        game.fight.phase = 777

                    elif game.fight.dead_player:
                        game.fight.phase = 666

                    elif game.fight.phase == -3:
                        game.fight.phase = 1

                    elif game.fight.phase == 1111:
                        game.display.load_image_position(screen, "assets/menu/loading_screen.jpg", 1280, 720, 0, 0)

                # Vérifie si la souris est en collision avec le bouton Précédent
                elif previous_button_rect.collidepoint(event.pos):
                    if game.fight.objects != 0:
                        game.fight.objects = 0

                    elif game.fight.phase == 1 and game.fight.objects == 0 and game.fight.action == 2 or game.fight.action == 3:
                        game.fight.action = 0

                elif game.fight.phase == 1:
                    # Vérifie si la souris est en collision avec le premier bouton
                    if first_button_rect.collidepoint(event.pos):
                        if game.fight.action == 0:
                            game.fight.action = 1

                        elif game.fight.action == 3 and game.fight.objects == 0:
                            game.fight.objects = 1

                        elif game.fight.objects != 0 or game.fight.action == 2:
                            game.fight.used = 1

                    # Vérifie si la souris est en collision avec le second bouton
                    elif second_button_rect.collidepoint(event.pos):
                        if game.fight.action == 0:
                            game.fight.action = 2

                        elif game.fight.action == 3  and game.fight.objects == 0:
                            game.fight.objects = 2

                        elif game.fight.objects != 0 or game.fight.action == 2:
                            game.fight.used = 2

                    # Vérifie si la souris est en collision avec le troisième bouton
                    elif third_button_rect.collidepoint(event.pos):
                        if game.fight.action == 0:
                            game.fight.action = 3

                        elif game.fight.action == 3 and game.fight.objects == 0:
                            game.fight.objects = 3

                        elif game.fight.objects != 0 or game.fight.action == 2:
                            game.fight.used = 3

                    # Vérifie si la souris est en collision avec le quatrième bouton
                    elif fourth_button_rect.collidepoint(event.pos):
                        if game.fight.action == 0:
                            game.fight.action = 4

                        elif game.fight.action == 3 and game.fight.objects == 0:
                            game.fight.objects = 4

                        elif game.fight.objects != 0 or game.fight.action == 2:
                            game.fight.used = 4

            elif game.end:
                game.end = False
                choice = "home_menu"

            elif game.interaction.interaction:
                if game.interaction.npc_name == "Vendeur":
                    # Vérifie si la souris est en collision avec le bouton Précédent / Quitter
                    if previous_leave_button_rect.collidepoint(event.pos):
                        if game.interaction.show == -2:
                            game.is_playing = True
                            game.display.chat_logs(screen, "Vendeur : Merci d'avoir visité Gaby cook, au plaisir de te revoir !")
                            game.interaction.show = -1
                            game.interaction.interaction = False

                        else:
                            game.interaction.show = 0

                    # Vérifie si la souris est en collision avec le premier bouton
                    elif first_choice_button_rect.collidepoint(event.pos):
                        if game.interaction.show == -2:
                            game.interaction.show = 1

                        elif game.interaction.show != -2:
                            game.interaction.action = 1

                    # Vérifie si la souris est en collision avec le second bouton
                    if second_choice_button_rect.collidepoint(event.pos):
                        if game.interaction.show == -2:
                            game.interaction.show = 2

                        elif game.interaction.show != -2:
                            game.interaction.action = 2

                    # Vérifie si la souris est en collision avec le troisième bouton
                    if third_choice_button_rect.collidepoint(event.pos):
                        if game.interaction.show == -2:
                            game.interaction.show = 3

                        elif game.interaction.show != -2:
                            game.interaction.action = 3

                    # Vérifie si la souris est en collision avec le quatrième bouton
                    if fourth_choice_button_rect.collidepoint(event.pos):
                        if game.interaction.show == -2:
                            game.interaction.show = 4

                        elif game.interaction.show != -2:
                            game.interaction.action = 4

                elif game.interaction.npc_name in ["M. Janin", "Mme. Marty", "M. Charrassin"]:
                    # Vérifie si la souris est en collision avec le bouton Suivant
                    if skill_next_button_rect.collidepoint(event.pos):
                        game.interaction.show = -1
                        game.interaction.interaction = False
                        game.is_playing = True

            elif game.display.stats_window:
                # Vérifie si la souris est en collision avec le bouton Retour
                if stats_previous_button_rect.collidepoint(event.pos):
                    game.display.stats_window = False
                    game.is_playing = True

            elif game.display.inventory_window:
                # Vérifie si la souris est en collision avec le bouton Précédent
                if previous_inventory_button_rect.collidepoint(event.pos):
                    if game.display.objects == 0:
                        game.display.inventory_window = False
                        game.is_playing = True

                    else:
                        game.display.objects = 0

                # Vérifie si la souris est en collision avec le premier bouton
                elif first_inventory_button_rect.collidepoint(event.pos):
                    if game.display.objects == 0:
                        game.display.objects = 1

                    else:
                        game.display.used = 1

                # Vérifie si la souris est en collision avec le second bouton
                elif second_inventory_button_rect.collidepoint(event.pos):
                    if game.display.objects == 0:
                        game.display.objects = 2

                    else:
                        game.display.used = 2

                # Vérifie si la souris est en collision avec le troisième bouton
                elif third_inventory_button_rect.collidepoint(event.pos):
                    if game.display.objects == 0:
                        game.display.objects = 3

                    else:
                        game.display.used = 3

                # Vérifie si la souris est en collision avec le quatrième bouton
                elif fourth_inventory_button_rect.collidepoint(event.pos):
                    if game.display.objects == 0:
                        game.display.objects = 4

                    else:
                        game.display.used = 4

            elif game.is_playing:
                # Vérifie si la souris est en collision avec le bouton Statut
                if stats_button_rect.collidepoint(event.pos):
                    game.display.stats_window = True
                    game.is_playing = False

                # Vérifie si la souris est en collision avec le bouton Inventaire
                elif inventory_button_rect.collidepoint(event.pos):
                    game.display.inventory_window = True
                    game.is_playing = False

        # Vérifie si la touche ECHAP est appuyé
        if game.pressed.get(pygame.K_ESCAPE):

            #Affiche le menu de départ
            if game.is_playing:
                game.save.save_game()
                game.is_playing = False
            if game.fight.in_fight:
                game.fight.enemy.remove()
            choice = "home_menu"
            game.fight.reset()
            game.player.reset()
            game.interaction.reset()
            game.inventory.reset_inventory()
