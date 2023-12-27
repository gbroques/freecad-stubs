import FreeCAD as App
import FreeCADGui as Gui
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import PySide2.QtCore
import PySide2.QtWidgets
import Tux_rc as Tux_rc
from _typeshed import Incomplete
from typing import ClassVar

p: ParameterGrp
pView: ParameterGrp
def translate(context, text):
    """convenience function for Qt 5 translator"""

class IndicatorButton(PySide2.QtWidgets.QPushButton):
    staticMetaObject: ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def changeEvent(self, event):
        """Change events."""
    def onChange(self, paramGrp, param): ...
def retranslateUi():
    """Retranslate navigation indicator on language change"""

indicator: IndicatorButton
def onCompact():
    """Enable or disable compact mode."""
def setCompact(action):
    """Set compact mode."""
def onTooltip():
    """Enable or disable verbose tooltips."""
def onOrbit():
    """Use turntable or trackball orbit style."""
def onOrbitShow():
    """Set turntable or trackball orbit style."""
def onMenu(action):
    """Set navigation style on selection."""
def setCurrent():
    """Set navigation style on start and on interval."""

t0: str
t1: str
t2: str
t3: str
t4: str
t5: str
t6: str
t7: str
t8: str
t9: str
t10: str
