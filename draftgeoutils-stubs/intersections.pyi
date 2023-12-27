import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import lazy_loader.lazy_loader as lz
from draftgeoutils.edges import findMidpoint as findMidpoint
from draftgeoutils.general import geomType as geomType, isPtOnEdge as isPtOnEdge, precision as precision, vec as vec

def findIntersection(edge1, edge2, infinite1: bool = ..., infinite2: bool = ..., ex1: bool = ..., ex2: bool = ..., dts: bool = ..., findAll: bool = ...):
    """Return a list containing the intersection points of 2 edges.

        You can also feed 4 points instead of `edge1` and `edge2`.
        If `dts` is used, `Shape.distToShape()` is used, which can be buggy.
    """
def wiresIntersect(wire1, wire2):
    """Return True if some of the edges of the wires are intersecting.

        Otherwise return `False`.
    """
def connect(edges, closed: bool = ...):
    """Connect the edges in the given list by their intersections."""
def angleBisection(edge1, edge2):
    """Return an edge that bisects the angle between the 2 straight edges."""
