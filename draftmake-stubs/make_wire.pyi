import DraftGeomUtils as DraftGeomUtils
import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_wire(pointslist, closed: bool = ..., placement: Incomplete | None = ..., face: Incomplete | None = ..., support: Incomplete | None = ..., bs2wire: bool = ...):
    """make_wire(pointslist, [closed], [placement])

        Creates a Wire object from the given list of vectors.  If face is
        true (and wire is closed), the wire will appear filled. Instead of
        a pointslist, you can also pass a Part Wire.

        Parameters
        ----------
        pointslist : [Base.Vector]
            List of points to create the polyline

        closed : bool
            If closed is True or first and last points are identical,
            the created polyline will be closed.

        placement : Base.Placement
            If a placement is given, it is used.

        face : Bool
            If face is False, the rectangle is shown as a wireframe,
            otherwise as a face.

        support :
            TODO: Describe

        bs2wire : bool
            TODO: Describe
    """
def makeWire(pointslist, closed: bool = ..., placement: Incomplete | None = ..., face: Incomplete | None = ..., support: Incomplete | None = ..., bs2wire: bool = ...):
    """make_wire(pointslist, [closed], [placement])

        Creates a Wire object from the given list of vectors.  If face is
        true (and wire is closed), the wire will appear filled. Instead of
        a pointslist, you can also pass a Part Wire.

        Parameters
        ----------
        pointslist : [Base.Vector]
            List of points to create the polyline

        closed : bool
            If closed is True or first and last points are identical,
            the created polyline will be closed.

        placement : Base.Placement
            If a placement is given, it is used.

        face : Bool
            If face is False, the rectangle is shown as a wireframe,
            otherwise as a face.

        support :
            TODO: Describe

        bs2wire : bool
            TODO: Describe
    """
