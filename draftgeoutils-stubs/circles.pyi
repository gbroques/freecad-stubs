import Base
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import lazy_loader.lazy_loader as lz
from draftgeoutils.edges import findMidpoint as findMidpoint
from draftgeoutils.general import edg as edg, geomType as geomType, v1 as v1, vec as vec
from draftgeoutils.geometry import findDistance as findDistance, mirror as mirror
from draftgeoutils.intersections import angleBisection as angleBisection, findIntersection as findIntersection

NORM: Base.Vector
def findClosestCircle(point, circles):
    """Return the circle with closest center to a given point."""
def getCircleFromSpline(edge):
    """Return a circle-based edge from a bspline-based edge.

        Return None if the edge is not a BSplineCurve.
    """
def circlefrom1Line2Points(edge, p1, p2):
    """Return a list of circles created from an edge and two points.

        It calculates up to 2 possible centers.
    """
def circlefrom2Lines1Point(edge1, edge2, point):
    """Return a list of circles from two edges and one point."""
def circleFrom2LinesRadius(edge1, edge2, radius):
    """Return a list of circles from two edges and one radius.

        It calculates 4 centers.
    """
def circleFrom3LineTangents(edge1, edge2, edge3):
    """Return a list of circles from three edges.

        It calculates up to 6 possible centers.
    """
def circleFromPointLineRadius(point, edge, radius):
    """Return a list of circles from one point, one edge, and one radius.

        It calculates up to 2 possible centers.
    """
def circleFrom2PointsRadius(p1, p2, radius):
    """Return a list of circles from two points, and one radius.

        The two points must not be equal.

        It calculates up to 2 possible centers.
    """
def findHomotheticCenterOfCircles(circle1, circle2):
    """Calculate the homothetic centers from two circles.

        Return None if the objects are not circles, or if they are concentric.

        http://en.wikipedia.org/wiki/Homothetic_center
        http://mathworld.wolfram.com/HomotheticCenter.html
    """
def findRadicalAxis(circle1, circle2):
    """Calculate the radical axis of two circles.

        On the radical axis (also called power line) of two circles any
        tangents drawn from a point on the axis to both circles have
        the same length.

        http://en.wikipedia.org/wiki/Radical_axis
        http://mathworld.wolfram.com/RadicalLine.html

        See Also
        --------
        findRadicalCenter
    """
def findRadicalCenter(circle1, circle2, circle3):
    """Calculate the radical center of three circles.

        It is also called the power center.
        It is the intersection point of the three radical axes of the pairs
        of circles.

        http://en.wikipedia.org/wiki/Power_center_(geometry)
        http://mathworld.wolfram.com/RadicalCenter.html

        See Also
        --------
        findRadicalAxis
    """
