"Fichier pour le jeu"
import pygame
from display import Display
from save import Save
from player import Player
from skills import Skills
from inventory import Inventory
from fight import Fight
from interaction import Interaction
from monster import Shop_keeper
from monster import Design_master
from monster import Dev_master
from monster import Philo_master
from monster import Boss_normal
from monster import Boss_hardcore
from monster import Developper
from monster import Designer
from monster import Philosophe
from warp import Warp_north
from warp import Warp_south
from warp import Warp_east
from warp import Warp_north_east
from warp import Warp_south_east
from warp import Warp_west
from warp import Warp_north_west
from warp import Warp_south_west

# Crée une classe qui représente le jeu
class Game():
    """ Définit les informations du jeu """
    def __init__(self):
        # Le jeu est lancé
        self.is_playing = False

        # Charge l'affichage
        self.display = Display(self)

        # Charge la sauvegarde
        self.save = Save(self)

        # Charge le joueur
        self.player = Player()

        # Charge les attaques spéciales
        self.skills = Skills(self)

        # Charge l'inventaire
        self.inventory = Inventory(self)

        # Charge les combats
        self.fight = Fight(self)

        # Charge les intéractions avec les pnj
        self.interaction = Interaction(self)

        # Stock les touches pressés
        self.pressed = {}

        # Permet de se déplacer dans la map
        self.map_y = 5
        self.map_x = 2

        # Permet d'afficher la fin
        self.end = False

        # Permet de faire apparaître le boss
        self.spawn_boss = True

        # Définit la map où l'on est
        self.rooms = [
            [[           ],[             ],[Mini_salle2()],[Classe5()    ],[Classe4()]],#0
            [[Profs()    ],[CouloirG2()  ],[Mini_salle1()],[CouloirD2()  ],[Classe3()]],#1
            [[DarkVador()],[CouloirG1()  ],[Amphi()      ],[CouloirD1()  ],[Classe2()]],#2
            [[           ],[BureauDenis()],[Hall()       ],[ToiletteF()  ],[Classe1()]],#3
            [[           ],[Bureau()     ],[             ],[ToiletteH()  ],[          ]],#4
            [[           ],[Assos()      ],[Dehors()     ],[Schrodinger()],[          ]],#5
            [[           ],[Failen9()    ],[FoyerBureau()],[Synerg()     ],[          ]],#6
            ]      #0            #1              #2              #3             #4
        self.current_room = self.rooms[self.map_y][self.map_x][0]

        # Affiche la minimap
        self.minimap_update = True

        # Permet de compter le nombre de pas du joueur
        self.walk_count = 0


    def check_collision(self, sprite, group):
        """ Permet de check si il y a une collision entre 'une image' et 'un groupe' """
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def player_image_change(self):
        """ Permet d'adapter l'image du joueur en fonction du déplacement """
        # Permet d'enchainer les différentes images du joueur
        if self.walk_count + 1 >= 20:
            self.walk_count = 0
        if self.player.standby:
            self.player.image = self.display.load_image(f"assets/player/{self.player.gender}/{self.player.gender}_{self.player.orientation}.png", self.player.hitbox_x, self.player.hitbox_y)
        else:
            walk_image = [self.display.load_image(f"assets/player/{self.player.gender}/{self.player.gender}_{self.player.orientation}.png", self.player.hitbox_x, self.player.hitbox_y),
            self.display.load_image(f"assets/player/{self.player.gender}/{self.player.gender}_{self.player.orientation}_up.png", self.player.hitbox_x, self.player.hitbox_y),
            self.display.load_image(f"assets/player/{self.player.gender}/{self.player.gender}_{self.player.orientation}.png", self.player.hitbox_x, self.player.hitbox_y),
            self.display.load_image(f"assets/player/{self.player.gender}/{self.player.gender}_{self.player.orientation}_down.png", self.player.hitbox_x, self.player.hitbox_y)]
            self.player.image = walk_image[self.walk_count//5]
            self.walk_count += 1

    def update(self, screen):
        """ Met à jour le joueur """

        if not self.end and self.spawn_boss:
            if self.map_y == 2 and self.map_x == 2:
                if self.player.mode == "Normal":
                    self.current_room.enemy_sprites_x.add(Boss_normal(300, 335, 0))
                else:
                    self.current_room.enemy_sprites_x.add(Boss_hardcore(300, 335, 0))
                self.spawn_boss = False

        # Si on sur la map désignée, affiche la bulle du pnj
        if self.map_y == 5 and self.map_x == 2:
            self.display.load_image_position(screen, "assets/npc/emot_shop.png", 50, 50, 1045, 40)

        elif self.map_y == 1 and self.map_x == 0:
            if self.player.role == "Philosophe":
                x = 643
                y = 195

            elif self.player.role == "Développeur":
                x = 443
                y = 113

            else:
                x = 905
                y = 130

            if self.player.rank_change > 0 and self.player.rank != 5:
                self.display.load_image_position(screen, "assets/npc/emot_master_true.png", 50, 50, x, y)

            elif self.player.rank_change == 0 and self.player.rank != 5:
                self.display.load_image_position(screen, "assets/npc/emot_master_false.png", 50, 50, x, y)

        # Si on est sur la map, désactive le téléporteur
        elif self.player.level < 8 and self.map_y == 2 and self.map_x == 3:
            self.display.load_image_position(screen, "assets/map/warp_off.png", 50, 50, 545, 200)

        elif self.map_y == 2 and self.map_x == 1:
            self.display.load_image_position(screen, "assets/map/warp_off.png", 50, 50, 661, 224)

        elif self.map_y == 2 and self.map_x == 2:
            self.display.load_image_position(screen, "assets/map/warp_off.png", 50, 50, 212, 408)

        # Applique l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Anime le déplacement du joueur
        self.player_image_change()

        # Si le joueur n'est pas en combat
        if not self.fight.in_fight:
            # Fait déplacer les monstres en x et si il rentre en contact avec eux, lance le combat
            if self.current_room.enemy_sprites_x is not None:
                for monster in self.current_room.enemy_sprites_x:
                    monster.move_x()
                self.start_fight(self.current_room.enemy_sprites_x)

            # Fait déplacer les monstres en y et si il rentre en contact avec eux, lance le combat
            if self.current_room.enemy_sprites_y is not None:
                for monster in self.current_room.enemy_sprites_y:
                    monster.move_y()
                self.start_fight(self.current_room.enemy_sprites_y)

            # Permet d'intéragir avec les pnj
            if self.current_room.npc_sprites is not None and self.pressed.get(pygame.K_SPACE):
                for npc in self.check_collision(self.player, self.current_room.npc_sprites):
                    self.interaction.npc_name = npc.name
                    self.is_playing = False
                    self.interaction.interaction = True

            # Permet de créer les collisions avec les murs
            self.collisions(self.current_room.wall_list)

        # Permet de se déplacer
        if ((self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d)) and self.player.rect.x + self.player.rect.width < screen.get_width()):
            self.player.move_right()
            self.player.standby = False
            self.player.orientation = "right"

        elif (self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_q)) and self.player.rect.x > 0:
            self.player.move_left()
            self.player.standby = False
            self.player.orientation = "left"

        elif (self.pressed.get(pygame.K_UP) or self.pressed.get(pygame.K_z)) and self.player.rect.y > 0:
            self.player.move_up()
            self.player.standby = False
            self.player.orientation = "back"

        elif (self.pressed.get(pygame.K_DOWN) or self.pressed.get(pygame.K_s)) and self.player.rect.y + self.player.rect.height < 540:
            self.player.move_down()
            self.player.standby = False
            self.player.orientation = "front"
        else:
            self.player.standby = True

        # Permet de débuguer le personnage
        if self.player.rect.x < 0 or (self.player.rect.x + self.player.hitbox_x) > 1280 or self.player.rect.y < 0 or (self.player.rect.y + self.player.hitbox_y) > 540:
            self.player.rect.x, self.player.rect.y = (625, 250)

        # Permet de changer de map
        if self.pressed.get(pygame.K_SPACE):
            if self.check_collision(self.player, self.current_room.warp_east):
                if self.map_y == 2 and self.map_x == 1:
                    self.player.rect.x, self.player.rect.y = (591, 180)
                    self.display.chat_logs(screen, "La porte menant à l'amphithéatre est barricadée.", 0, (255, 0, 0))
                    self.display.chat_logs(screen, "Cependant vous ressentez une aura pesante à travers le mur.", 0, (255, 0, 0))
                    self.display.chat_logs(screen, "Peut-être y'a-t-il une issue non obstruée de l'autre coté ?.", 0, (255, 0, 0))

                else:
                    if self.map_y == 2 and self.map_x == 2:
                        for monster in self.current_room.enemy_sprites_x:
                            self.current_room.enemy_sprites_x.remove(monster)
                    self.map_x += 1
                    self.minimap_update = True
                    self.player.rect.x, self.player.rect.y = self.current_room.warp_east_exit
                    self.current_room = self.rooms[self.map_y][self.map_x][0]

            elif self.check_collision(self.player, self.current_room.warp_west):
                if self.map_y == 2 and self.map_x == 3 and self.player.level < 8:
                    self.player.rect.x, self.player.rect.y = (591, 180)
                    self.display.chat_logs(screen, "Vous ressentez une puissante aura s'échapper de l'amphithéatre, le danger vous fait reculer.", 0, (255, 0, 0))
                    self.display.chat_logs(screen, "Peut-être serait-t'il plus judicieux de revenir une fois niveau 8 ?", 0, (255, 0, 0))

                else:
                    self.map_x -= 1
                    self.minimap_update = True
                    self.player.rect.x, self.player.rect.y = self.current_room.warp_west_exit
                    self.current_room = self.rooms[self.map_y][self.map_x][0]
                    if self.map_y == 2 and self.map_x == 2:
                        if self.player.mode == "Normal":
                            self.current_room.enemy_sprites_x.add(Boss_normal(300, 335, 0))
                        else:
                            self.current_room.enemy_sprites_x.add(Boss_hardcore(300, 335, 0))
                        self.spawn_boss = False

            elif self.check_collision(self.player, self.current_room.warp_north):
                if self.map_y == 5 and self.map_x == 2:
                    self.map_y = 3
                else:
                    self.map_y -= 1
                self.minimap_update = True
                self.player.rect.x, self.player.rect.y = self.current_room.warp_north_exit
                self.current_room = self.rooms[self.map_y][self.map_x][0]

            elif self.check_collision(self.player, self.current_room.warp_south):
                if self.map_y == 3 and self.map_x == 2:
                    self.map_y = 5
                else:
                    self.map_y += 1
                self.minimap_update = True
                self.player.rect.x, self.player.rect.y = self.current_room.warp_south_exit
                self.current_room = self.rooms[self.map_y][self.map_x][0]

            elif self.check_collision(self.player, self.current_room.warp_north_west):
                self.map_y -= 1
                self.map_x -= 1
                self.minimap_update = True
                self.player.rect.x, self.player.rect.y = self.current_room.warp_north_west_exit
                self.current_room = self.rooms[self.map_y][self.map_x][0]

            elif self.check_collision(self.player, self.current_room.warp_north_east):
                self.map_y -= 1
                self.map_x += 1
                self.minimap_update = True
                self.player.rect.x, self.player.rect.y = self.current_room.warp_north_east_exit
                self.current_room = self.rooms[self.map_y][self.map_x][0]

            elif self.check_collision(self.player, self.current_room.warp_south_west):
                self.map_y += 1
                self.map_x -= 1
                self.minimap_update = True
                self.player.rect.x, self.player.rect.y = self.current_room.warp_south_west_exit
                self.current_room = self.rooms[self.map_y][self.map_x][0]

            elif self.check_collision(self.player, self.current_room.warp_south_east):
                self.map_y += 1
                self.map_x += 1
                self.minimap_update = True
                self.player.rect.x, self.player.rect.y = self.current_room.warp_south_east_exit
                self.current_room = self.rooms[self.map_y][self.map_x][0]
            self.save.save_game()

    def start_fight(self, enemies):
        """ Permet de lancer le combat au contact d'un ennemu """
        # Détecte si le joueuer est en collision avec un ennemi
        for enemy in self.check_collision(self.player, enemies):
            self.fight.enemy = enemy
            self.is_playing = False
            self.fight.dead_player = False
            self.fight.dead_enemy = False
            self.fight.phase = 0
            if self.player.mode == "Hardcore":
                enemy.hardcore_rage()
            self.fight.in_fight = True
            self.skills.weapons()

    def collisions(self, walls):
        """ Permet de créer les collisions avec les murs """
        # Détecte avec quel mur le joueur rentre en collision
        wall_hit_list = self.check_collision(self.player, walls)
        for wall in wall_hit_list:
            # Si le joueur rentre dans un mur en allant vers la droite, le joueur n'avance pas
            if self.player.rect.x + self.player.hitbox_x >= wall.rect.x and self.player.orientation == "right":
                self.player.move_left()

            # Si le joueur rentre dans un mur en allant vers la gauche, le joueur n'avance pas
            elif self.player.rect.x <= wall.rect.x + wall.width and self.player.orientation == "left":
                self.player.move_right()

            # Si le joueur rentre dans un mur en allant vers le haut, le joueur n'avance pas
            elif self.player.rect.y <= wall.rect.y + wall.height and self.player.orientation == "back":
                self.player.move_down()

            # Si le joueur rentre dans un mur en allant vers le bas, le joueur n'avance pas
            elif self.player.rect.y + self.player.hitbox_y >= wall.rect.y and self.player.orientation == "front":
                self.player.move_up()

