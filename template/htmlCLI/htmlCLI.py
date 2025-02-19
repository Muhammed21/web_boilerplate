import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'template', 'tinyDSL')))
from tinyDSL import *

class HTMLCLI:
    
    def __init__(self):
        self.authorized_tags = ["h1", "h2", "h3", "h4", "h5", "h6", "div", "span", "img"]
        self.html = HTML("")
        self.count = 0
        self.tags = []
        self.project_country = ""
        self.argument = ""
        self.contentArg = ""
        self.body = Body("")
        self.css_rules = [] 
        
    def askTag(self):
        if self.count < 1:
            self.project_country = input("Langue par défaut:")
        
        self.html = HTML("", {"lang": f"{self.project_country}"})
        newTag = input("Quel tag voulez-vous ajouter:")
        if newTag not in self.authorized_tags:
            print("Tag non autorisé")
            return self.askTag()
        else: 
            content = self.askContent(newTag)
            self.argument = self.askArguments()
            self.contentArg = self.askArgContent()
            finished = self.isGood()
            
            self.addCssRule()
            
            if newTag == "h1":
                self.tags.append(H1(content, {f"{self.argument}": f"{self.contentArg}"}))
            if newTag == "h2":
                self.tags.append(H2(content, {f"{self.argument}": f"{self.contentArg}"}))
            if newTag == "h3":
                self.tags.append(H3(content, {f"{self.argument}": f"{self.contentArg}"}))
            if newTag == "h4":
                self.tags.append(H4(content, {f"{self.argument}": f"{self.contentArg}"}))
            if newTag == "h5":
                self.tags.append(H5(content, {f"{self.argument}": f"{self.contentArg}"}))
            if newTag == "h6":
                self.tags.append(H6(content, {f"{self.argument}": f"{self.contentArg}"}))
            if newTag == "div":
                self.tags.append(DIV(content, {f"{self.argument}": f"{self.contentArg}"}))
            if newTag == "span":
                self.tags.append(SPAN(content, {f"{self.argument}": f"{self.contentArg}"}))
            if newTag == "img":
                self.tags.append(IMG(content, {f"{self.argument}": f"{self.contentArg}"}))
                
            if 'oui' in finished:
                self.count = 1
                return self.askTag()
                
    def askContent(self, currentTag):
        content = input("Quel contenu pour le tag: ")
        return content
        
    def askArguments(self):
        arguments = input("Quel attribut pour le tag: ")
        return arguments
    
    def askArgContent(self):
        argContent = input("Quel contenu pour l'attribut du tag: ")
        return argContent
    
    def isGood(self):
        finish = input("Voulez-vous ajouter plus de balise (oui/non): ")
        return finish
    
    def addCssRule(self):
        if 'id' in self.argument:
            self.css_rules.append(f"\n#{self.contentArg} {{\n /* ... */ \n}}")
        elif 'class' in self.argument:
            self.css_rules.append(f"\n.{self.contentArg} {{\n /* ... */ \n}}")

    def writeInCss(self, name):
        with open(f"{name}/public/styles/style.css", "a", encoding='utf-8') as f:
            for rule in self.css_rules:
                f.write(rule)
            self.css_rules.clear() 
        
    def buildHTML(self, project_name):
        self.body.add(self.tags)
        self.html.add([
            HEAD("").add([
                META("", {"charset": "UTF-8"}), 
                META("", {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}), 
                TITLE("Mon site"),
                LINK("", {"rel": "stylesheet", "href": f"/{project_name}/public/styles/design_system.css"}),
                LINK("", {"rel": "stylesheet", "href": f"/{project_name}/public/styles/reset.css"}),
                LINK("", {"rel": "stylesheet", "href": f"/{project_name}/public/styles/style.css"})
            ]),
            self.body
        ])
        return self.html
