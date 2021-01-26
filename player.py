"Fichier pour le joueur"
import math
import pygame

# Crée une classe qui représente le joueur
class Player(pygame.sprite.Sprite):
    """ Définit les informations du joueur """
    def __init__(self):
        self.gender = "boy"
        self.name = ""
        self.level = 1
        self.level_up = False
        self.xp = 0
        self.max_xp = 50
        self.xp_percent = math.ceil(self.xp / self.max_xp * 100)
        self.rank = 1
        self.rank_change = 0
        self.role = ""
        self.mode = ""
        self.weapon = "ses poings"
        self.shield = False
        self.orientation = "front"
        self.standby = True
        self.health = 10
        self.max_health = 10
        self.health_percent = math.ceil(self.health / self.max_health * 100)
        self.energy = 5
        self.max_energy = 5
        self.energy_percent = math.ceil(self.energy / self.max_energy * 100)
        self.attack = 4
        self.attack_boost = 0
        self.defence = 0
        self.defence_boost = 0
        self.velocity = 5
        self.image = pygame.image.load(f"assets/player/{self.gender}/{self.gender}_front.png")
        self.hitbox_x, self.hitbox_y = (70, 95)
        self.image = pygame.transform.scale(self.image, (self.hitbox_x, self.hitbox_y))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (1180, 95)

    def reset(self):
        """ Reset toutes les informations de la classe """
        self.gender = "boy"
        self.name = ""
        self.level = 1
        self.level_up = False
        self.xp = 0
        self.max_xp = 50
        self.xp_percent = math.ceil(self.xp / self.max_xp * 100)
        self.rank = 1
        self.rank_change = 0
        self.role = ""
        self.mode = ""
        self.weapon = "ses poings"
        self.shield = False
        self.orientation = "front"
        self.standby = True
        self.health = 10
        self.max_health = 10
        self.health_percent = math.ceil(self.health / self.max_health * 100)
        self.energy = 5
        self.max_energy = 5
        self.energy_percent = math.ceil(self.energy / self.max_energy * 100)
        self.attack = 4
        self.attack_boost = 0
        self.defence = 0
        self.defence_boost = 0
        self.velocity = 5
        self.image = pygame.image.load(f"assets/player/{self.gender}/{self.gender}_front.png")
        self.hitbox_x, self.hitbox_y = (70, 95)
        self.image = pygame.transform.scale(self.image, (self.hitbox_x, self.hitbox_y))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (1180, 95)

    def move_right(self):
        """ Fonction faisant bouger vers la droite l'image du joueur """
        self.rect.x += self.velocity

    def move_left(self):
        """ Fonction faisant bouger vers la gauche l'image du joueur """
        self.rect.x -= self.velocity

    def move_up(self):
        """ Fonction faisant monter l'image du joueur """
        self.rect.y -= self.velocity

    def move_down(self):
        """ Fonction faisant descendre l'image du joueur """
        self.rect.y += self.velocity

    def update_stats_bar(self, screen, mode="normal"):
        """ Dessine les différentes barre de statut du joueur """
        self.health_percent = math.ceil(self.health / self.max_health * 100)
        self.energy_percent = math.ceil(self.energy / self.max_energy * 100)
        self.xp_percent = math.ceil(self.xp / self.max_xp * 100)
        if mode == "normal":
            # Dessine la barre de vie du personnage
            pygame.draw.rect(screen, (0, 0, 0), [64, 673, 229, 16])
            pygame.draw.rect(screen, (255, 255, 255), [66, 675, 225, 12])
            pygame.draw.rect(screen, (111, 210, 46), [66, 675, self.health_percent * 2.25, 12])

            # Dessine la barre d'énergie du personnage
            pygame.draw.rect(screen, (0, 0, 0), [64, 693, 229, 16])
            pygame.draw.rect(screen, (255, 255, 255), [66, 695, 225, 12])
            pygame.draw.rect(screen, (255, 255, 51), [66, 695, self.energy_percent * 2.25, 12])

        if mode == "fight":
            # Dessine la barre de vie pendant le combat
            pygame.draw.rect(screen, (255, 255, 255), [886, 431, 238, 18])
            pygame.draw.rect(screen, (60, 60, 60), [887, 432, 236, 16])
            pygame.draw.rect(screen, (111, 210, 46), [887, 432, self.health_percent * 2.36, 16])

            # Dessine la barre d'énergie pendant le combat
            pygame.draw.rect(screen, (255, 255, 255), [886, 468, 238, 18])
            pygame.draw.rect(screen, (60, 60, 60), [887, 469, 236, 16])
            pygame.draw.rect(screen, (255, 255, 51), [887, 469, self.energy_percent * 2.36, 16])

            # Dessine la barre d'expérience pendant le combat
            pygame.draw.rect(screen, (255, 255, 255), [885, 502, 315, 12])
            pygame.draw.rect(screen, (60, 60, 60), [886, 503, 313, 10])
            pygame.draw.rect(screen, (89, 198, 242), [886, 503, self.xp_percent * 3.13, 10])

        if mode == "status":
            # Dessine la barre d'expérience sur la fenêtre de statut
            pygame.draw.rect(screen, (255, 255, 255), [641, 213, 352, 15])
            pygame.draw.rect(screen, (60, 60, 60), [642, 214, 350, 13])
            pygame.draw.rect(screen, (89, 198, 242), [642, 214, self.xp_percent * 3.50, 13])

    def level_update(self):
        """ Si l'expérience du joueur est supérieur à l'expérience requis, augmente le niveau du joueur """
        while self.xp >= self.max_xp:
            self.level_up = True
            self.xp -= self.max_xp
            self.level += 1
            self.max_xp = 25 * self.level * (self.level + 1)
            self.defence += int(self.level/2)

            if self.level in [2, 4, 6, 8]:
                self.rank_change += 1

            if self.role == "Designer":
                self.max_health += (self.level - 1) * 5
                self.max_energy += 5
                self.attack += (self.level - 1)

            elif self.role == "Développeur":
                self.max_health += (self.level - 1) * 4
                self.max_energy += 7
                self.attack += self.level

            elif self.role == "Philosophe":
                self.max_health += int((self.level - 1) * 4.5)
                self.max_energy += 6
                self.attack += (self.level - 1) + self.level%2

            self.health = self.max_health
            self.energy = self.max_energy

    def damage(self, amount):
        """ Réduit les points de vie du joueur de 'amount' """
        self.health -= amount
