import DraftGeomUtils as DraftGeomUtils
import FreeCAD as App
import Part as Part
import draftmake.make_arc_3points as make_arc_3points
import draftmake.make_bezcurve as make_bezcurve
import draftmake.make_block as make_block
import draftmake.make_bspline as make_bspline
import draftmake.make_circle as make_circle
import draftmake.make_wire as make_wire
import draftutils.gui_utils as gui_utils
import lazy_loader.lazy_loader as lz

def draftify(objectslist, makeblock: bool = ..., delete: bool = ...):
    """draftify(objectslist,[makeblock],[delete])

        Turn each object of the given list (objectslist can also be a single
        object) into a Draft parametric wire.

        TODO: support more objects

        Parameters
        ----------
        objectslist :

        makeblock : bool
            If makeblock is True, multiple objects will be grouped in a block.

        delete : bool
            If delete = False, old objects are not deleted
    """
def draftify_shape(shape): ...
