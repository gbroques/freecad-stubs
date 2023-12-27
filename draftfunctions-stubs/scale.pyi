import Base
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import draftfunctions.join as join
import draftmake.make_copy as make_copy
import draftmake.make_line as make_line
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils

def scale(objectslist, scale: Base.Vector = ..., center: Base.Vector = ..., copy: bool = ...):
    """scale(objects, scale, [center], copy)

        Scales the objects contained in objects (that can be a list of objects or
        an object) of the given  around given center.

        Parameters
        ----------
        objectlist : list

        scale : Base.Vector
            Scale factors defined by a given vector (in X, Y, Z directions).

        objectlist : Base.Vector
            Center of the scale operation.

        copy : bool
            If copy is True, the actual objects are not scaled, but copies
            are created instead.

        Return
        ----------
        The objects (or their copies) are returned.
    """
def scale_vertex(obj, vertex_index, scale, center):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def scaleVertex(obj, vertex_index, scale, center):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def scale_vector_from_center(vector, scale, center):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def scaleVectorFromCenter(vector, scale, center):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def scale_edge(obj, edge_index, scale, center):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def scaleEdge(obj, edge_index, scale, center):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def copy_scaled_edge(obj, edge_index, scale, center):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def copyScaledEdge(obj, edge_index, scale, center):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def copy_scaled_edges(arguments):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def copyScaledEdges(arguments):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
