import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_point_array(base_object, point_object, extra: Incomplete | None = ..., use_link: bool = ...):
    """Make a Draft PointArray object.

        Create copies of a `base_object` at the points defined by
        a `point_object`.

        Parameters
        ----------
        base_object: Part::Feature or str
            Any of object that has a `Part::TopoShape` that can be duplicated.
            This means most 2D and 3D objects produced with any workbench.
            If it is a string, it must be the `Label` of that object.
            Since a label is not guaranteed to be unique in a document,
            it will use the first object found with this label.

        point_object: Part::Feature, Sketcher::SketchObject, Mesh::Feature,
                      Points::FeatureCustom or str
            The object must have vertices and/or points.

        extra: Base::Placement, Base::Vector3, or Base::Rotation, optional
            It defaults to `None`.
            If it is provided, it is an additional placement that is applied
            to each copy of the array.
            The input could be a full placement, just a vector indicating
            the additional translation, or just a rotation.

        Returns
        -------
        Part::FeaturePython
            A scripted object of type `'PointArray'`.
            Its `Shape` is a compound of the copies of the original object.

        None
            If there is a problem it will return `None`.
    """
def makePointArray(base, ptlst):
    """Create PointArray. DEPRECATED. Use 'make_point_array'."""
def reapply_diffuse_color(vobj): ...