class Wall(pygame.sprite.Sprite):
    """ Définit les informations des murs """
    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (x, y)
        self.width, self.height = (width, height)

class Map():
    """ Classe de départ de toutes les salles """
    wall_list = None
    warp_north = None
    warp_south = None
    warp_east = None
    warp_west = None
    warp_south_east = None
    warp_south_west = None
    warp_north_east = None
    warp_north_west = None
    warp_north_exit = None
    warp_south_exit = None
    warp_east_exit = None
    warp_west_exit = None
    warp_south_east_exit = None
    warp_south_west_exit = None
    warp_north_east_exit = None
    warp_north_west_exit = None
    enemy_sprites_x = None
    enemy_sprites_y = None
    npc_sprites = None

    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.warp_north = pygame.sprite.Group()
        self.warp_south = pygame.sprite.Group()
        self.warp_east = pygame.sprite.Group()
        self.warp_west = pygame.sprite.Group()
        self.warp_south_east = pygame.sprite.Group()
        self.warp_south_west = pygame.sprite.Group()
        self.warp_north_east = pygame.sprite.Group()
        self.warp_north_west = pygame.sprite.Group()
        self.enemy_sprites_x = pygame.sprite.Group()
        self.enemy_sprites_y = pygame.sprite.Group()
        self.npc_sprites = pygame.sprite.Group()

