import Base
import FreeCAD as App
import draftutils.gui_utils as gui_utils
import draftutils.utils as utils
from _typeshed import Incomplete

def make_dimension(p1, p2, p3: Incomplete | None = ..., p4: Incomplete | None = ...):
    '''Create one of three types of dimension objects.

        In all dimensions the p3 parameter defines a point through which
        the dimension line will go through.

        The current line width and color will be used.

        Linear dimension
        ----------------
        - (p1, p2, p3): a simple linear dimension from p1 to p2

        - (object, i1, i2, p3): creates a linked dimension to the provided
          object (edge), measuring the distance between its vertices
          indexed i1 and i2

        Circular dimension
        ------------------
        - (arc, i1, mode, p3): creates a linked dimension to the given arc
          object, i1 is the index of the arc edge that will be measured;
          mode is either "radius" or "diameter".
    '''
def makeDimension(p1, p2, p3: Incomplete | None = ..., p4: Incomplete | None = ...):
    """Create a dimension. DEPRECATED. Use 'make_dimension'."""
def make_linear_dimension(p1, p2, dim_line: Incomplete | None = ...):
    """Create a free linear dimension from two main points.

        Parameters
        ----------
        p1: Base::Vector3
            First point of the measurement.

        p2: Base::Vector3
            Second point of the measurement.

        dim_line: Base::Vector3, optional
            It defaults to `None`.
            This is a point through which the extension of the dimension line
            will pass.
            This point controls how close or how far the dimension line is
            positioned from the measured segment that goes from `p1` to `p2`.

            If it is `None`, this point will be calculated from the intermediate
            distance between `p1` and `p2`.

        Returns
        -------
        App::FeaturePython
            A scripted object of type `'LinearDimension'`.
            This object does not have a `Shape` attribute, as the text and lines
            are created on screen by Coin (pivy).

        None
            If there is a problem it will return `None`.
    """
def make_linear_dimension_obj(edge_object, i1: int = ..., i2: int = ..., dim_line: Incomplete | None = ...):
    """Create a linear dimension from an object.

        Parameters
        ----------
        edge_object: Part::Feature
            The object which has an edge which will be measured.
            It must have a `Part::TopoShape`, and at least one element
            in `Shape.Vertexes`, to be able to measure a distance.

        i1: int, optional
            It defaults to `1`.
            It is the index of the first vertex in `edge_object` from which
            the measurement will be taken.
            The minimum value should be `1`, which will be interpreted
            as `'Vertex1'`.

            If the value is below `1`, it will be set to `1`.

        i2: int, optional
            It defaults to `2`, which will be converted to `'Vertex2'`.
            It is the index of the second vertex in `edge_object` that determines
            the endpoint of the measurement.

            If it is the same value as `i1`, the resulting measurement will be
            made from the origin `(0, 0, 0)` to the vertex indicated by `i1`.

            If the value is below `1`, it will be set to the last vertex
            in `edge_object`.

            Then to measure the first and last, this could be used
            ::
                make_linear_dimension_obj(edge_object, i1=1, i2=-1)

        dim_line: Base::Vector3
            It defaults to `None`.
            This is a point through which the extension of the dimension line
            will pass.
            This point controls how close or how far the dimension line is
            positioned from the measured segment in `edge_object`.

            If it is `None`, this point will be calculated from the intermediate
            distance between the vertices defined by `i1` and `i2`.

        Returns
        -------
        App::FeaturePython
            A scripted object of type `'LinearDimension'`.
            This object does not have a `Shape` attribute, as the text and lines
            are created on screen by Coin (pivy).

        None
            If there is a problem it will return `None`.
    """
def make_radial_dimension_obj(edge_object, index: int = ..., mode: str = ..., dim_line: Incomplete | None = ...):
    """Create a radial or diameter dimension from an arc object.

        Parameters
        ----------
        edge_object: Part::Feature
            The object which has a circular edge which will be measured.
            It must have a `Part::TopoShape`, and at least one element
            must be a circular edge in `Shape.Edges` to be able to measure
            its radius.

        index: int, optional
            It defaults to `1`.
            It is the index of the edge in `edge_object` which is going to
            be measured.
            The minimum value should be `1`, which will be interpreted
            as `'Edge1'`. If the value is below `1`, it will be set to `1`.

        mode: str, optional
            It defaults to `'radius'`; the other option is `'diameter'`.
            It determines whether the dimension will be shown as a radius
            or as a diameter.

        dim_line: Base::Vector3, optional
            It defaults to `None`.
            This is a point through which the extension of the dimension line
            will pass. The dimension line will be a radius or diameter
            of the measured arc, extending from the center to the arc itself.

            If it is `None`, this point will be set to one unit to the right
            of the center of the arc, which will create a dimension line that is
            horizontal, that is, parallel to the +X axis.

        Returns
        -------
        App::FeaturePython
            A scripted object of type `'LinearDimension'`.
            This object does not have a `Shape` attribute, as the text and lines
            are created on screen by Coin (pivy).

        None
            If there is a problem it will return `None`.
    """
def make_angular_dimension(center: Base.Vector = ..., angles: Incomplete | None = ..., dim_line: Base.Vector = ..., normal: Incomplete | None = ...):
    """Create an angular dimension from the given center and angles.

        Parameters
        ----------
        center: Base::Vector3, optional
            It defaults to the origin `Vector(0, 0, 0)`.
            Center of the dimension line, which is a circular arc.

        angles: list of two floats, optional
            It defaults to `[0, 90]`.
            It is a list of two angles, given in degrees, that determine
            the aperture of the dimension line, that is, of the circular arc.
            It is drawn counter-clockwise.
            ::
                angles = [0 90]
                angles = [330 60]  # the arc crosses the X axis
                angles = [-30 60]  # same angle

        dim_line: Base::Vector3, optional
            It defaults to `Vector(10, 10, 0)`.
            This is a point through which the extension of the dimension line
            will pass. This defines the radius of the dimension line,
            the circular arc.

        normal: Base::Vector3, optional
            It defaults to `None`, in which case the `normal` is taken
            from the currently active `App.DraftWorkingPlane.axis`.

            If the working plane is not available, then the `normal`
            defaults to +Z or `Vector(0, 0, 1)`.

        Returns
        -------
        App::FeaturePython
            A scripted object of type `'AngularDimension'`.
            This object does not have a `Shape` attribute, as the text and lines
            are created on screen by Coin (pivy).

        None
            If there is a problem it will return `None`.
    """
def makeAngularDimension(center, angles, p3, normal: Incomplete | None = ...):
    """Create an angle dimension. DEPRECATED. Use 'make_angular_dimension'."""
