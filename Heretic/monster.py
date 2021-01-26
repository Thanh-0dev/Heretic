"Fichier pour les monstres"
from math import ceil
import pygame

# Définie une classe qui représente un monstre
class Monster(pygame.sprite.Sprite):
    """ Définit les informations du monstre """
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.health_percent = ceil(self.health / self.max_health * 100)
        self.velocity = -2
        self.attack = 1
        self.defence = 1

    def update_stats_bar(self, surface):
        """ Met à jour la barre de vie du monstre """
        self.health_percent = ceil(self.health / self.max_health * 100)
        # Dessine la barre de vie du monstre
        pygame.draw.rect(surface, (255, 255, 255), [119, 119, 243, 18])
        pygame.draw.rect(surface, (60, 60, 60), [120, 120, 241, 16])
        pygame.draw.rect(surface, (111, 210, 46), [120, 120, self.health_percent*2.41, 16])

    def move_x(self):
        """ Fait bouger le monstre sur l'axe des abscisses """
        self.rect.x -= self.velocity
        if (self.rect.x <= self.rect_spawn_x - self.movement) or (self.rect.x >= self.rect_spawn_x + self.movement):
            self.velocity = - self.velocity

    def move_y(self):
        """ Fait bouger le monstre sur l'axe des ordonnées """
        self.rect.y -= self.velocity
        if (self.rect.y <= self.rect_spawn_y - self.movement) or (self.rect.y >= self.rect_spawn_y + self.movement):
            self.velocity = - self.velocity

    def damage(self, amount):
        """ Réduit les points de vie du monstre de 'amount' """
        self.health -= amount

    def hardcore_rage(self):
        """ Renforce les ennemis lorsque l'on est en mode hardcore """
        self.max_health = int(self.max_health * 3/2)
        self.health = self.max_health
        self.attack = int(self.attack * 4/3)

    def reverse_hardcore_rage(self):
        """ Annule le buff du mode hardcore """
        self.max_health = self.max_health * 2/3
        self.health = self.max_health
        self.attack = int(self.attack * 3/4)

# Définie les classes des pnj
class Shop_keeper(Monster):
    """ Définit les informations du vendeur d'objets """
    def __init__(self, x, y):
        super().__init__()
        self.name = "Vendeur"
        self.image = pygame.image.load("assets/npc/shop_keeper.png")
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Design_master(Monster):
    """ Définit les informations du vendeur d'objets """
    def __init__(self, x, y):
        super().__init__()
        self.name = "M. Charrassin"
        self.image = pygame.image.load("assets/npc/charrassin.png")
        self.image = pygame.transform.scale(self.image, (75, 110))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Dev_master(Monster):
    """ Définit les informations du vendeur d'objets """
    def __init__(self, x, y):
        super().__init__()
        self.name = "M. Janin"
        self.image = pygame.image.load("assets/npc/janin.png")
        self.image = pygame.transform.scale(self.image, (75, 110))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Philo_master(Monster):
    """ Définit les informations du vendeur d'objets """
    def __init__(self, x, y):
        super().__init__()
        self.name = "Mme. Marty"
        self.image = pygame.image.load("assets/npc/marty.png")
        self.image = pygame.transform.scale(self.image, (75, 110))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Définie les classe du boss de chaque mode
class Boss_normal(Monster):
    """ Définit les informations du monstre """
    def __init__(self, x, y, move):
        super().__init__()
        self.name = "M. Martinez"
        self.path = "assets/enemy/martinez.png"
        self.level = "???"
        self.health = 150
        self.max_health = 150
        self.weapon = "ses poings"
        self.attack = 35
        self.defence = 15
        self.xp = 10000
        self.money = 100000
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (100, 115))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_spawn_x = self.rect.x
        self.rect_spawn_y = self.rect.y
        self.movement = move

class Boss_hardcore(Monster):
    """ Définit les informations du boss """
    def __init__(self, x, y, move):
        super().__init__()
        self.name = "M. Bourienne"
        self.path = "assets/enemy/bourienne.png"
        self.level = "???"
        self.health = 300
        self.max_health = 300
        self.weapon = "sa divinité"
        self.attack = 45
        self.defence = 20
        self.xp = 10000
        self.money = 1000000
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (100, 115))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_spawn_x = self.rect.x
        self.rect_spawn_y = self.rect.y
        self.movement = move

# Définie les ennemies
class Developper(Monster):
    """ Définit les informations du boss """
    def __init__(self, choose, x, y, move):
        super().__init__()
        if choose == 1:
            self.name = "Eugénie - Développeuse"
            self.path = "assets/enemy/eugenie_dev.png"
            self.level = 3

        elif choose == 2:
            self.name = "Clara - Développeuse"
            self.path = "assets/enemy/clara_dev.png"
            self.level = 2

        elif choose == 3:
            self.name = "Axelle - Développeuse"
            self.path = "assets/enemy/axelle_dev.png"
            self.level = 7

        elif choose == 4:
            self.name = "Valentine - Développeuse"
            self.path = "assets/enemy/valentine_dev.png"
            self.level = 9

        elif choose == 5:
            self.name = "Donia - Développeuse"
            self.path = "assets/enemy/donia_dev.png"
            self.level = 5

        elif choose == 6:
            self.name = "Romain - Développeur"
            self.path = "assets/enemy/romain_dev.png"
            self.level = 8

        elif choose == 7:
            self.name = "Tommy - Développeur"
            self.path = "assets/enemy/tommy_dev.png"
            self.level = 6

        elif choose == 8:
            self.name = "Anatole - Développeur"
            self.path = "assets/enemy/anatole_dev.png"
            self.level = 4

        elif choose == 9:
            self.name = "Hugo - Développeur"
            self.path = "assets/enemy/hugo_dev.png"
            self.level = 1

        elif choose == 10:
            self.name = "Jacques - Développeur"
            self.path = "assets/enemy/jacques_dev.png"
            self.level = 2

        self.health = int(0.5 * 4.5*(self.level * (self.level - 1))) + 8
        self.max_health = int(0.5 * 4.5*(self.level * (self.level - 1))) + 8
        self.weapon = "son macbook pro"
        self.attack = int(0.5 * self.level * (self.level - 0.25)) + 2
        self.defence = int(0.5 * self.level * (self.level - 1))
        self.xp = int((25 * self.level * (self.level + 1))/3)
        self.money = int(((self.level + 1) * (self.level + 2))/2)
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (100, 115))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_spawn_x = self.rect.x
        self.rect_spawn_y = self.rect.y
        self.movement = move