# Extérieur
class Dehors(Map):
    """ Définit les informations de dehors """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 70, 0, 0],
            [1280, 28, 0, 512],
            [20, 442, 0, 70],
            [20, 442, 1260, 70]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les pnjs
        npcs = [
            [Shop_keeper, 985, 75]
        ]

        for item in npcs:
            self.npc_sprites.add(item[0].__call__(item[1], item[2]))

        # Crée les ennemis
        enemies = [
            [Philosophe, 10, "move y", 730, 265, 125],
            [Developper, 9, "move x", 150, 170, 100],
            [Designer, 3, "move y", 255, 300, 75]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée les téléporteurs
        self.warp_north.add(Warp_north(25, 270))
        self.warp_south_west.add(Warp_south_west(65, 155))
        self.warp_west.add(Warp_west(303, 155))
        self.warp_south.add(Warp_south(440, 155))
        self.warp_south.add(Warp_south(545, 155))
        self.warp_east.add(Warp_east(640, 155))
        self.warp_south_east.add(Warp_south_east(875, 155))

        # Crée les sorties des téléporteurs
        self.warp_north_exit = (670, 395)
        self.warp_south_west_exit = (477, 385)
        self.warp_west_exit = (732, 340)
        self.warp_south_exit = (605, 365)
        self.warp_east_exit = (478, 385)
        self.warp_south_east_exit = (733, 340)

class Failen9(Map):
    """ Définit les informations de la salle Failen9 """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 80, 0, 0],
            [1280, 30, 0, 510],
            [445, 435, 0, 80],
            [830, 445, 835, 80],
            [80, 190, 600, 195],
            [45, 150, 447, 80],
            [50, 50, 785, 80],
            [50, 50, 785, 465]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
         [Developper, 8, "move y", 737, 235, 100]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_north_east.add(Warp_north_east(487, 482))

        # Crée la sortie du téléporteur
        self.warp_north_east_exit = (115, 70)

