import FreeCAD as App
import draftobjects.base
import draftutils.utils as utils
from draftobjects.base import DraftObject as DraftObject

class Circle(draftobjects.base.DraftObject):
    def __init__(self, obj) -> None: ...
    def execute(self, obj):
        """This method is run when the object is created or recomputed."""
    def onChanged(self, obj, prop): ...

class _Circle(draftobjects.base.DraftObject):
    def __init__(self, obj) -> None: ...
    def execute(self, obj):
        """This method is run when the object is created or recomputed."""
    def onChanged(self, obj, prop): ...
