import Draft as Draft
import FreeCAD as App
import Part as Part
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_arc_3points(points, placement: Incomplete | None = ..., face: bool = ..., support: Incomplete | None = ..., map_mode: str = ..., primitive: bool = ...):
    '''Draw a circular arc defined by three points in the circumference.

        Parameters
        ----------
        points: list of Base::Vector3
            A list that must be three points.

        placement: Base::Placement, optional
            It defaults to `None`.
            It is a placement, comprised of a `Base` (`Base::Vector3`),
            and a `Rotation` (`Base::Rotation`).
            If it exists it moves the center of the new object to the point
            indicated by `placement.Base`, while `placement.Rotation`
            is ignored so that the arc keeps the same orientation
            with which it was created.

            If both `support` and `placement` are given,
            `placement.Base` is used for the `AttachmentOffset.Base`,
            and again `placement.Rotation` is ignored.

        face: bool, optional
            It defaults to `False`.
            If it is `True` it will create a face in the closed arc.
            Otherwise only the circumference edge will be shown.

        support: App::PropertyLinkSubList, optional
            It defaults to `None`.
            It is a list containing tuples to define the attachment
            of the new object.

            A tuple in the list needs two elements;
            the first is an external object, and the second is another tuple
            with the names of sub-elements on that external object
            likes vertices or faces.
            ::
                support = [(obj, ("Face1"))]
                support = [(obj, ("Vertex1", "Vertex5", "Vertex8"))]

            This parameter sets the `Support` property but it only really affects
            the position of the new object when the `map_mode`
            is set to other than `\'Deactivated\'`.

        map_mode: str, optional
            It defaults to `\'Deactivated\'`.
            It defines the type of `\'MapMode\'` of the new object.
            This parameter only works when a `support` is also provided.

            Example: place the new object on a face or another object.
            ::
                support = [(obj, ("Face1"))]
                map_mode = \'FlatFace\'

            Example: place the new object on a plane created by three vertices
            of an object.
            ::
                support = [(obj, ("Vertex1", "Vertex5", "Vertex8"))]
                map_mode = \'ThreePointsPlane\'

        primitive: bool, optional
            It defaults to `False`. If it is `True`, it will create a Part
            primitive instead of a Draft object.
            In this case, `placement`, `face`, `support`, and `map_mode`
            are ignored.

        Returns
        -------
        Part::Part2DObject or Part::Feature
            The new arc object.
            Normally it returns a parametric Draft object (`Part::Part2DObject`).
            If `primitive` is `True`, it returns a basic `Part::Feature`.

        None
            Returns `None` if there is a problem and the object cannot be created.
    '''