class Assos(Map):
    """ Définit les informations du bureau des associations """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 125, 0, 0],
            [1280, 80, 0, 460],
            [450, 359, 0, 125],
            [445, 359, 835, 125],
            [125, 75, 570, 275],
            [100, 20, 735, 125],
            [35, 55, 800, 145],
            [40, 80, 450, 380]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Designer, 5, "move x", 597, 130, 70]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_east.add(Warp_east(742, 435))

        # Crée la sortie du téléporteur
        self.warp_east_exit = (230, 70)

class FoyerBureau(Map):
    """ Définit les informations du foyer ainsi que du bureau des étudiants """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 125, 0, 0],
            [1280, 80, 0, 460],
            [290, 359, 0, 125],
            [330, 359, 950, 125],
            [110, 110, 390, 225],
            [100, 20, 590, 120],
            [40, 20, 910, 120],
            [20, 65, 630, 250]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
        [Philosophe, 3, "move y", 805, 240, 100]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée les téléporteurs
        self.warp_north.add(Warp_north(550, 440))
        self.warp_north.add(Warp_north(680, 440))

        # Crée la sortiedu téléporteur
        self.warp_north_exit = (370, 70)

class Schrodinger(Map):
    """ Définit les informations de la salle Schrodinger dev room """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 80, 0, 0],
            [445, 435, 0, 80],
            [435, 435, 835, 80],
            [1280, 25, 0, 515],
            [45, 165, 445, 80],
            [150, 20, 685, 80],
            [55, 45, 780, 470],
            [65, 140, 615, 240]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Philosophe, 7, "move y", 733, 220, 80]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_west.add(Warp_west(488, 480))

        # Crée la sortie du téléporteur
        self.warp_west_exit = (690, 70)

