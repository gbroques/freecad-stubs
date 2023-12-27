import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils

def offset(obj, delta, copy: bool = ..., bind: bool = ..., sym: bool = ..., occ: bool = ...):
    """offset(object,delta,[copymode],[bind])

        Offset the given wire by applying the given delta Vector to its first
        vertex.

        Parameters
        ----------
        obj :

        delta : Base.Vector or list of Base.Vector
            If offsetting a BSpline, the delta must not be a Vector but a list
            of Vectors, one for each node of the spline.

        copy : bool
            If copymode is True, another object is created, otherwise the same
            object gets offsetted.

        copy : bool
            If bind is True, and provided the wire is open, the original
            and the offset wires will be bound by their endpoints, forming a face.

        sym : bool
            if sym is True, bind must be true too, and the offset is made on both
            sides, the total width being the given delta length.
    """
