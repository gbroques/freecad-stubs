import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_copy(obj, force: Incomplete | None = ..., reparent: bool = ..., simple_copy: bool = ...):
    """make_copy(object, [force], [reparent], [simple_copy])

        Make an exact copy of an object and return it.

        Parameters
        ----------
        obj :
            Object to copy.

        force :
            Obsolete, not used anymore.

        reparent :
            Group the new object in the same group of the old one.

        simple_copy :
            Create a simple copy of the object (a new non parametric
            Part::Feature with the same Shape as the given object).
    """
