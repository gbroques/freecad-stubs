import FreeCAD as App
import FreeCADGui as Gui
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils

def mirror(objlist, p1, p2):
    """Create a mirror object from the provided list and line.

        It creates a `Part::Mirroring` object from the given `objlist` using
        a plane that is defined by the two given points `p1` and `p2`,
        and either

        - the Draft working plane normal, or
        - the negative normal provided by the camera direction
          if the working plane normal does not exist and the graphical interface
          is available.

        If neither of these two is available, it uses as normal the +Z vector.

        Parameters
        ----------
        objlist: single object or a list of objects
            A single object or a list of objects.

        p1: Base::Vector3
            Point 1 of the mirror plane. It is also used as the `Placement.Base`
            of the resulting object.

        p2: Base::Vector3
            Point 1 of the mirror plane.

        Returns
        -------
        None
            If the operation fails.

        list
            List of `Part::Mirroring` objects, or a single one
            depending on the input `objlist`.

        To Do
        -----
        Implement a mirror tool specific to the workbench that does not
        just use `Part::Mirroring`. It should create a derived object,
        that is, it should work similar to `Draft.offset`.
    """
