import DraftGeomUtils as DraftGeomUtils
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_sketch(objects_list, autoconstraints: bool = ..., addTo: Incomplete | None = ..., delete: bool = ..., name: str = ..., radiusPrecision: int = ..., tol: float = ...):
    """make_sketch(objects_list, [autoconstraints], [addTo], [delete],
                       [name], [radiusPrecision], [tol])

        Makes a Sketch objects_list with the given Draft objects.

        Parameters
        ----------
        objects_list: can be single or list of objects of Draft type objects,
            Part::Feature, Part.Shape, or mix of them.

        autoconstraints(False): if True, constraints will be automatically added to
            wire nodes, rectangles and circles.

        addTo(None) : if set to an existing sketch, geometry will be added to it
            instead of creating a new one.

        delete(False): if True, the original object will be deleted.
            If set to a string 'all' the object and all its linked object will be
            deleted.

        name('Sketch'): the name for the new sketch object.

        radiusPrecision(-1): If <0, disable radius constraint. If =0, add individual
            radius constraint. If >0, the radius will be rounded according to this
            precision, and 'Equal' constraint will be added to curve with equal
            radius within precision.

        tol(1e-3): Tolerance used to check if the shapes are planar and coplanar.
            Consider change to tol=-1 for a more accurate analysis.
    """
def makeSketch(objects_list, autoconstraints: bool = ..., addTo: Incomplete | None = ..., delete: bool = ..., name: str = ..., radiusPrecision: int = ..., tol: float = ...):
    """make_sketch(objects_list, [autoconstraints], [addTo], [delete],
                       [name], [radiusPrecision], [tol])

        Makes a Sketch objects_list with the given Draft objects.

        Parameters
        ----------
        objects_list: can be single or list of objects of Draft type objects,
            Part::Feature, Part.Shape, or mix of them.

        autoconstraints(False): if True, constraints will be automatically added to
            wire nodes, rectangles and circles.

        addTo(None) : if set to an existing sketch, geometry will be added to it
            instead of creating a new one.

        delete(False): if True, the original object will be deleted.
            If set to a string 'all' the object and all its linked object will be
            deleted.

        name('Sketch'): the name for the new sketch object.

        radiusPrecision(-1): If <0, disable radius constraint. If =0, add individual
            radius constraint. If >0, the radius will be rounded according to this
            precision, and 'Equal' constraint will be added to curve with equal
            radius within precision.

        tol(1e-3): Tolerance used to check if the shapes are planar and coplanar.
            Consider change to tol=-1 for a more accurate analysis.
    """