class Synerg(Map):
    """ Définit les informations de la salle de Synerg'Hetic """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 125, 0, 0],
            [1280, 80, 0, 460],
            [450, 359, 0, 125],
            [440, 359, 840, 125],
            [50, 80, 450, 380],
            [30, 75, 450, 125]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Designer, 8, "move x", 560, 230, 80]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        self.warp_north_west.add(Warp_north_west(743, 435))

        self.warp_north_west_exit = (805, 70)

# Intérieur
class Hall(Map):
    """ Définit les informations du hall d'entrée """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
                [31, 540, 0, 0],
                [587, 60, 31, 200],
                [204, 250, 31, 260],
                [69, 20, 235, 260],
                [90, 20, 528, 260],
                [69, 45, 528, 465],
                [190, 100, 235, 410],
                [60, 40, 365, 370],
                [1219, 30, 31, 510],
                [21, 90, 597, 420],
                [854, 69, 148, 0],
                [32, 140, 1250, 400],
                [171, 400, 1108, 0],
                [20, 10, 375, 69]
                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Philosophe, 2, "move x" , 950, 380, 200],
            [Developper, 5, "move y", 800, 180, 100]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée les téléporteurs
        self.warp_north_west.add(Warp_north_west(65, 0))
        self.warp_north_east.add(Warp_north_east(1030, 0))
        self.warp_south_west.add(Warp_south_west(198, 150))
        self.warp_west.add(Warp_west(535, 150))
        self.warp_south_east.add(Warp_south_east(645, 150))
        self.warp_south.add(Warp_south(680, 490))

        # Crée les sorties des téléporteurs
        self.warp_north_west_exit = (587, 395)
        self.warp_north_east_exit = (600, 395)
        self.warp_south_west_exit = (480, 340)
        self.warp_west_exit = (735, 340)
        self.warp_south_east_exit = (477, 338)
        self.warp_south_exit = (75, 225)

