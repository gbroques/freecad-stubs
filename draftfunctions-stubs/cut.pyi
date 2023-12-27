import FreeCAD as App
import draftutils.gui_utils as gui_utils

def cut(object1, object2):
    """Return a cut object made from the difference of the 2 given objects.

        Parameters
        ----------
        object1: Part::Feature
            Any object with a `Part::TopoShape`.

        object2: Part::Feature
            Any object with a `Part::TopoShape`.

        Returns
        -------
        Part::Cut
            The resulting cut object.

        None
            If there is a problem and the new object can't be created.
    """