class Designer(Monster):
    """ Définit les informations du boss """
    def __init__(self, choose, x, y, move):
        super().__init__()
        if choose == 1:
            self.name = "Eugénie - Designer"
            self.path = "assets/enemy/eugenie_des.png"
            self.level = 8

        elif choose == 2:
            self.name = "Clara - Designer"
            self.path = "assets/enemy/clara_des.png"
            self.level = 6

        elif choose == 3:
            self.name = "Axelle - Designer"
            self.path = "assets/enemy/axelle_des.png"
            self.level = 1

        elif choose == 4:
            self.name = "Valentine - Designer"
            self.path = "assets/enemy/valentine_des.png"
            self.level = 2

        elif choose == 5:
            self.name = "Donia - Designer"
            self.path = "assets/enemy/donia_des.png"
            self.level = 4

        elif choose == 6:
            self.name = "Romain - Designer"
            self.path = "assets/enemy/romain_des.png"
            self.level = 2

        elif choose == 7:
            self.name = "Tommy - Designer"
            self.path = "assets/enemy/tommy_des.png"
            self.level = 3

        elif choose == 8:
            self.name = "Anatole - Designer"
            self.path = "assets/enemy/anatole_des.png"
            self.level = 5

        elif choose == 9:
            self.name = "Hugo - Designer"
            self.path = "assets/enemy/hugo_des.png"
            self.level = 7

        elif choose == 10:
            self.name = "Jacques - Designer"
            self.path = "assets/enemy/jacques_des.png"
            self.level = 9
            self.velocity = -self.velocity

        self.health = int(0.5 * 5.5*(self.level * (self.level - 1))) + 8
        self.max_health = int(0.5 * 5.5*(self.level * (self.level - 1))) + 8
        self.weapon = "sa tablette graphique"
        self.attack = int(0.5 * self.level * (self.level - 0.75)) + 2
        self.defence = int(0.5 * self.level * (self.level - 1))
        self.xp = int((25 * self.level * (self.level + 1))/3)
        self.money = int(((self.level + 1) * (self.level + 2))/2)
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (100, 115))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_spawn_x = self.rect.x
        self.rect_spawn_y = self.rect.y
        self.movement = move

class Philosophe(Monster):
    """ Définit les informations du boss """
    def __init__(self, choose, x, y, move):
        super().__init__()
        if choose == 1:
            self.name = "Eugénie - Philosophe"
            self.path = "assets/enemy/eugenie_phi.png"
            self.level = 9

        elif choose == 2:
            self.name = "Clara - Philosophe"
            self.path = "assets/enemy/clara_phi.png"
            self.level = 3

        elif choose == 3:
            self.name = "Axelle - Philosophe"
            self.path = "assets/enemy/axelle_phi.png"
            self.level = 5

        elif choose == 4:
            self.name = "Valentine - Philosophe"
            self.path = "assets/enemy/valentine_phi.png"
            self.level = 7

        elif choose == 5:
            self.name = "Donia - Philosophe"
            self.path = "assets/enemy/donia_phi.png"
            self.level = 1

        elif choose == 6:
            self.name = "Romain - Philosophe"
            self.path = "assets/enemy/romain_phi.png"
            self.level = 7

        elif choose == 7:
            self.name = "Tommy - Philosophe"
            self.path = "assets/enemy/tommy_phi.png"
            self.level = 5

        elif choose == 8:
            self.name = "Anatole - Philosophe"
            self.path = "assets/enemy/anatole_phi.png"
            self.level = 3

        elif choose == 9:
            self.name = "Hugo - Philosophe"
            self.path = "assets/enemy/hugo_phi.png"
            self.level = 9
            self.velocity = -self.velocity

        elif choose == 10:
            self.name = "Jacques - Philosophe"
            self.path = "assets/enemy/jacques_phi.png"
            self.level = 1

        self.health = int(0.5 * 5*(self.level * (self.level - 1))) + 8
        self.max_health = int(0.5 * 5*(self.level * (self.level - 1))) + 8
        self.weapon = "son livre"
        self.attack = int(0.5 * self.level * (self.level - 0.5)) + 2
        self.defence = int(0.5 * self.level * (self.level - 1))
        self.xp = int((25 * self.level * (self.level + 1))/3)
        self.money = int(((self.level + 1) * (self.level + 2))/2)
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (100, 115))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_spawn_x = self.rect.x
        self.rect_spawn_y = self.rect.y
        self.movement = move
