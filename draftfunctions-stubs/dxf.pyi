import DraftGeomUtils as DraftGeomUtils
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import WorkingPlane as WorkingPlane
import draftutils.utils as utils
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete

def _get_proj(vec, plane: Incomplete | None = ...):
    """Get a projection of the vector in the plane's u and v directions.

        TODO: check if the same function for SVG and DXF projection can be used
        so that this function is not just duplicated code.
        This function may also be present elsewhere, like `WorkingPlane`
        or `DraftGeomUtils`, so we should avoid code duplication.
    """
def get_dxf(obj, direction: Incomplete | None = ...):
    """Return a DXF entity from the given object.

        If direction is given, the object is projected in 2D.
    """
def getDXF(obj, direction: Incomplete | None = ...):
    """Return DXF string of the object. DEPRECATED. Use 'get_dxf'."""
