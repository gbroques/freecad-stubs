import FreeCAD as FreeCAD
import FreeCADGui as FreeCADGui
import draftguitools.gui_base
import draftguitools.gui_base as gui_base

class Draft_Hatch(draftguitools.gui_base.GuiCommandSimplest):
    def GetResources(self): ...
    def Activated(self): ...

class Draft_Hatch_TaskPanel:
    def __init__(self, baseobj) -> None: ...
    def accept(self): ...
    def reject(self): ...
    def onFileChanged(self, filename): ...
    def getPatterns(self, filename):
        """returns a list of pattern names found in a PAT file"""