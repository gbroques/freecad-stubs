import FreeCAD as App
import PySide.QtCore as QtCore
from _typeshed import Incomplete

def get_default_unit(dim):
    """Return default Unit of Measure for a dimension.

        It is based on the user preferences.
    """
def getDefaultUnit(dim):
    """Return default Unit of Measure for a dimension.

        It is based on the user preferences.
    """
def make_format_spec(decimals: int = ..., dim: str = ...):
    """Return a string format specifier with decimals for a dimension.

        It is based on the user preferences.
    """
def makeFormatSpec(decimals: int = ..., dim: str = ...):
    """Return a string format specifier with decimals for a dimension.

        It is based on the user preferences.
    """
def display_external(internal_value, decimals: Incomplete | None = ..., dim: str = ..., showUnit: bool = ..., unit: Incomplete | None = ...):
    """Return a converted value for display, according to the unit schema.

        Parameters
        ----------
        internal_value: float
            A value that will be transformed depending on the other parameters.

        decimals: float, optional
            It defaults ot `None`, in which case, the decimals are 2.

        dim: str, optional
            It defaults to `'Length'`. It can also be `'Angle'`.

        showUnit: bool, optional
            It defaults to `True`.
            If it is `False` it won't show the unit.

        unit: str, optional
            A unit string such as `'mm'`, `'cm'`, `'m'`, `'in'`, `'ft'`,
            in which to express the returned value.
    """
def displayExternal(internal_value, decimals: Incomplete | None = ..., dim: str = ..., showUnit: bool = ..., unit: Incomplete | None = ...):
    """Return a converted value for display, according to the unit schema.

        Parameters
        ----------
        internal_value: float
            A value that will be transformed depending on the other parameters.

        decimals: float, optional
            It defaults ot `None`, in which case, the decimals are 2.

        dim: str, optional
            It defaults to `'Length'`. It can also be `'Angle'`.

        showUnit: bool, optional
            It defaults to `True`.
            If it is `False` it won't show the unit.

        unit: str, optional
            A unit string such as `'mm'`, `'cm'`, `'m'`, `'in'`, `'ft'`,
            in which to express the returned value.
    """
