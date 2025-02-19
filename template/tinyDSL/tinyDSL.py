import os

class TAG:
    
    def __init__(self, type, content, attributes = None, isAutoClose=False):
        self.type = type
        self.content = content
        self.attributes = attributes
        self.isAutoClose = isAutoClose
        self.sub_tags = []
        
    def to_string(self, prettify=False):
        endStr = ""
        other_tag_str = ""
        attributes = ""
                    
        if prettify:
            endStr = "\n"

        for tag in self.sub_tags:
            other_tag_str += tag.to_string(prettify=prettify)

        if self.attributes:
            for key, value in self.attributes.items():
                attributes += f" {key}='{value}'"

        if self.isAutoClose:
            return f"<{self.type}{attributes}/>"

        if other_tag_str:
            return f"<{self.type}{attributes}>{self.content}{other_tag_str}</{self.type}>" + endStr

        return f"<{self.type}{attributes}>{self.content}</{self.type}>" + endStr

    
    
    
    def add(self, tags):
        self.sub_tags = tags
        return self
    
class A(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("a", content, attributes, isAutoClose)


class HTML(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("html", content, attributes, isAutoClose)
        
class HEAD(TAG):
    
    def __init__(self, content, attributes=None):
        super().__init__("head", content, attributes, isAutoClose=False)
        
class LINK(TAG):
    
    def __init__(self, content, attributes=None):
        super().__init__("link", content, attributes, isAutoClose=True)
        
class META(TAG):
    
    def __init__(self, content, attributes=None):
        super().__init__("meta", content, attributes, isAutoClose = True)
        
class TITLE(TAG):
    
    def __init__(self, content, attributes=None):
        super().__init__("title", content, attributes, isAutoClose=False)

class H1(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("h1", content, attributes, isAutoClose)

class H2(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("h2", content, attributes, isAutoClose)
        
class H3(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("h3", content, attributes, isAutoClose)
        
class H4(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("h4", content, attributes, isAutoClose)
        
class H5(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("h5", content, attributes, isAutoClose)
        
class H6(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("h6", content, attributes, isAutoClose)
        
class DIV(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("div", content, attributes, isAutoClose)
        
class SPAN(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("span", content, attributes, isAutoClose)
        
class IMG(TAG):
    
    def __init__(self, content, attributes=None):
        super().__init__("img", content, attributes, isAutoClose=True)

class Body(TAG):
    
    def __init__(self, content, attributes=None, isAutoClose=False):
        super().__init__("body", content, attributes, isAutoClose)


def buildHTMLFundation(country):
    html = HTML("", {"lang":f"{country}"}).add([
        Body("").add([
            H1("Title"),
            IMG("", {"src":"public/assets"}, isAutoClose=True),
            H2("Sub Title"),
            A("Click here", {"href":"http://www.google.com"})
        ])
    ])
    return html

def writeInHtmlTemplate(path, country):
    if os.path.exists(path):
        with open(path, "w", encoding='utf-8') as f:
            f.write(buildHTMLFundation(country).to_string(prettify=True))
            print("Write success")
    else:
        print("File doesn't exist!")

# writeInHtmlTemplate("template/template_html.txt", "fr")

# print(buildHTMLFundation("fr").to_string(prettify=True))