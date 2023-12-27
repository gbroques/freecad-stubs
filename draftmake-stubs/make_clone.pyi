import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_clone(obj, delta: Incomplete | None = ..., forcedraft: bool = ...):
    """clone(obj,[delta,forcedraft])

        Makes a clone of the given object(s).
        The clone is an exact, linked copy of the given object. If the original
        object changes, the final object changes too.

        Parameters
        ----------
        obj :

        delta : Base.Vector
            Delta Vector to move the clone from the original position.

        forcedraft : bool
            If forcedraft is True, the resulting object is a Draft clone
            even if the input object is an Arch object.

    """
def reapply_diffuse_color(vobj): ...
def clone(obj, delta: Incomplete | None = ..., forcedraft: bool = ...):
    """clone(obj,[delta,forcedraft])

        Makes a clone of the given object(s).
        The clone is an exact, linked copy of the given object. If the original
        object changes, the final object changes too.

        Parameters
        ----------
        obj :

        delta : Base.Vector
            Delta Vector to move the clone from the original position.

        forcedraft : bool
            If forcedraft is True, the resulting object is a Draft clone
            even if the input object is an Arch object.

    """
