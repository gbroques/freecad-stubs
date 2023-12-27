import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete
from draftgeoutils.edges import findMidpoint as findMidpoint
from draftgeoutils.general import geomType as geomType

def isClockwise(edge, ref: Incomplete | None = ...):
    """Return True if a circle-based edge has a clockwise direction."""
def isWideAngle(edge):
    """Return True if the given edge is an arc with angle > 180 degrees."""
def arcFrom2Pts(firstPt, lastPt, center, axis: Incomplete | None = ...):
    """Build an arc with center and 2 points, can be oriented with axis."""
def arcFromSpline(edge):
    """Turn given edge into a circular arc from three points.

        Takes its first point, midpoint and endpoint. It works best with bspline
        segments such as those from imported svg files. Use this only
        if you are sure your edge is really an arc.

        It returns None if there is a problem, including passing straight edges.
    """
