import Part as Part
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete
from draftgeoutils.edges import findMidpoint as findMidpoint, invert as invert, isLine as isLine
from draftgeoutils.general import geomType as geomType

def sortEdges(edges):
    """Sort edges. Deprecated. Use Part.__sortEdges__ instead."""
def sortEdgesOld(lEdges, aVertex: Incomplete | None = ...):
    """Sort edges. Deprecated. Use Part.__sortEdges__ instead."""
