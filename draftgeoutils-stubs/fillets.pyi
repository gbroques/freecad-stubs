import FreeCAD as App
import Part as Part
import lazy_loader.lazy_loader as lz
from draftgeoutils.arcs import arcFrom2Pts as arcFrom2Pts
from draftgeoutils.general import precision as precision
from draftgeoutils.wires import isReallyClosed as isReallyClosed

def fillet(lEdges, r, chamfer: bool = ...):
    """Return a list of sorted edges describing a round corner.

        Author: Jacques-Antoine Gaudin
    """
def filletWire(aWire, r, chamfer: bool = ...):
    """Fillet each angle of a wire with r as radius.

        If chamfer is true, a `chamfer` is made instead, and `r` is the
        size of the chamfer.
    """
