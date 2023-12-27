import Base
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import lazy_loader.lazy_loader as lz
from draftgeoutils.general import geomType as geomType
from draftgeoutils.geometry import findDistance as findDistance

NORM: Base.Vector
def pointInversion(circle, point):
    """Return the circle inversion of a point.

        It will return `None` if the given point is equal to the center
        of the circle.
    """
def polarInversion(circle, edge):
    """Return the inversion pole of a line. The edge is the polar.

        The nearest point on the line is inversed.

        http://mathworld.wolfram.com/InversionPole.html
    """
def circleInversion(circle, circle2):
    """Circle inversion of a circle, inverting the center point.

        Returns the new circle created from the inverted center of circle2.
    """
