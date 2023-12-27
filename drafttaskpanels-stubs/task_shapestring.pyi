import Base
import Draft_rc as Draft_rc
import FreeCAD as App
import FreeCADGui as Gui
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import draftguitools.gui_tool_utils as gui_tool_utils

class ShapeStringTaskPanel:
    def __init__(self, point: Base.Vector = ..., size: int = ..., string: str = ..., font: str = ...) -> None: ...
    def fileSelect(self, fn):
        """Assign the selected file."""
    def resetPoint(self):
        """Reset the selected point."""
    def action(self, arg):
        """scene event handler"""
    def setPoint(self, point):
        """Assign the selected point."""
    def platWinDialog(self, flag):
        """Handle the type of dialog depending on the platform."""

class ShapeStringTaskPanelCmd(ShapeStringTaskPanel):
    def __init__(self, sourceCmd) -> None: ...
    def accept(self):
        """Execute when clicking the OK button."""
    def reject(self):
        """Run when clicking the Cancel button."""
    def createObject(self):
        """Create object in the current document."""

class ShapeStringTaskPanelEdit(ShapeStringTaskPanel):
    def __init__(self, vobj) -> None: ...
    def accept(self): ...
    def reject(self): ...
    def finish(self): ...
