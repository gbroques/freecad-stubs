import FreeCAD as App
import FreeCADGui as Gui
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

conectedToolbars: list
def pythonToolbars():
    """Manage Python based toolbar in BIM workbench."""
def isConnected(i):
    """Connect toolbar to onSave function."""
def onRestore(active):
    """Restore current workbench toolbars position."""
def onSave():
    """Save current workbench toolbars position."""
def onWorkbenchActivated():
    """When workbench gets activated restore toolbar position."""
def onStart():
    """Start persistent toolbars."""
def onClose():
    """Remove system provided presets on FreeCAD close."""
