import FreeCAD as App
import draftutils.utils as utils
from _typeshed import Incomplete

def heal(objlist: Incomplete | None = ..., delete: bool = ..., reparent: bool = ...):
    """heal([objlist],[delete],[reparent])

        Recreate Draft objects that are damaged, for example if created from an
        earlier version. If ran without arguments, all the objects in the document
        will be healed if they are damaged.

        Parameters
        ----------
        objlist : list

        delete : Base.Vector or list of Base.Vector
            If delete is True, the damaged objects are deleted (default).

        reparent : bool
            If reparent is True (default), new objects go at the very same place
            in the tree than their original.
    """
