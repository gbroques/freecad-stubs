import DraftGeomUtils as DraftGeomUtils
import FreeCAD as App
import Part as Part
import draftobjects.fillet as fillet
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
import draftviewproviders.view_fillet as view_fillet
import lazy_loader.lazy_loader as lz

def _print_obj_length(obj, edge, num: int = ...): ...
def _extract_edges(objs):
    """Extract the edges from the list of objects, Draft lines or Part.Edges.

        Parameters
        ----------
        objs: list of Draft Lines or Part.Edges
            The list of edges from which to create the fillet.
    """
def make_fillet(objs, radius: int = ..., chamfer: bool = ..., delete: bool = ...):
    """Create a fillet between two lines or Part.Edges.

        Parameters
        ----------
        objs: list
            List of two objects of type wire, or edges.

        radius: float, optional
            It defaults to 100. The curvature of the fillet.

        chamfer: bool, optional
            It defaults to `False`. If it is `True` it no longer produces
            a rounded fillet but a chamfer (straight edge)
            with the value of the `radius`.

        delete: bool, optional
            It defaults to `False`. If it is `True` it will delete
            the pair of objects that are used to create the fillet.
            Otherwise, the original objects will still be there.

        Returns
        -------
        Part::Part2DObjectPython
            The object of Proxy type `'Fillet'`.
            It returns `None` if it fails producing the object.
    """
