import Base
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import lazy_loader.lazy_loader as lz

PARAMGRP: ParameterGrp
NORM: Base.Vector
def precision():
    """Return the Draft precision setting."""
def vec(edge, use_orientation: bool = ...):
    """Return a vector from an edge or a Part.LineSegment.

        If use_orientation is True, it takes into account the edges orientation.
        If edge is not straight, you'll get strange results!
    """
def edg(p1, p2):
    """Return an edge from 2 vectors."""
def getVerts(shape):
    """Return a list containing vectors of each vertex of the shape."""
def v1(edge):
    """Return the first point of an edge."""
def isNull(something):
    """Return True if the given shape, vector, or placement is Null.

        If the vector is (0, 0, 0), it will return True.
    """
def isPtOnEdge(pt, edge):
    """Test if a point lies on an edge."""
def hasCurves(shape):
    """Check if the given shape has curves."""
def isAligned(edge, axis: str = ...):
    """Check if the given edge or line is aligned to the given axis.

        The axis can be 'x', 'y' or 'z'.
    """
def getQuad(face):
    """Return a list of 3 vectors if the face is a quad, ortherwise None.

        Returns
        -------
        basepoint, Xdir, Ydir
            If the face is a quad.

        None
            If the face is not a quad.
    """
def areColinear(e1, e2):
    """Return True if both edges are colinear."""
def hasOnlyWires(shape):
    """Return True if all edges are inside a wire."""
def geomType(edge):
    """Return the type of geometry this edge is based on."""
def isValidPath(shape):
    """Return True if the shape can be used as an extrusion path."""
def findClosest(base_point, point_list):
    """Find closest point in a list of points to the base point.

        Returns
        -------
        int
            An index from the list of points is returned.

        None
            If point_list is empty.
    """
def getBoundaryAngles(angle, alist):
    """Return the 2 closest angles that encompass the given angle."""
