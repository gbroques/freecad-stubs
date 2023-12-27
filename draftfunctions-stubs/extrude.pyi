import FreeCAD as App
import draftutils.gui_utils as gui_utils

def extrude(obj, vector, solid: bool = ...):
    """extrude(object, vector, [solid])

        Create a Part::Extrusion object from a given object.

        Parameters
        ----------
        obj :

        vector : Base.Vector
            The extrusion direction and module.

        solid : bool
            TODO: describe.
    """
