import sys

class LightDarkMode:
    def __init__(self):
        self.legal_theme = ["dark", "light"]
        self.theme = self.askTheme()  # Appeler la méthode pour obtenir le thème sélectionné
        if self.theme not in self.legal_theme:  # Vérification du thème valide
            print(f"Theme invalide, les thèmes valides sont : {self.legal_theme}")
            sys.exit(0)
        
    def askTheme(self):
        # Demander à l'utilisateur de choisir un thème
        theme = input("Quel thème pour votre site (light/dark) : ")
        return theme
        
# lightDarkMode = LightDarkMode() 
