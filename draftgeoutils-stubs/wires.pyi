import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import WorkingPlane as WorkingPlane
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete
from draftgeoutils.edges import findMidpoint as findMidpoint, isLine as isLine
from draftgeoutils.general import geomType as geomType, precision as precision, vec as vec
from draftgeoutils.geometry import get_normal as get_normal

def findWires(edgeslist):
    """Find wires in a list of edges."""
def findWiresOld2(edgeslist):
    """Find connected wires in the given list of edges."""
def findWiresOld(edges):
    """Return a list of lists containing edges that can be connected.

        Find connected edges in the list.
    """
def flattenWire(wire, origin: Incomplete | None = ..., normal: Incomplete | None = ...):
    """Force a wire to be flat on a plane defined by an origin and a normal.

        If origin or normal are None they are derived from the wire.
    """
def superWire(edgeslist, closed: bool = ...):
    """Force a wire between edges that don't have coincident endpoints.

        Forces a wire between edges that don't necessarily
        have coincident endpoints. If closed=True, the wire will always be closed.
    """
def isReallyClosed(wire): ...
def curvetowire(obj, steps):
    """Discretize the object and return a list of edges."""
def curvetosegment(curve, seglen):
    """Discretize the curve and return a list of edges."""
def rebaseWire(wire, vidx: int = ...):
    """Return a copy of the wire with the first vertex indicated by the index.

        Return a new wire which is a copy of the current wire,
        but where the first vertex is the vertex indicated by the given
        index vidx, starting from 1.
        0 will return an exact copy of the wire.
    """
def removeInterVertices(wire):
    """Remove middle vertices from a straight wire and return a new wire.

        Remove unneeded vertices, those that are in the middle of a straight line,
        from a wire, return a new wire.
    """
def cleanProjection(shape, tessellate: bool = ..., seglength: float = ...):
    """Return a compound of edges, optionally tessellate ellipses, splines
        and bezcurves.

        The function was formerly used to workaround bugs in the projection
        algorithm. These bugs have since been fixed. Now the function is only
        used when tessellation of ellipses, splines and bezcurves is required
        (DXF output and Draft_Shape2DView).
    """
def tessellateProjection(shape, seglen):
    """Return projection with BSplines and Ellipses broken into line segments.

        Useful for exporting projected views to DXF files.
    """
def get_placement_perpendicular_to_wire(wire):
    """Return the placement whose base is the wire's first vertex and it's z axis aligned to the wire's tangent."""
def get_extended_wire(wire, offset_start, offset_end):
    """Return a wire trimmed (negative offset) or extended (positive offset) at its first vertex, last vertex or both ends.

        get_extended_wire(wire, -100.0, 0.0) -> returns a copy of the wire with its first 100 mm removed
        get_extended_wire(wire, 0.0, 100.0) -> returns a copy of the wire extended by 100 mm after it's last vertex
    """
