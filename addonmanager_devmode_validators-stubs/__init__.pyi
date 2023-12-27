import PySide2.QtCore
import PySide2.QtGui
from typing import ClassVar

class NameValidator(PySide2.QtGui.QValidator):
    invalid: ClassVar[str] = ...
    staticMetaObject: ClassVar[PySide2.QtCore.QMetaObject] = ...
    def validate(self, value: str, _: int):
        """Check the value against the validator"""
    def fixup(self, value: str) -> str:
        """Remove invalid characters from value"""

class PythonIdentifierValidator(PySide2.QtGui.QValidator):
    staticMetaObject: ClassVar[PySide2.QtCore.QMetaObject] = ...
    def validate(self, value: str, _: int):
        """The function that does the validation."""

class SemVerValidator(PySide2.QtGui.QRegularExpressionValidator):
    semver_re: ClassVar[PySide2.QtCore.QRegularExpression] = ...
    staticMetaObject: ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self) -> None: ...
    @classmethod
    def check(cls, value: str) -> bool:
        """Returns true if value validates, and false if not"""

class CalVerValidator(PySide2.QtGui.QRegularExpressionValidator):
    calver_re: ClassVar[PySide2.QtCore.QRegularExpression] = ...
    staticMetaObject: ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self) -> None: ...
    @classmethod
    def check(cls, value: str) -> bool:
        """Returns true if value validates, and false if not"""

class VersionValidator(PySide2.QtGui.QValidator):
    staticMetaObject: ClassVar[PySide2.QtCore.QMetaObject] = ...
    def __init__(self) -> None: ...
    def validate(self, value: str, position: int):
        """Called for validation, returns a tuple of the validation state, the value, and the
                position."""
