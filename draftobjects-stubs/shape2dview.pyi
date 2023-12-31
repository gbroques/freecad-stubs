import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import draftobjects.base
import draftutils.groups as groups
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from draftobjects.base import DraftObject as DraftObject

class Shape2DView(draftobjects.base.DraftObject):
    def __init__(self, obj) -> None: ...
    def setProperties(self, obj): ...
    def onDocumentRestored(self, obj): ...
    def getProjected(self, obj, shape, direction):
        """returns projected edges from a shape and a direction"""
    def cleanExcluded(self, obj, shapes):
        """removes any edge touching exclusion points"""
    def excludeNames(self, obj, objs): ...
    def execute(self, obj): ...
    def onChanged(self, obj, prop): ...

class _Shape2DView(draftobjects.base.DraftObject):
    def __init__(self, obj) -> None: ...
    def setProperties(self, obj): ...
    def onDocumentRestored(self, obj): ...
    def getProjected(self, obj, shape, direction):
        """returns projected edges from a shape and a direction"""
    def cleanExcluded(self, obj, shapes):
        """removes any edge touching exclusion points"""
    def excludeNames(self, obj, objs): ...
    def execute(self, obj): ...
    def onChanged(self, obj, prop): ...
