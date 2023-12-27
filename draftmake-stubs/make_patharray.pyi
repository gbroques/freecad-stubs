import Base
import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_path_array(base_object, path_object, count: int = ..., extra: Base.Vector = ..., subelements: Incomplete | None = ..., align: bool = ..., align_mode: str = ..., tan_vector: Base.Vector = ..., force_vertical: bool = ..., vertical_vector: Base.Vector = ..., start_offset: float = ..., end_offset: float = ..., use_link: bool = ...):
    """Make a Draft PathArray object.

        Distribute copies of a `base_object` along `path_object`
        or `subelements` from `path_object`.

        Parameters
        ----------
        base_object: Part::Feature or str
            Any of object that has a `Part::TopoShape` that can be duplicated.
            This means most 2D and 3D objects produced with any workbench.
            If it is a string, it must be the `Label` of that object.
            Since a label is not guaranteed to be unique in a document,
            it will use the first object found with this label.

        path_object: Part::Feature or str
            Path object like a polyline, B-Spline, or bezier curve that should
            contain edges.
            Just like `base_object` it can also be `Label`.

        count: int, float, optional
            It defaults to 4.
            Number of copies to create along the `path_object`.
            It must be at least 2.
            If a `float` is provided, it will be truncated by `int(count)`.

        extra: Base.Vector3, optional
            It defaults to `App.Vector(0, 0, 0)`.
            It translates each copy by the value of `extra`.
            This is useful to adjust for the difference between shape centre
            and shape reference point.

        subelements: list or tuple of str, optional
            It defaults to `None`.
            It should be a list of names of edges that must exist in `path_object`.
            Then the path array will be created along these edges only,
            and not the entire `path_object`.
            ::
                subelements = ['Edge1', 'Edge2']

            The edges must be contiguous, meaning that it is not allowed to
            input `'Edge1'` and `'Edge3'` if they do not touch each other.

            A single string value is also allowed.
            ::
                subelements = 'Edge1'

        align: bool, optional
            It defaults to `False`.
            If it is `True` it will align `base_object` to tangent, normal,
            or binormal to the `path_object`, depending on the value
            of `tan_vector`.

        align_mode: str, optional
            It defaults to `'Original'` which is the traditional alignment.
            It can also be `'Frenet'` or `'Tangent'`.

            - Original. It does not calculate curve normal.
              `X` is curve tangent, `Y` is normal parameter, Z is the cross
              product `X` x `Y`.
            - Frenet. It defines a local coordinate system along the path.
              `X` is tangent to curve, `Y` is curve normal, `Z` is curve binormal.
              If normal cannot be computed, for example, in a straight path,
              a default is used.
            - Tangent. It is similar to `'Original'` but includes a pre-rotation
              to align the base object's `X` to the value of `tan_vector`,
              then `X` follows curve tangent.

        tan_vector: Base::Vector3, optional
            It defaults to `App.Vector(1, 0, 0)` or the +X axis.
            It aligns the tangent of the path to this local unit vector
            of the object.

        force_vertical: Base::Vector3, optional
            It defaults to `False`.
            If it is `True`, the value of `vertical_vector`
            will be used when `align_mode` is `'Original'` or `'Tangent'`.

        vertical_vector: Base::Vector3, optional
            It defaults to `App.Vector(0, 0, 1)` or the +Z axis.
            It will force this vector to be the vertical direction
            when `force_vertical` is `True`.

        start_offset: float, optional
            It defaults to 0.0.
            It is the length from the start of the path to the first copy.

        end_offset: float, optional
            It defaults to 0.0.
            It is the length from the end of the path to the last copy.

        use_link: bool, optional
            It defaults to `True`, in which case the copies are `App::Link`
            elements. Otherwise, the copies are shape copies which makes
            the resulting array heavier.

        Returns
        -------
        Part::FeaturePython
            The scripted object of type `'PathArray'`.
            Its `Shape` is a compound of the copies of the original object.

        None
            If there is a problem it will return `None`.
    """
def makePathArray(baseobject, pathobject, count, xlate: Incomplete | None = ..., align: bool = ..., pathobjsubs: list = ..., use_link: bool = ...):
    """Create PathArray. DEPRECATED. Use 'make_path_array'."""
def make_path_twisted_array(base_object, path_object, count: int = ..., rot_factor: float = ..., use_link: bool = ...):
    """Create a Path twisted array."""
def reapply_diffuse_color(vobj): ...
