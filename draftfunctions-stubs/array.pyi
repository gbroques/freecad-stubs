import FreeCAD as App
import draftfunctions.move as move
import draftfunctions.rotate as rotate
import draftutils.utils as utils
from _typeshed import Incomplete

def array(objectslist, arg1, arg2, arg3, arg4: Incomplete | None = ..., arg5: Incomplete | None = ..., arg6: Incomplete | None = ...):
    """
    This function creates an array of independent objects.
    Use make_array() to create a parametric array object.

    Creates an array of the given objects (that can be an object or a list
    of objects).

    In case of rectangular array, xnum of iterations in the x direction
    at xvector distance between iterations, and same for y and z directions
    with yvector and ynum and zvector and znum.

    In case of polar array, center is a vector, totalangle is the angle
    to cover (in degrees) and totalnum is the number of objects, including
    the original.

    Use
    ---
    array(objectslist, xvector, yvector, xnum, ynum) for rectangular array

    array(objectslist, xvector, yvector, zvector, xnum, ynum, znum) for rectangular array

    array(objectslist, center, totalangle, totalnum) for polar array
    """
def rectArray(objectslist, xvector, yvector, xnum, ynum): ...
def rectArray2(objectslist, xvector, yvector, zvector, xnum, ynum, znum): ...
def polarArray(objectslist, center, angle, num): ...
