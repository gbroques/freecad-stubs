import FreeCAD as App
import draftfunctions.join as join
import draftmake.make_copy as make_copy
import draftmake.make_line as make_line
import draftutils.groups as groups
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils

def move(objectslist, vector, copy: bool = ...):
    """move(objects,vector,[copy])

        Move the objects contained in objects (that can be an object or a
        list of objects) in the direction and distance indicated by the given
        vector.

        Parameters
        ----------
        objectslist : list

        vector : Base.Vector
            Delta Vector to move the clone from the original position.

        copy : bool
            If copy is True, the actual objects are not moved, but copies
            are created instead.

        Return
        ----------
        The objects (or their copies) are returned.
    """
def move_vertex(object, vertex_index, vector):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def moveVertex(object, vertex_index, vector):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def move_edge(object, edge_index, vector):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def moveEdge(object, edge_index, vector):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def copy_moved_edges(arguments):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def copyMovedEdges(arguments):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
def copy_moved_edge(object, edge_index, vector):
    """
    Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).
    """
