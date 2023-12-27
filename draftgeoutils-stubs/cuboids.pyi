import DraftVecUtils as DraftVecUtils
import FreeCAD as App
from draftgeoutils.general import geomType as geomType, precision as precision, vec as vec

def isCubic(shape):
    """Return True if the shape is a parallelepiped (cuboid).

        A parallelepiped of cube-like shape has 8 vertices, 6 faces, 12 edges,
        and all angles are 90 degrees between its edges.
    """
def getCubicDimensions(shape):
    """Return a list containing the placement, and dimensions of the shape.

        The dimensios are length, width and height of a the parallelepiped,
        rounded to the value indicated by `precision`.
        The placement point is the lowest corner of the shape.

        If it is not a parallelepiped (cuboid), return None.
    """
