import FreeCAD as App
import FreeCADGui as Gui
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import draftutils.utils as utils

param: ParameterGrp

class ViewProviderDraftAnnotation:
    def __init__(self, vobj) -> None: ...
    def set_properties(self, vobj):
        """Set the properties only if they don't already exist."""
    def set_annotation_properties(self, vobj, properties):
        """Set annotation properties only if they don't already exist."""
    def set_text_properties(self, vobj, properties):
        """Set text properties only if they don't already exist."""
    def set_units_properties(self, vobj, properties): ...
    def set_graphics_properties(self, vobj, properties):
        """Set graphics properties only if they don't already exist."""
    def dumps(self):
        """Return a tuple of objects to save or None."""
    def loads(self, state):
        """Set the internal properties from the restored state."""
    def attach(self, vobj):
        """Set up the scene sub-graph of the view provider."""
    def updateData(self, obj, prop):
        """Execute when a property from the Proxy class is changed."""
    def getDisplayModes(self, vobj):
        """Return the display modes that this viewprovider supports."""
    def getDefaultDisplayMode(self):
        """Return the default display mode."""
    def setDisplayMode(self, mode):
        """Return the saved display mode."""
    def onChanged(self, vobj, prop):
        """Execute when a view property is changed."""
    def execute(self, vobj):
        """Execute when the object is created or recomputed."""
    def setEdit(self, vobj, mode):
        """Execute the code when entering the specific edit mode.

                See view_base.py.
        """
    def unsetEdit(self, vobj, mode):
        """Execute the code when leaving the specific edit mode.

                See view_base.py.
        """
    def doubleClicked(self, vobj): ...
    def setupContextMenu(self, vobj, menu): ...
    def edit(self): ...
    def getIcon(self):
        """Return the path to the icon used by the view provider."""
