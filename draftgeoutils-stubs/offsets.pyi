import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete
from draftgeoutils.general import geomType as geomType, vec as vec
from draftgeoutils.geometry import get_normal as get_normal
from draftgeoutils.intersections import connect as connect, wiresIntersect as wiresIntersect
from draftgeoutils.wires import isReallyClosed as isReallyClosed

def pocket2d(shape, offset):
    """Return a list of wires obtained from offsetting wires from the shape.

        Return a list of wires obtained from offsetting the wires
        from the given shape by the given offset, and intersection if needed.
    """
def offset(edge, vector, trim: bool = ...):
    """Return a copy of the edge at a certain vector offset.

        If the edge is an arc, the vector will be added at its first point
        and a complete circle will be returned.

        None if there is a problem.
    """
def offsetWire(wire, dvec, bind: bool = ..., occ: bool = ..., widthList: Incomplete | None = ..., offsetMode: Incomplete | None = ..., alignList: list = ..., normal: Incomplete | None = ..., basewireOffset: int = ...):
    '''Offset the wire along the given vector.

        Parameters
        ----------
        wire as a sorted list of edges (the list is used directly), or as a
        wire or a face (Draft Wire with MakeFace True or False supported).

        The vector will be applied at the first vertex of the wire. If bind
        is True (and the shape is open), the original wire and the offsetted one
        are bound by 2 edges, forming a face.

        If widthList is provided (values only, not lengths - i.e. no unit),
        each value will be used to offset each corresponding edge in the wire.

        The 1st value overrides \'dvec\' for 1st segment of wire;
        if a value is zero, value of \'widthList[0]\' will follow;
        if widthList[0]\' == 0, but dvec still provided, dvec will be followed

        offsetMode="BasewireMode" or None

        If alignList is provided,
        each value will be used to offset each corresponding edge
        in the wire with corresponding index.

        \'basewireOffset\' corresponds to \'offset\' in ArchWall which offset
        the basewire before creating the wall outline

        OffsetWire() is now aware of width and align per edge
        Primarily for use with ArchWall based on Sketch object

        To Do
        -----
        `dvec` vector to offset is now derived (and can be ignored)
        in this function if widthList and alignList are provided
        - \'dvec\' to be obsolete in future?
    '''
