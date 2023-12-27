import FreeCAD as App
import FreeCADGui as Gui
import draftutils.gui_utils as gui_utils
from _typeshed import Incomplete

def make_point(X: int = ..., Y: int = ..., Z: int = ..., color: Incomplete | None = ..., name: str = ..., point_size: int = ...):
    """ make_point(x, y, z, [color(r, g, b), point_size]) or
            make_point(Vector, color(r, g, b), point_size])

        Creates a Draft Point in the current document.

        Parameters
        ----------
        X :
            float -> X coordinate of the point
            Base.Vector -> Ignore Y and Z coordinates and create the point
                from the vector.

        Y : float
            Y coordinate of the point

        Z : float
            Z coordinate of the point

        color : (R, G, B)
            Point color as RGB
            example to create a colored point:
            make_point(0, 0, 0, (1, 0, 0)) # color = red
            example to change the color, make sure values are floats:
            p1.ViewObject.PointColor = (0.0, 0.0, 1.0)
    """
def makePoint(X: int = ..., Y: int = ..., Z: int = ..., color: Incomplete | None = ..., name: str = ..., point_size: int = ...):
    """ make_point(x, y, z, [color(r, g, b), point_size]) or
            make_point(Vector, color(r, g, b), point_size])

        Creates a Draft Point in the current document.

        Parameters
        ----------
        X :
            float -> X coordinate of the point
            Base.Vector -> Ignore Y and Z coordinates and create the point
                from the vector.

        Y : float
            Y coordinate of the point

        Z : float
            Z coordinate of the point

        color : (R, G, B)
            Point color as RGB
            example to create a colored point:
            make_point(0, 0, 0, (1, 0, 0)) # color = red
            example to change the color, make sure values are floats:
            p1.ViewObject.PointColor = (0.0, 0.0, 1.0)
    """
