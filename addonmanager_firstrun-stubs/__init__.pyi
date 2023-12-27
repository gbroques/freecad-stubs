import FreeCAD as FreeCAD
import FreeCADGui as FreeCADGui
import PySide.QtCore as QtCore
import PySide.QtWidgets as QtWidgets
import addonmanager_utilities as utils

class FirstRunDialog:
    def __init__(self) -> None: ...
    def exec(self) -> bool:
        """Display a first-run dialog if needed, and return True to indicate the Addon Manager
                should continue loading, or False if the user cancelled the dialog and wants to exit."""
