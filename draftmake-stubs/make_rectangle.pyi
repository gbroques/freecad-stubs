import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_rectangle(length, height: int = ..., placement: Incomplete | None = ..., face: Incomplete | None = ..., support: Incomplete | None = ...):
    """make_rectangle(length, width, [placement], [face])

        Creates a Rectangle object with length in X direction and height in Y
        direction.

        Parameters
        ----------
        length, height : dimensions of the rectangle

        placement : Base.Placement
            If a placement is given, it is used.

        face : Bool
            If face is False, the rectangle is shown as a wireframe,
            otherwise as a face.

        Rectangles can also be constructed by giving them a list of four vertices
        as first argument: make_rectangle(list_of_vertices, face=...)
        but you are responsible to check yourself that these 4 vertices are ordered
        and actually form a rectangle, otherwise the result might be wrong. Placement
        is ignored when constructing a rectangle this way (face argument is kept).
    """
def makeRectangle(length, height: int = ..., placement: Incomplete | None = ..., face: Incomplete | None = ..., support: Incomplete | None = ...):
    """make_rectangle(length, width, [placement], [face])

        Creates a Rectangle object with length in X direction and height in Y
        direction.

        Parameters
        ----------
        length, height : dimensions of the rectangle

        placement : Base.Placement
            If a placement is given, it is used.

        face : Bool
            If face is False, the rectangle is shown as a wireframe,
            otherwise as a face.

        Rectangles can also be constructed by giving them a list of four vertices
        as first argument: make_rectangle(list_of_vertices, face=...)
        but you are responsible to check yourself that these 4 vertices are ordered
        and actually form a rectangle, otherwise the result might be wrong. Placement
        is ignored when constructing a rectangle this way (face argument is kept).
    """
