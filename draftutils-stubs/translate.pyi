import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
from _typeshed import Incomplete

Qtranslate: builtin_function_or_method
_encoding: None
def translate(context, text, comment: Incomplete | None = ...):
    """Translate the text using the Qt translate function.

        It wraps around `QtGui.QApplication.translate`,
        which is the same as `QtCore.QCoreApplication.translate`.

        Parameters
        ----------
        context: str
            In C++ it is typically a class name.
            But it can also be any other string to categorize the translation,
            for example, the name of a workbench, tool, or function
            that is being translated. Usually it will be the name
            of the workbench.

        text: str
            Text that will be translated. It could be a single word,
            a full sentence, paragraph, or multiple paragraphs with new lines.
            Usually the last endline character '\\n'
            that finishes the string doesn't need to be included
            for translation.

        Returns
        -------
        str
            A unicode string returned by `QtGui.QApplication.translate`.

        Unicode strings
        ---------------
        Reference: https://doc.qt.io/qtforpython/PySide2/QtCore

        In Qt5 the strings are always assumed unicode

        >>> QtCore.QCoreApplication.translate(context, text, None)
        >>> QtGui.QApplication.translate(context, text, None)
    """
