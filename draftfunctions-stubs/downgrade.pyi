import FreeCAD as App
import draftfunctions.cut as cut
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def downgrade(objects, delete: bool = ..., force: Incomplete | None = ...):
    """Downgrade the given objects.

        This is a counterpart to `upgrade`.

        Parameters
        ----------
        objects: Part::Feature or list
            A single object to downgrade or a list
            containing various such objects.

        delete: bool, optional
            It defaults to `False`.
            If it is `True`, the old objects are deleted, and only the resulting
            object is kept.

        force: str, optional
            It defaults to `None`.
            Its value can be used to force a certain method of downgrading.
            It can be any of: `'explode'`, `'shapify'`, `'subtr'`, `'splitFaces'`,
            `'cut2'`, `'getWire'`, `'splitWires'`, or `'splitCompounds'`.

        Returns
        -------
        tuple
            A tuple containing two lists, a list of new objects
            and a list of objects to be deleted.

        None
            If there is a problem it will return `None`.

        See Also
        --------
        ugrade
    """
