import Base
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import draftfunctions.join as join
import draftmake.make_copy as make_copy
import draftmake.make_line as make_line
import draftutils.groups as groups
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils

def rotate(objectslist, angle, center: Base.Vector = ..., axis: Base.Vector = ..., copy: bool = ...):
    """rotate(objects,angle,[center,axis,copy])

        Rotates the objects contained in objects (that can be a list of objects
        or an object) of the given angle (in degrees) around the center, using
        axis as a rotation axis.

        Parameters
        ----------
        objectslist : list

        angle : rotation angle (in degrees)

        center : Base.Vector

        axis : Base.Vector
            If axis is omitted, the rotation will be around the vertical Z axis.

        copy : bool
            If copy is True, the actual objects are not moved, but copies
            are created instead.

        Return
        ----------
        The objects (or their copies) are returned.
    """
def rotate_vertex(object, vertex_index, angle, center, axis):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def rotateVertex(object, vertex_index, angle, center, axis):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def rotate_vector_from_center(vector, angle, axis, center):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def rotateVectorFromCenter(vector, angle, axis, center):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def rotate_edge(object, edge_index, angle, center, axis):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def rotateEdge(object, edge_index, angle, center, axis):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def copy_rotated_edges(arguments):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def copyRotatedEdges(arguments):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def copy_rotated_edge(object, edge_index, angle, center, axis):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
