import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_array(base_object, arg1, arg2, arg3, arg4: Incomplete | None = ..., arg5: Incomplete | None = ..., arg6: Incomplete | None = ..., use_link: bool = ...):
    """Create a Draft Array of the given object.

        Rectangular array
        -----------------
        make_array(object, xvector, yvector, xnum, ynum)
        make_array(object, xvector, yvector, zvector, xnum, ynum, znum)

        xnum of iterations in the x direction
        at xvector distance between iterations, same for y direction
        with yvector and ynum, same for z direction with zvector and znum.

        Polar array
        -----------
        make_array(object, center, totalangle, totalnum) for polar array, or

        center is a vector, totalangle is the angle to cover (in degrees)
        and totalnum is the number of objects, including the original.

        Circular array
        --------------
        make_array(object, rdistance, tdistance, axis, center, ncircles, symmetry)

        In case of a circular array, rdistance is the distance of the
        circles, tdistance is the distance within circles, axis the rotation-axis,
        center the center of rotation, ncircles the number of circles
        and symmetry the number of symmetry-axis of the distribution.

        To Do
        -----
        The `Array` class currently handles three types of arrays,
        orthogonal, polar, and circular. In the future, probably they should be
        split in separate classes so that they are easier to manage.
    """
def makeArray(baseobject, arg1, arg2, arg3, arg4: Incomplete | None = ..., arg5: Incomplete | None = ..., arg6: Incomplete | None = ..., name: str = ..., use_link: bool = ...):
    """Create an Array. DEPRECATED. Use 'make_array'."""
def reapply_diffuse_color(vobj): ...
