"Fichier pour les téléporteurs"
import pygame

class Warp_north(pygame.sprite.Sprite):
    """ Définit les informations des téléporteurs Nord """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/map/warp.png")
        self.hitbox_x, self.hitbox_y = (50, 50)
        self.image = pygame.transform.scale(self.image, (self.hitbox_x, self.hitbox_y))
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = (x, y)

class Warp_south(pygame.sprite.Sprite):
    """ Définit les informations des téléporteurs Sud """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/map/warp.png")
        self.hitbox_x, self.hitbox_y = (50, 50)
        self.image = pygame.transform.scale(self.image, (self.hitbox_x, self.hitbox_y))
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = (x, y)

class Warp_east(pygame.sprite.Sprite):
    """ Définit les informations des téléporteurs Est """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/map/warp.png")
        self.hitbox_x, self.hitbox_y = (50, 50)
        self.image = pygame.transform.scale(self.image, (self.hitbox_x, self.hitbox_y))
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = (x, y)

class Warp_west(pygame.sprite.Sprite):
    """ Définit les informations des téléporteurs Ouest """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/map/warp.png")
        self.hitbox_x, self.hitbox_y = (50, 50)
        self.image = pygame.transform.scale(self.image, (self.hitbox_x, self.hitbox_y))
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = (x, y)

class Warp_north_west(pygame.sprite.Sprite):
    """ Définit les informations des téléporteurs Nord-Ouest """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/map/warp.png")
        self.hitbox_x, self.hitbox_y = (50, 50)
        self.image = pygame.transform.scale(self.image, (self.hitbox_x, self.hitbox_y))
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = (x, y)

class Warp_north_east(pygame.sprite.Sprite):
    """ Définit les informations des téléporteurs Nord-Est """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/map/warp.png")
        self.hitbox_x, self.hitbox_y = (50, 50)
        self.image = pygame.transform.scale(self.image, (self.hitbox_x, self.hitbox_y))
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = (x, y)

class Warp_south_west(pygame.sprite.Sprite):
    """ Définit les informations des téléporteurs Sud-Ouest """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/map/warp.png")
        self.hitbox_x, self.hitbox_y = (50, 50)
        self.image = pygame.transform.scale(self.image, (self.hitbox_x, self.hitbox_y))
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = (x, y)

class Warp_south_east(pygame.sprite.Sprite):
    """ Définit les informations des téléporteurs Sud-Est """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/map/warp.png")
        self.hitbox_x, self.hitbox_y = (50, 50)
        self.image = pygame.transform.scale(self.image, (self.hitbox_x, self.hitbox_y))
        self.rect = self.image.get_rect()
        self.rect.x , self.rect.y = (x, y)
