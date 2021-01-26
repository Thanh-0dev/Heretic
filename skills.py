"Fichier pour les attaques spéciales"
from random import randint

class Skills():
    """ Définit les attaques spéciales """
    def __init__(self, game):
        self.game = game
        self.skills = {
            "?" : {"cost" : 0, "damage" : 0},
            "??" : {"cost" : 0, "damage" : 0},
            "???" : {"cost" : 0, "damage" : 0},
            "????" : {"cost" : 0, "damage" : 0}
        }

        self.skills_Designer = {
            # Attaques spéciales du designer
            "Wireframe d'épée" : {"cost" : 5, "Atk" : 5 * self.game.player.rank, "desc" : "Design le wireframe d'une épée et s'en équipe jusqu'à la fin du combat."},
            "Prototype de bouclier" : {"cost" : 15, "Def" : 3 * self.game.player.rank, "desc" : "Design un prototype de bouclier et s'en équipe jusqu'à la fin du combat."},
            "Design enemie-centric" : {"cost" : 25, "damage" : 1.3, "desc" : "Décèle les faiblesses de l'ennemi pour l'immobiliser pendant ce tour."},
            "Make the logo bigger!" : {"cost" : 50, "damage" : (self.game.player.health - 1)//30, "desc" : "Sacrifie l'égo du designer pour arrêter les feedbacks l'ennemi."}
        }

        self.skills_Développeur = {
            # Attaques spéciales du développeur
            "Etreinte du Python" : {"cost" : 5, "damage" : 1.8, "desc" : "Fait suffoquer l'ennemi avec un programme codé avec Python."},
            "Balise bombe HTML" : {"cost" : 15, "damage" : randint(15, 25)/10, "desc" : "Lance aléatoirement 1 à 3 balises HTML qui explosent sur l'ennemi."},
            "Restructuration CSS" : {"cost" : 25, "damage" : 1.5, "desc" : "Restructure l'ennemi avec du CSS, l'empêche d'attaquer pendant ce tour."},
            "Débuggage" : {"cost" : self.game.player.energy, "damage" : (self.game.player.energy)//30, "desc" : "Utilise toute l'énergie du joueur pour débugger le code sur l'ennemi."}
        }

        self.skills_Philosophe = {
            # Attaques spéciales du philosophe
            "Projet Voltaire" : {"cost" : 5, "damage" : 1.8, "desc" : "Donne mal au crâne à l'ennemi en lui faisant faire le projet Voltaire."},
            "Lance-lettres" : {"cost" : 15, "damage" : randint(10, 30)/10, "desc" : "Arrache aléatoirement 1 à 5 lettres d'un livre et les lance sur l'ennemi."},
            "Question philosophique" : {"cost" : 25, "damage" : 1.5, "desc" : "Pose une question philosophique qui fait réfléchir l'ennemi pendant ce tour."},
            "Folie de Freud" : {"cost" : 50, "damage" : (self.game.player.max_health - self.game.player.health)//35, "desc" : "Reproduit la folie de Freud, le joueur se déchaine sur l'ennemi."}
        }

    def skills_update(self):
        """ Permet d'utiliser les skills de la classe chosie lorsque le rang est atteint """

        if self.game.player.role == "Designer":
            self.skills_Designer = {
            # Attaques spéciales du designer
            "Wireframe d'épée" : {"cost" : 5, "Atk" : 5 * self.game.player.rank, "desc" : "Design le wireframe d'une épée et s'en équipe jusqu'à la fin du combat."},
            "Prototype de bouclier" : {"cost" : 15, "Def" : 3 * self.game.player.rank, "desc" : "Design un prototype de bouclier et s'en équipe jusqu'à la fin du combat."},
            "Design enemie-centric" : {"cost" : 25, "damage" : 1.3, "desc" : "Décèle les faiblesses de l'ennemi pour l'immobiliser pendant ce tour."},
            "Make the logo bigger!" : {"cost" : 50, "damage" : (self.game.player.health - 1)//30, "desc" : "Sacrifie l'égo du designer pour arrêter les feedbacks l'ennemi."}
            }
            if self.game.player.rank > 1:
                self.change_skill("Wireframe d'épée", self.skills_Designer)
            else:
                self.change_skill("?", self.skills)

            if self.game.player.rank > 2:
                self.change_skill("Prototype de bouclier", self.skills_Designer)
            else:
                self.change_skill("??", self.skills)

            if self.game.player.rank > 3:
                self.change_skill("Design enemie-centric", self.skills_Designer)
            else:
                self.change_skill("???", self.skills)

            if self.game.player.rank > 4:
                self.change_skill("Make the logo bigger!", self.skills_Designer)
            else:
                self.change_skill("????", self.skills)

        elif self.game.player.role == "Développeur":
            self.skills_Développeur = {
            # Attaques spéciales du développeur
            "Etreinte du Python" : {"cost" : 5, "damage" : 1.8, "desc" : "Fait suffoquer l'ennemi avec un programme codé avec Python."},
            "Balise bombe HTML" : {"cost" : 15, "damage" : randint(15, 25)/10, "desc" : "Lance aléatoirement 1 à 3 balises HTML qui explosent sur l'ennemi."},
            "Restructuration CSS" : {"cost" : 25, "damage" : 1.5, "desc" : "Restructure l'ennemi avec du CSS, l'empêche d'attaquer pendant ce tour."},
            "Débuggage" : {"cost" : self.game.player.energy, "damage" : (self.game.player.energy)//30, "desc" : "Utilise toute l'énergie du joueur pour débugger le code sur l'ennemi."}
            }
            if self.game.player.rank > 1:
                self.change_skill("Etreinte du Python", self.skills_Développeur)
            else:
                self.change_skill("?", self.skills)

            if self.game.player.rank > 2:
                self.change_skill("Balise bombe HTML", self.skills_Développeur)
            else:
                self.change_skill("??", self.skills)

            if self.game.player.rank > 3:
                self.change_skill("Restructuration CSS", self.skills_Développeur)
            else:
                self.change_skill("???", self.skills)

            if self.game.player.rank > 4:
                self.change_skill("Débuggage", self.skills_Développeur)
            else:
                self.change_skill("????", self.skills)

        elif self.game.player.role == "Philosophe":
            self.skills_Philosophe = {
            # Attaques spéciales du philosophe
            "Projet Voltaire" : {"cost" : 5, "damage" : 1.8, "desc" : "Donne mal au crâne à l'ennemi en lui faisant faire le projet Voltaire."},
            "Lance-lettres" : {"cost" : 15, "damage" : randint(10, 30)/10, "desc" : "Arrache aléatoirement 1 à 5 lettres d'un livre et les lance sur l'ennemi."},
            "Question philosophique" : {"cost" : 25, "damage" : 1.5, "desc" : "Pose une question philosophique qui fait réfléchir l'ennemi pendant ce tour."},
            "Folie de Freud" : {"cost" : 50, "damage" : (self.game.player.max_health - self.game.player.health)//20, "desc" : "Reproduit la folie de Freud, le joueur se déchaine sur l'ennemi."}
            }
            if self.game.player.rank > 1:
                self.change_skill("Projet Voltaire", self.skills_Philosophe)
            else:
                self.change_skill("?", self.skills)

            if self.game.player.rank > 2:
                self.change_skill("Lance-lettres", self.skills_Philosophe)
            else:
                self.change_skill("??", self.skills)

            if self.game.player.rank > 3:
                self.change_skill("Question philosophique", self.skills_Philosophe)
            else:
                self.change_skill("???", self.skills)

            if self.game.player.rank > 4:
                self.change_skill("Folie de Freud", self.skills_Philosophe)

            else:
                self.change_skill("????", self.skills)

    def change_skill(self, skill_name, skill_role):
        """ Change le nom et les informations de l'attaque spéciale """
        loop = 0
        # Change le nom de l'attaque spéciale
        self.skills[skill_name] = self.skills.pop(list(self.skills)[0])

        # Remet les skills dans l'ordre
        while loop < 4:
            skill = list(self.skills)[0]
            self.skills["Skill"] = self.skills.pop(skill)
            self.skills[skill] = self.skills.pop("Skill")
            loop += 1

        # Change les informations de l'attaque spéciale
        self.skills[skill] = skill_role[skill_name]

    def weapons(self):
        """ Met à jour les armes dans les mains """
        if self.game.player.role == "Designer":

            if self.game.player.shield:
                self.game.player.shield = False

            if self.game.player.rank > 1:
                self.game.player.weapon = "une tablette graphique"

            else:
                self.game.player.weapon = "ses poings"

        elif self.game.player.role == "Développeur":
            if self.game.player.rank > 1:
                self.game.player.weapon = "un macbook pro"

        elif self.game.player.role == "Philosophe":
            if self.game.player.rank > 1:
                self.game.player.weapon = "un livre"