class Bureau(Map):
    """ Définit les informations de la salle d'un bureau """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 125, 0, 0],
            [1280, 50, 0, 460],
            [445, 335, 0, 125],
            [445, 335, 835, 125],
            [30, 75, 445, 125],
            [65, 20, 475, 125],
            [45, 145, 645, 315],
            [145, 80, 690, 380]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Developper, 1, "move x", 580, 140, 75]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_north_east.add(Warp_north_east(488, 438))

        # Crée la sortie du téléporteur
        self.warp_north_east_exit = (250, 70)

class BureauDenis(Map):
    """ Définit les informations du bureau de Denis Chomel """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 125, 0, 0],
            [1280, 50, 0, 460],
            [445, 335, 0, 125],
            [445, 335, 835, 125],
            [200, 5, 650, 235],
            [30, 110, 805, 125],
            [45, 185, 445, 275]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Designer, 7, "move y", 550, 205, 60]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_east.add(Warp_east(744, 438))

        # Crée la sortie du téléporteur
        self.warp_east_exit = (460, 70)

class ToiletteH(Map):
    """ Définit les informations des toillettes pour hommes """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 125, 0, 0],
            [1280, 50, 0, 460],
            [445, 335, 0, 125],
            [445, 335, 835, 125],
            [40, 153, 447, 125],
            [203, 20, 632, 323]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Philosophe, 8, "move x", 620, 203, 100]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_north_west.add(Warp_north_west(488, 438))

        # Crée la sortie du téléporteur
        self.warp_north_west_exit = (695, 70)

# Gauche du hall
class CouloirG1(Map):
    """ Définit les informations du premier couloir de gauche"""
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [390, 540, 0, 0],
            [570, 540, 710, 0],
            [165, 75, 390, 465]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Philosophe, 5, "move y", 510, 185, 65]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée les téléporteurs
        self.warp_south_east.add(Warp_south_east(597, 490))
        self.warp_west.add(Warp_west(661, 408))
        self.warp_east.add(Warp_east(661, 224))
        self.warp_north_west.add(Warp_north_west(388, 105))
        self.warp_north.add(Warp_north(524, 0))

        # Crée les sorties des téléporteurs
        self.warp_south_east_exit = (55, 50)
        self.warp_west_exit = (605, 390)
        self.warp_east_exit = (265, 365)
        self.warp_north_west_exit = (350, 340)
        self.warp_north_exit = (515, 390)

class DarkVador(Map):
    """ Définit les informations de la salle Darkvador """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [445, 540, 0, 0],
            [445, 540, 835, 0],
            [390, 80, 445, 0],
            [390, 30, 445, 510],
            [35, 130, 445, 80],
            [15, 25, 480, 80],
            [55, 25, 780, 80]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Designer, 6, "move x", 605, 80, 50]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_east.add(Warp_east(615, 485))

        # Crée la sortie du téléporteur
        self.warp_east_exit = (590, 365)

