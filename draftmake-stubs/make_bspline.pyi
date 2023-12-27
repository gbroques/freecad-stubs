import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_bspline(pointslist, closed: bool = ..., placement: Incomplete | None = ..., face: Incomplete | None = ..., support: Incomplete | None = ...):
    """make_bspline(pointslist, [closed], [placement])

        Creates a B-Spline object from the given list of vectors.

        Parameters
        ----------
        pointlist : [Base.Vector]
            List of points to create the polyline.
            Instead of a pointslist, you can also pass a Part Wire.
            TODO: Change the name so!

        closed : bool
            If closed is True or first and last points are identical,
            the created BSpline will be closed.

        placement : Base.Placement
            If a placement is given, it is used.

        face : Bool
            If face is False, the rectangle is shown as a wireframe,
            otherwise as a face.

        support :
            TODO: Describe
    """
def makeBSpline(pointslist, closed: bool = ..., placement: Incomplete | None = ..., face: Incomplete | None = ..., support: Incomplete | None = ...):
    """make_bspline(pointslist, [closed], [placement])

        Creates a B-Spline object from the given list of vectors.

        Parameters
        ----------
        pointlist : [Base.Vector]
            List of points to create the polyline.
            Instead of a pointslist, you can also pass a Part Wire.
            TODO: Change the name so!

        closed : bool
            If closed is True or first and last points are identical,
            the created BSpline will be closed.

        placement : Base.Placement
            If a placement is given, it is used.

        face : Bool
            If face is False, the rectangle is shown as a wireframe,
            otherwise as a face.

        support :
            TODO: Describe
    """
