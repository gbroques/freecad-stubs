import Base
import FreeCAD as App
import draftmake.make_array as make_array
import draftutils.utils as utils

def make_polar_array(base_object, number: int = ..., angle: int = ..., center: Base.Vector = ..., use_link: bool = ...):
    """Create a polar array from the given object.

        Parameters
        ----------
        base_object: Part::Feature or str
            Any of object that has a `Part::TopoShape` that can be duplicated.
            This means most 2D and 3D objects produced with any workbench.
            If it is a string, it must be the `Label` of that object.
            Since a label is not guaranteed to be unique in a document,
            it will use the first object found with this label.

        number: int, optional
            It defaults to 5.
            The number of copies produced in the polar pattern.

        angle: float, optional
            It defaults to 360.
            The magnitude in degrees swept by the polar pattern.

        center: Base::Vector3, optional
            It defaults to the origin `App.Vector(0, 0, 0)`.
            The vector indicating the center of rotation of the array.

        use_link: bool, optional
            It defaults to `True`.
            If it is `True` the produced copies are not `Part::TopoShape` copies,
            but rather `App::Link` objects.
            The Links repeat the shape of the original `obj` exactly,
            and therefore the resulting array is more memory efficient.

            Also, when `use_link` is `True`, the `Fuse` property
            of the resulting array does not work; the array doesn't
            contain separate shapes, it only has the original shape repeated
            many times, so there is nothing to fuse together.

            If `use_link` is `False` the original shape is copied many times.
            In this case the `Fuse` property is able to fuse
            all copies into a single object, if they touch each other.

        Returns
        -------
        Part::FeaturePython
            A scripted object of type `'Array'`.
            Its `Shape` is a compound of the copies of the original object.

        None
            If there is a problem it will return `None`.

        See Also
        --------
        make_ortho_array, make_circular_array, make_path_array, make_point_array
    """