class Profs(Map):
    """ Définit les informations de la salle des professeurs """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 130, 0, 0],
            [1280, 75, 0, 465],
            [150, 125, 545, 340],
            [300, 335, 0, 130],
            [255, 335, 1025, 130],
            [125, 25, 815, 285]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les PNJ
        npcs = [
            [Dev_master, 385, 140],
            [Philo_master, 580, 225],
            [Design_master, 840, 173]
        ]

        for item in npcs:
            self.npc_sprites.add(item[0].__call__(item[1], item[2]))

        # Crée les téléporteurs
        self.warp_south_east.add(Warp_south_east(359, 435))
        self.warp_east.add(Warp_east(871, 435))

        # Crée les sorties des téléporteurs
        self.warp_south_east_exit = (440, 60)
        self.warp_east_exit = (440, 375)

class CouloirG2(Map):
    """ Définit les informations du deuxième couloir de gauche """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [390, 540, 0, 0],
            [445, 540, 835, 0],
            [445, 75, 390, 0],
            [145, 145, 690, 395]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Developper, 2, "move y", 600, 220, 80]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée les téléporteurs
        self.warp_south.add(Warp_south(524, 490))
        self.warp_west.add(Warp_east(388, 419))
        self.warp_east.add(Warp_east(789, 293))
        self.warp_north_east.add(Warp_north_east(789, 159))

        # Crée les sorties des téléporteurs
        self.warp_south_exit = (515, 50)
        self.warp_west_exit = (860, 340)
        self.warp_east_exit = (285, 260)
        self.warp_north_east_exit = (285, 260)

class Mini_salle1(Map):
    """ Définit les informations de la première mini-salle """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 150, 0, 0],
            [1280, 75, 0, 465],
            [250, 315, 0, 150],
            [250, 315, 1030, 150],
            [50, 5, 980, 270]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Designer, 4, "move y", 590, 230, 50]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_west.add(Warp_west(232, 307))

        # Crée la sortie du téléporteur
        self.warp_west_exit = (715, 250)

class Mini_salle2(Map):
    """ Définit les informations de la seconde mini_salle """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 150, 0, 0],
            [1280, 75, 0, 465],
            [250, 315, 0, 150],
            [250, 315, 1030, 150],
            [125, 45, 465, 150],
            [55, 5, 975, 290]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Developper, 10, "move x", 605, 230, 200]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_south_west.add(Warp_south_west(232, 307))

        # Crée la sortie du téléporteur
        self.warp_south_west_exit = (715, 115)

# Milieu
class Amphi(Map):
    """ Définit les informations de l'amphithéatre """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 25, 0, 515],
            [1280, 335, 0, 0],
            [235, 280, 0, 335],
            [235, 280, 1050, 335]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Philosophe, 1, 430, 345, 40],
            [Designer, 10, 560, 345, 40],
            [Developper, 4, 690, 345, 40],
            [Philosophe, 9, 820, 345, 40]
        ]

        for item in enemies:
            self.enemy_sprites_y.add(item[0].__call__(item[1], item[2], item[3], item[4]))

        # Crée le téléporteur
        self.warp_east.add(Warp_east(1018, 409))

        # Crée la sortie du téléporteur
        self.warp_east_exit = (595, 160)

# Droite du hall
class CouloirD1(Map):
    """ Définit les informations du premier couloir de droite """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [565, 540, 0, 0],
            [570, 540, 710, 0]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les téléporteurs
        self.warp_south_west.add(Warp_south_west(610, 490))
        self.warp_south.add(Warp_south(545, 435))
        self.warp_south_east.add(Warp_south_east(677, 443))
        self.warp_west.add(Warp_west(545, 200))
        self.warp_east.add(Warp_east(677, 99))
        self.warp_north.add(Warp_north(613, 0))

        # Crée les sorties des téléporteurs
        self.warp_south_west_exit = (1020, 50)
        self.warp_south_exit = (715, 330)
        self.warp_south_east_exit = (265, 310)
        self.warp_west_exit = (945, 365)
        self.warp_east_exit = (265, 310)
        self.warp_north_exit = (605, 395)

