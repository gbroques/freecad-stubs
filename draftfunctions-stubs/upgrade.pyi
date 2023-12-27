import DraftGeomUtils as DraftGeomUtils
import FreeCAD as App
import Part as Part
import draftfunctions.draftify as ext_draftify
import draftfunctions.fuse as fuse
import draftmake.make_block as make_block
import draftmake.make_line as make_line
import draftmake.make_wire as make_wire
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete

_DEBUG: bool
def upgrade(objects, delete: bool = ..., force: Incomplete | None = ...):
    """Upgrade the given objects.

        This is a counterpart to `downgrade`.

        Parameters
        ----------
        objects: Part::Feature or list
            A single object to upgrade or a list
            containing various such objects.

        delete: bool, optional
            It defaults to `False`.
            If it is `True`, the old objects are deleted, and only the resulting
            object is kept.

        force: str, optional
            It defaults to `None`.
            Its value can be used to force a certain method of upgrading.
            It can be any of: `'makeCompound'`, `'closeGroupWires'`,
            `'makeSolid'`, `'closeWire'`, `'turnToParts'`, `'makeFusion'`,
            `'makeShell'`, `'makeFaces'`, `'draftify'`, `'joinFaces'`,
            `'makeSketchFace'`, `'makeWires'`.

        Returns
        -------
        tuple
            A tuple containing two lists, a list of new objects
            and a list of objects to be deleted.

        None
            If there is a problem it will return `None`.

        See Also
        --------
        downgrade
    """
