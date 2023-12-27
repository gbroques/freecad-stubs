import DraftGeomUtils as DraftGeomUtils
import FreeCAD as App
import Part as Part
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_circle(radius, placement: Incomplete | None = ..., face: Incomplete | None = ..., startangle: Incomplete | None = ..., endangle: Incomplete | None = ..., support: Incomplete | None = ...):
    """make_circle(radius, [placement, face, startangle, endangle])
        or make_circle(edge,[face]):

        Creates a circle object with given parameters.

        Parameters
        ----------
        radius : the radius of the circle.

        placement :
            If placement is given, it is used.

        face : Bool
            If face is False, the circle is shown as a wireframe,
            otherwise as a face.

        startangle : start angle of the arc (in degrees)

        endangle : end angle of the arc (in degrees)
            if startangle and endangle are equal, a circle is created,
            if they are different an arc is created

        edge : edge.Curve must be a 'Part.Circle'
            the circle is created from the given edge

        support :
            TODO: Describe
    """
def makeCircle(radius, placement: Incomplete | None = ..., face: Incomplete | None = ..., startangle: Incomplete | None = ..., endangle: Incomplete | None = ..., support: Incomplete | None = ...):
    """make_circle(radius, [placement, face, startangle, endangle])
        or make_circle(edge,[face]):

        Creates a circle object with given parameters.

        Parameters
        ----------
        radius : the radius of the circle.

        placement :
            If placement is given, it is used.

        face : Bool
            If face is False, the circle is shown as a wireframe,
            otherwise as a face.

        startangle : start angle of the arc (in degrees)

        endangle : end angle of the arc (in degrees)
            if startangle and endangle are equal, a circle is created,
            if they are different an arc is created

        edge : edge.Curve must be a 'Part.Circle'
            the circle is created from the given edge

        support :
            TODO: Describe
    """
