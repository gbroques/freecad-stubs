import FreeCAD as App
import draftutils.gui_utils as gui_utils

def fuse(object1, object2):
    """fuse(oject1, object2)

        Returns an object made from the union of the 2 given objects.
        If the objects are coplanar, a special Draft Wire is used, otherwise we use
        a standard Part fuse.

    """
