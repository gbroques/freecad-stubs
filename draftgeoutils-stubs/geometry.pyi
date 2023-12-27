import Base
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import draftutils.gui_utils as gui_utils
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete
from draftgeoutils.general import geomType as geomType, vec as vec

def findPerpendicular(point, edgeslist, force: Incomplete | None = ...):
    """Find the perpendicular distance between a point and a list of edges.

        If force is specified, only the edge[force] will be considered,
        and it will be considered infinite.

        Returns
        -------
        [vector_from_point_to_closest_edge, edge_index]
            The vector and the index in the list.

        None
            If no perpendicular vector could be found.
    """
def findDistance(point, edge, strict: bool = ...):
    """Return a vector from the point to its closest point on the edge.

        If `strict` is `True`, the vector will be returned
        only if its endpoint lies on the `edge`.
        Edge can also be a list of 2 points.
    """
def get_spline_normal(edge, tol: int = ...):
    """Find the normal of a BSpline edge."""
def get_normal(shape, tol: int = ...):
    """Find the normal of a shape or list of points, if possible."""
def getRotation(v1, v2: Base.Vector = ...):
    """Get the rotation Quaternion between 2 vectors."""
def is_planar(shape, tol: int = ...):
    """Return True if the given shape or list of points is planar."""
def is_straight_line(shape, tol: int = ...):
    """Return True if shape is a straight line.
        function used in other methods because Part.Shape.findPlane assign a
        plane and normal to straight wires creating privileged directions
        and to deal with straight wires with overlapped edges."""
def are_coplanar(shape_a, shape_b, tol: int = ...):
    """Return True if exist a plane containing both shapes."""
def get_spline_surface_normal(shape, tol: int = ...):
    """Check if shape formed by BSpline surfaces is planar and get normal.
        If shape is not planar return None."""
def find_plane(shape, tol: int = ...):
    """Find the plane containing the shape if possible.
        Use this function as a workaround due Part.Shape.findPlane
        fail to find plane on BSpline surfaces."""
def calculatePlacement(shape):
    """Return a placement located in the center of gravity of the shape.

        If the given shape is planar, return a placement located at the center
        of gravity of the shape, and oriented towards the shape's normal.
        Otherwise, it returns a null placement.
    """
def mirror(point, edge):
    """Find mirror point relative to an edge."""
def getSplineNormal(edge, tol: int = ...):
    """Find the normal of a BSpline edge."""
def getNormal(shape, tol: int = ...):
    """Find the normal of a shape or list of points, if possible."""
def isPlanar(shape, tol: int = ...):
    """Return True if the given shape or list of points is planar."""