class ToiletteF(Map):
    """ Définit les informations des toilettes pour femmes """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [460, 540, 0, 0],
            [430, 540, 850, 0],
            [390, 130, 460, 0],
            [390, 75, 460, 465],
            [140, 30, 590, 130],
            [55, 95, 790, 160],
            [200, 15, 460, 325]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Designer, 2, "move x", 715, 160, 0]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_north.add(Warp_north(819, 374))

        # Crée la sortie du téléporteur
        self.warp_north_exit = (602, 340)

class Classe1(Map):
    """ Définit les informations de la première classe """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 105, 0, 0],
            [1280, 105, 0, 435],
            [230, 330, 0, 105],
            [230, 330, 1050, 105],
            [50, 90, 865, 105],
            [45, 15, 915, 180]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Developper, 7, "move x", 500, 105, 200],
            [Philosophe, 4, "move y", 850, 245, 70]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_north_west.add(Warp_north_west(213, 353))

        # Crée la sortie du téléporteur
        self.warp_north_west_exit = (602, 340)

class Classe2(Map):
    """ Définit les informations de la seconde classe """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 105, 0, 0],
            [1280, 105, 0, 435],
            [230, 330, 0, 105],
            [230, 330, 1050, 105],
            [50, 90, 865, 105],
            [45, 15, 915, 180]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Philosophe, 6, "move y", 595, 210, 100]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_west.add(Warp_west(213, 353))

        # Crée les la sortie du téléporteur
        self.warp_west_exit = (605, 80)

class CouloirD2(Map):
    """ Définit les informations du second couloir de droite """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [560, 540, 0, 0],
            [570, 540, 710, 0],
            [150, 70, 560, 0]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les téléporteurs
        self.warp_south.add(Warp_south(613, 490))
        self.warp_east.add(Warp_east(677, 336))
        self.warp_north_east.add(Warp_north_east(677, 212))
        self.warp_north.add(Warp_north(545, 212))

        # Crée les sorties des téléporteurs
        self.warp_south_exit = (603, 50)
        self.warp_east_exit = (265, 310)
        self.warp_north_east_exit = (265, 225)
        self.warp_north_exit = (945, 225)

class Classe3(Map):
    """ Définit les informations de la troisième classe """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [1280, 105, 0, 0],
            [1280, 105, 0, 435],
            [230, 330, 0, 105],
            [230, 330, 1050, 105],
            [50, 90, 865, 105],
            [45, 15, 915, 180]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Developper, 3, "move y", 775, 220, 110]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_west.add(Warp_west(213, 353))

        # Crée la sortie du téléporteur
        self.warp_west_exit = (593, 285)

class Classe4(Map):
    """ Définit les informations de la quatrième classe """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [230, 495, 0 , 20],
            [1280, 20, 0, 0],
            [230 , 495, 1050, 20],
            [1280, 45, 0, 495],
            [190, 10, 735, 365]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Designer, 9, "move y", 595, 175, 135],
            [Developper, 6, "move x", 375, 375, 125]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_south_west.add(Warp_south_west(212, 270))

        # Crée la sortie du téléporteur
        self.warp_south_west_exit = (603, 120)

class Classe5(Map):
    """ Définit les informations de la cinquième classe """
    def __init__(self):
        Map.__init__(self)

        # Crée les murs
        walls = [
            [230, 495, 0 , 20],
            [1280, 20, 0, 0],
            [230 , 495, 1050, 20],
            [1280, 45, 0, 495],
            [50, 95, 365, 20],
            [55, 15, 310, 100]
        ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)

        # Crée les ennemis
        enemies = [
            [Designer, 1, "move y", 325, 250, 125]
        ]

        for item in enemies:
            if item[2] == "move x":
                self.enemy_sprites_x.add(item[0].__call__(item[1], item[3], item[4], item[5]))
            else:
                self.enemy_sprites_y.add(item[0].__call__(item[1], item[3], item[4], item[5]))

        # Crée le téléporteur
        self.warp_south.add(Warp_south(1018, 269))

        # Crée la sortie du téléporteur
        self.warp_south_exit = (603, 120)
