import DraftGeomUtils as DraftGeomUtils
import FreeCAD as App
import draftobjects.base
from draftobjects.base import DraftObject as DraftObject

class Rectangle(draftobjects.base.DraftObject):
    def __init__(self, obj) -> None: ...
    def execute(self, obj):
        """This method is run when the object is created or recomputed."""
    def onChanged(self, obj, prop): ...

class _Rectangle(draftobjects.base.DraftObject):
    def __init__(self, obj) -> None: ...
    def execute(self, obj):
        """This method is run when the object is created or recomputed."""
    def onChanged(self, obj, prop): ...
