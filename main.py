# Classe File
import os
import sys
from template.tinyDSL.tinyDSL import *
from template.htmlCLI.htmlCLI import *
from template.projectTheme.project_theme import *

# Classe File
class File:
        
    def __init__(self, name, content = "", extension = ".txt"): # Définition d'un constructeur avec comme paramétre name (obligatoire), content et extension (les deux facultatif).
        print("Name", name) # Print(du nom)
        self.extensions = [".html", ".css", ".js", ".txt"] # Assignation d'un tableau à la variable extensions  
        self.name = name # Assignation du parametre name à la variable name
        self.content = content # Assignation du parametre content à la variable content
        if extension not in self.extensions: # Si extension n'est pas dans la variable extensions contenant le tableau
            raise ValueError(f"Extension {extension} is not valid, authorized extensions are {self.extensions}") # Alors tu génére une erreur
        self.extension = extension
    
    @staticmethod # Pour pouvoir écrire une méthode (func) static
    def fromFileName(file_name: str): # Définition d'un function fromFileName qui verifie si le fichier existe, si oui alors tu le lit et tu renvoie son nom, contenu et son extension 
        if "." not in file_name: # Si "." n'est pas dans file_name
            raise ValueError("The file name must contain an extension") # Alors tu génére une erreur
        name, extension = file_name.split(".")
        # if file file_name exists, we can get the content
        if os.path.exists(file_name):
            content = ""
            with open(file_name, "r") as file: # Ouvre le fichier file_name ,"r" pour read -> envoie le contenu dans le param file
                content = file.read() # Envoie le contenu dans la variable content
            return File(name, content, "."+extension) # Et renvoie File() avec ces params
        return File(name, "", "."+extension)
    
    def full_name(self) -> str: # Définition d'un function qui renvoie une chaine de caractere (name et extension)
        return self.name + self.extension
        
    def informations(self) -> str: # Définition d'un function qui renvoie une chaine de caractere (name, content et extension)
        return f"Name: {self.name}, Content: {self.content}, Extension: {self.extension}"

# Classe FileManager
class FileManager:

    def __init__(self):
        pass
    
    def create_file(self, file_name, content = "", extension = ".txt") -> File: # Définition d'une fonction qui créer un fichier avec un nom, contenu et extension dynamic
        
        myFile = File(file_name, content, extension) 
        
        with open(myFile.full_name(), "w") as file: # Il est censé ouvrire le fichier et écrire dedans
            file.write(content) # On utilise la méthode write pour écrire dans le fichier en question
            
        return File(file_name, content, extension)


    def delete_file(self, file:File) -> bool: # Définition d'une function qui supprime un fichier qui est transmis par le biais d'un parametre et qui renvoie un Bool
        print("Deleting file", file.full_name())
        if os.path.exists(file.full_name()): # On vérifie si le path (chemin) existe si oui on supprime le fichier et on retunr True
            os.remove(file.full_name())
            return True
        return False
        
    def delete_file_from_file_name(self, file_name:str) -> bool: # Cette function permet de supprimer un fichier par son nom
        file_to_delete = File.fromFileName(file_name)
        self.delete_file(file_to_delete)
    
    
    
    def update_file(self, file:File, content) -> bool: # Met à jour le fichier par le biais de son nom sous forme de chaine de caractere
        with open(file.full_name(), "a", encoding='utf-8') as f:
            f.write(content)
        return True
    
    def update_file_from_file_name(self, file_name: str, content) -> bool: # Met à jour le fichier par le biais de la classe File()
        file_to_update = File.fromFileName(file_name)
        return self.update_file(file_to_update, content)

class ProjectGenerator:
    
    def __init__(self): # Constructeur qui vas appeler la function readTemplate() et fileGenerator() si le type est valide sinon afficher une erreur
        self.project_folder_name = ""
        self.project_folder_type = ""
        self.questionner = HTMLCLI()
        self.createProjectWithCLI()
        
        if self.project_folder_type == "web":
            self.readTemplate()
            self.questionner.askTag()
            self.buildHTMLFundation()
            self.fileGenerator()
            self.questionner.writeInCss(self.project_folder_name)
        else:
            print("The project type is not valid!")
            
    def createProjectWithCLI(self):
        self.project_folder_type = input("Enter the project type: ")
        
        if (self.project_folder_type) != "web":
            print("The project type is not valid, valid type is web")
            sys.exit(0)
            
        self.project_folder_name = input("Enter the project name: ")
    
    def folderGenerator(self): # Méthode qui vas s'occuper de créer les dossiers necessaire si le type est valide sinon il affiche une erreur
        if (self.project_folder_type == "web"):
            os.mkdir(f"{self.project_folder_name}")
            os.mkdir(f"{self.project_folder_name}/public")
            os.mkdir(f"{self.project_folder_name}/public/styles")
            os.mkdir(f"{self.project_folder_name}/public/assets")
            os.mkdir(f"{self.project_folder_name}/public/assets/img")
            os.mkdir(f"{self.project_folder_name}/public/assets/svg")
            os.mkdir(f"{self.project_folder_name}/public/fonts")
            os.mkdir(f"{self.project_folder_name}/public/fonts/otf")
            os.mkdir(f"{self.project_folder_name}/public/fonts/ttf")
        else:
            print("The project type is not valid!")
            
    def readTemplate(self): # Méthode qui créer des variables (propriété) puis l
        self.html_template = ""
        self.reset_css = ""
        self.design_system_css = ""
        self.style_css = ""
        
        project_theme = LightDarkMode()
        
        with open('template/template_reset_css.txt') as f:
            self.reset_css = f.read()
        if "light" in project_theme.theme:
            with open('template/template_design_system_light_css.txt') as f:
                self.design_system_css = f.read()
        if "dark" in project_theme.theme:
            with open('template/template_design_system_dark_css.txt') as f:
                self.design_system_css = f.read()
        with open('template/template_style_css.txt') as f:
            self.style_css = f.read()
            
    def buildHTMLFundation(self):
        # html = HTML("", {"lang":f"{country}"}).add([
        #         Body("").add([
        #             H1("Title"),
        #             IMG("", {"src":"public/assets"}, isAutoClose=True),
        #             H2("Sub Title"),
        #             A("Click here", {"href":"http://www.google.com"})
        #         ])
        #     ])
        self.html_template = self.questionner.buildHTML(self.project_folder_name).to_string(prettify=True)
    
    def fileGenerator(self):
        self.folderGenerator()
        fileManager = FileManager()
        fileManager.create_file(f"{self.project_folder_name}/public/styles"+"/reset", f"{self.reset_css}", ".css")
        fileManager.create_file(f"{self.project_folder_name}/public/styles"+"/design_system", f"{self.design_system_css}", ".css")
        fileManager.create_file(f"{self.project_folder_name}/public/styles"+"/style", f"{self.style_css}", ".css")
        fileManager.create_file(f"{self.project_folder_name}"+"/index", f"{self.html_template}", ".html")

projectWeb = ProjectGenerator()
