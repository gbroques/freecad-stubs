import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import FreeCADGui as Gui
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import draftgeoutils.wires as wires
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
import draftviewproviders.view_base
from draftviewproviders.view_base import ViewProviderDraft as ViewProviderDraft

class ViewProviderWire(draftviewproviders.view_base.ViewProviderDraft):
    def __init__(self, vobj) -> None: ...
    def _set_properties(self, vobj):
        """Set the properties of objects if they don't exist."""
    def attach(self, vobj): ...
    def updateData(self, obj, prop): ...
    def onChanged(self, vobj, prop): ...
    def claimChildren(self): ...
    def flatten(self): ...

class _ViewProviderWire(draftviewproviders.view_base.ViewProviderDraft):
    def __init__(self, vobj) -> None: ...
    def _set_properties(self, vobj):
        """Set the properties of objects if they don't exist."""
    def attach(self, vobj): ...
    def updateData(self, obj, prop): ...
    def onChanged(self, vobj, prop): ...
    def claimChildren(self): ...
    def flatten(self): ...
