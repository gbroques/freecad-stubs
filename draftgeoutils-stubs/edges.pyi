import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete
from draftgeoutils.general import geomType as geomType, vec as vec

def findEdge(anEdge, aList):
    """Return True if edge is found in list of edges."""
def orientEdge(edge, normal: Incomplete | None = ..., make_arc: bool = ...):
    """Re-orient the edge such that it is in the XY plane.

        Re-orients `edge` such that it is in the XY plane.
        If `normal` is passed, this is used as the basis for the rotation,
        otherwise the placement of `edge` is used.
    """
def isSameLine(e1, e2):
    """Return True if the 2 edges are lines and have the same points."""
def is_line(bspline):
    """Return True if the given BSpline curve is a straight line."""
def invert(shape):
    """Return an inverted copy of the edge or wire contained in the shape."""
def findMidpoint(edge):
    """Return the midpoint of an edge."""
def getTangent(edge, from_point: Incomplete | None = ...):
    """Return the tangent to an edge, including BSpline and circular arcs.

        If from_point is given, it is used to calculate the tangent,
        only useful for a circular arc.
    """
def get_referenced_edges(property_value):
    """Return the Edges referenced by the value of a App:PropertyLink, App::PropertyLinkList,
           App::PropertyLinkSub or App::PropertyLinkSubList property."""
def isLine(bspline):
    """Return True if the given BSpline curve is a straight line."""
