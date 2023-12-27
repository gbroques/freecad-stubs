import FreeCAD as FreeCAD
import FreeCADGui as FreeCADGui
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import StartPage.TranslationTexts as TranslationTexts
from _typeshed import Incomplete

has_am_macro: bool
iconbank: dict
tempfolder: str
defaulticon: None
def getThumbnailDir(): ...
def createThumbnailDir(): ...
def getSha1Hash(path, encode: str = ...): ...
def getUniquePNG(filename): ...
def useCachedPNG(image, project): ...
def gethexcolor(color):
    """returns a color hex value #000000"""
def isOpenableByFreeCAD(filename):
    """check if FreeCAD can handle this file type"""
def getInfo(filename):
    """returns available file information"""
def getDefaultIcon():
    """retrieves or creates a default file icon"""
def buildCard(filename, method, arg: Incomplete | None = ...):
    """builds an html <li> element representing a file.
        method is a script + a keyword, for ex. url.py?key="""
def handle():
    """builds the HTML code of the start page"""
def exportTestFile():
    """Allow to check if everything is Ok"""
def postStart():
    """executes needed operations after loading a file"""
def checkPostOpenStartPage():
    """on Start WB startup, check if we are loading a file and therefore need to close the StartPage"""
