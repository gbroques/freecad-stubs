import Base
import DraftGeomUtils as DraftGeomUtils
import DraftVecUtils as DraftVecUtils
import FreeCAD as FreeCAD
import FreeCADGui as FreeCADGui
import Part as Part
import lazy_loader.lazy_loader as lz
import sys
from _typeshed import Incomplete

float_info: sys.float_info
__url__: str

class Plane:
    def __init__(self, u: Base.Vector = ..., v: Base.Vector = ..., w: Base.Vector = ..., pos: Base.Vector = ...) -> None: ...
    def copy(self):
        """Return a new plane that is a copy of the present object."""
    def offsetToPoint(self, p, direction: Incomplete | None = ...):
        """Return the signed distance from a point to the plane.

                Parameters
                ----------
                p : Base::Vector3
                    The external point to consider.

                direction : Base::Vector3, optional
                    The unit vector that indicates the direction of the distance.

                    It defaults to `None`, which then uses the `plane.axis` (normal)
                    value, meaning that the measured distance is perpendicular
                    to the plane.

                Returns
                -------
                float
                    The distance from the point to the plane.

                Notes
                -----
                The signed distance `d`, from `p` to the plane, is such that
                ::
                    x = p + d*direction,

                where `x` is a point that lies on the plane.

                The `direction` is a unit vector that specifies the direction
                in which the distance is measured.
                It defaults to `plane.axis`,
                meaning that it is the perpendicular distance.

                A picture will help explain the computation
                ::
                                                    p
                                                  //|
                                                / / |
                                            d /  /  | axis
                                            /   /   |
                                          /    /    |
                    -------- plane -----x-----c-----a--------

                The points are as follows

                 * `p` is an arbitrary point outside the plane.
                 * `c` is a known point on the plane,
                   for example, `plane.position`.
                 * `x` is the intercept on the plane from `p` in
                   the desired `direction`.
                 * `a` is the perpendicular intercept on the plane,
                   i.e. along `plane.axis`.

                The distance is calculated through the dot product
                of the vector `pc` (going from point `p` to point `c`,
                both of which are known) with the unit vector `direction`
                (which is provided or defaults to `plane.axis`).
                ::
                    d = pc . direction
                    d = (c - p) . direction

                **Warning:** this implementation doesn't calculate the entire
                distance `|xp|`, only the distance `|pc|` projected onto `|xp|`.

                Trigonometric relationships
                ---------------------------
                In 2D the distances can be calculated by trigonometric relationships
                ::
                    |ap| = |cp| cos(apc) = |xp| cos(apx)

                Then the desired distance is `d = |xp|`
                ::
                    |xp| = |cp| cos(apc) / cos(apx)

                The cosines can be obtained from the definition of the dot product
                ::
                    A . B = |A||B| cos(angleAB)

                If one vector is a unit vector
                ::
                    A . uB = |A| cos(angleAB)
                    cp . axis = |cp| cos(apc)

                and if both vectors are unit vectors
                ::
                    uA . uB = cos(angleAB).
                    direction . axis = cos(apx)

                Then
                ::
                    d = (cp . axis) / (direction . axis)

                **Note:** for 2D these trigonometric operations
                produce the full `|xp|` distance.
        """
    def projectPoint(self, p, direction: Incomplete | None = ..., force_projection: bool = ...):
        """Project a point onto the plane, by default orthogonally.

                Parameters
                ----------
                p : Base::Vector3
                    The point to project.
                direction : Base::Vector3, optional
                    The unit vector that indicates the direction of projection.

                    It defaults to `None`, which then uses the `plane.axis` (normal)
                    value, meaning that the point is projected perpendicularly
                    to the plane.
                force_projection: Bool, optional
                    Forces the projection if the deviation between the direction and
                    the normal is less than float epsilon from the orthogonality.
                    The direction of projection is modified to a float epsilon
                    deviation between the direction and the orthogonal.
                    It defaults to True.

                Returns
                -------
                Base::Vector3
                    The projected vector, scaled to the appropriate distance.
        """
    def projectPointOld(self, p, direction: Incomplete | None = ...):
        """Project a point onto the plane. OBSOLETE.

                Parameters
                ----------
                p : Base::Vector3
                    The point to project.
                direction : Base::Vector3, optional
                    The unit vector that indicates the direction of projection.

                    It defaults to `None`, which then uses the `plane.axis` (normal)
                    value, meaning that the point is projected perpendicularly
                    to the plane.

                Returns
                -------
                Base::Vector3
                    The projected point,
                    or the original point if the angle between the `direction`
                    and the `plane.axis` is 90 degrees.
        """
    def alignToPointAndAxis(self, point, axis, offset: int = ..., upvec: Incomplete | None = ...):
        """Align the working plane to a point and an axis (vector).

                Set `v` as the cross product of `axis` with `(1, 0, 0)` or `+X`,
                and `u` as `v` rotated -90 degrees around the `axis`.
                Also set `weak` to `False`.

                Parameters
                ----------
                point : Base::Vector3
                    The new `position` of the plane, adjusted by
                    the `offset`.
                axis : Base::Vector3
                    A vector whose unit vector will be used as the new `axis`
                    of the plane.
                    If it is very close to the `X` or `-X` axes,
                    it will use this axis exactly, and will adjust `u` and `v`
                    to `+Y` and `+Z`, or `-Y` and `+Z`, respectively.
                offset : float, optional
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.
                upvec : Base::Vector3, optional
                    Defaults to `None`.
                    If it exists, its unit vector will be used as `v`,
                    and will set `u` as the cross product of `v` with `axis`.
        """
    def alignToPointAndAxis_SVG(self, point, axis, offset: int = ...):
        """Align the working plane to a point and an axis (vector).

                It aligns `u` and `v` based on the magnitude of the components
                of `axis`.
                Also set `weak` to `False`.

                Parameters
                ----------
                point : Base::Vector3
                    The new `position` of the plane, adjusted by
                    the `offset`.
                axis : Base::Vector3
                    A vector whose unit vector will be used as the new `axis`
                    of the plane.
                    The magnitudes of the `x`, `y`, `z` components of the axis
                    determine the orientation of `u` and `v` of the plane.
                offset : float, optional
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.

                Cases
                -----
                The `u` and `v` are always calculated the same

                    * `u` is the cross product of the positive or negative of `axis`
                      with a `reference vector`.
                      ::
                          u = [+1|-1] axis.cross(ref_vec)
                    * `v` is `u` rotated 90 degrees around `axis`.

                Whether the `axis` is positive or negative, and which reference
                vector is used, depends on the absolute values of the `x`, `y`, `z`
                components of the `axis` unit vector.

                 #. If `x > y`, and `y > z`
                     The reference vector is +Z
                     ::
                         u = -1 axis.cross(+Z)
                 #. If `y > z`, and `z >= x`
                     The reference vector is +X.
                     ::
                         u = -1 axis.cross(+X)
                 #. If `y >= x`, and `x > z`
                     The reference vector is +Z.
                     ::
                         u = +1 axis.cross(+Z)
                 #. If `x > z`, and `z >= y`
                     The reference vector is +Y.
                     ::
                         u = +1 axis.cross(+Y)
                 #. If `z >= y`, and `y > x`
                     The reference vector is +X.
                     ::
                         u = +1 axis.cross(+X)
                 #. otherwise
                     The reference vector is +Y.
                     ::
                         u = -1 axis.cross(+Y)
        """
    def alignToCurve(self, shape, offset: int = ...):
        """Align plane to curve. NOT YET IMPLEMENTED.

                Parameters
                ----------
                shape : Part.Shape
                    A curve that will serve to align the plane.
                    It can be an `'Edge'` or `'Wire'`.
                offset : float
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.

                Returns
                -------
                False
                    Returns `False` if the shape is null.
                    Currently it always returns `False`.
        """
    def alignToEdges(self, edges):
        """Align plane to two edges.

                Uses the two points of the first edge to define the direction
                of the unit vector `u`, the other two points of the other edge
                to define the other unit vector `v`, and then the cross product
                of `u` with `v` to define the `axis`.

                Parameters
                ----------
                edges : list
                    A list of two edges.

                Returns
                -------
                False
                    Return `False` if `edges` is a list of more than 2 elements.
        """
    def alignToFace(self, shape, offset: int = ..., parent: Incomplete | None = ...):
        """Align the plane to a face.

                It uses the center of mass of the face as `position`,
                and its normal in the center of the face as `axis`,
                then calls `alignToPointAndAxis(position, axis, offset)`.

                If the face is a quadrilateral, then it adjusts the position
                of the plane according to its reported X direction and Y direction.

                Also set `weak` to `False`.

                Parameter
                --------
                shape : Part.Face
                    A shape of type `'Face'`.

                offset : float
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.

                parent : object
                    Defaults to None. The ParentGeoFeatureGroup of the object
                    the face belongs to.

                Returns
                -------
                bool
                    `True` if the operation was successful, and `False` if the shape
                    is not a `'Face'`.

                See Also
                --------
                alignToPointAndAxis
        """
    def alignTo3Points(self, p1, p2, p3, offset: int = ...):
        """Align the plane to three points.

                It makes a closed quadrilateral face with the three points,
                and then calls `alignToFace(shape, offset)`.

                Parameter
                ---------
                p1 : Base::Vector3
                    The first point.
                p2 : Base::Vector3
                    The second point.
                p3 : Base::Vector3
                    The third point.

                offset : float
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.

                Returns
                -------
                bool
                    `True` if the operation was successful, and `False` otherwise.
        """
    def alignToSelection(self, offset: int = ...):
        """Align the plane to a selection if it defines a plane.

                If the selection uniquely defines a plane it will be used.

                Parameter
                ---------
                offset : float
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.

                Returns
                -------
                bool
                    `True` if the operation was successful, and `False` otherwise.
                    It returns `False` if the selection has no elements,
                    or if the object is not derived from `'Part::Feature'`
                    or if the object doesn't have a `Shape`.

                See Also
                --------
                alignToFace, alignToCurve
        """
    def setup(self, direction: Incomplete | None = ..., point: Incomplete | None = ..., upvec: Incomplete | None = ..., force: bool = ...):
        """Set up the working plane if it exists but is undefined.

                If `direction` and `point` are present,
                it calls `alignToPointAndAxis(point, direction, 0, upvec)`.

                Otherwise, it gets the camera orientation to define
                a working plane that is perpendicular to the current view,
                centered at the origin, and with `v` pointing up on the screen.

                This method only works when the `weak` attribute is `True`.
                This method also sets `weak` to `True`.

                This method only works when `FreeCAD.GuiUp` is `True`,
                that is, when the graphical interface is loaded.
                Otherwise it fails silently.

                Parameters
                ----------
                direction : Base::Vector3, optional
                    It defaults to `None`. It is the new `axis` of the plane.
                point : Base::Vector3, optional
                    It defaults to `None`. It is the new `position` of the plane.
                upvec : Base::Vector3, optional
                    It defaults to `None`. It is the new `v` orientation of the plane.
                force : Bool
                    If True, it sets the plane even if the plane is not in weak mode

                To do
                -----
                When the interface is not loaded it should fail and print
                a message, `FreeCAD.Console.PrintError()`.
        """
    def reset(self):
        """Reset the plane.

                Set the `doc` attribute to `None`, and `weak` to `True`.
        """
    def setTop(self):
        """sets the WP to top position and updates the GUI"""
    def setFront(self):
        """sets the WP to front position and updates the GUI"""
    def setSide(self):
        """sets the WP to top position and updates the GUI"""
    def getRotation(self):
        """Return a placement describing the plane orientation only.

                If `FreeCAD.GuiUp` is `True`, that is, if the graphical interface
                is loaded, it will test if the active object is an `Arch` container
                and will calculate the placement accordingly.

                Returns
                -------
                Base::Placement
                    A placement, comprised of a `Base` (`Base::Vector3`),
                    and a `Rotation` (`Base::Rotation`).
        """
    def getPlacement(self, rotated: bool = ...):
        """Return the placement of the plane.

                Parameters
                ----------
                rotated : bool, optional
                    It defaults to `False`. If it is `True`, it switches `axis`
                    with `-v` to produce a rotated placement.

                Returns
                -------
                Base::Placement
                    A placement, comprised of a `Base` (`Base::Vector3`),
                    and a `Rotation` (`Base::Rotation`).
        """
    def getNormal(self):
        """Return the normal vector of the plane (axis).

                Returns
                -------
                Base::Vector3
                    The `axis` attribute of the plane.
        """
    def setFromPlacement(self, pl, rebase: bool = ...):
        """Set the plane from a placement.

                It normally uses only the rotation, unless `rebase` is `True`.

                Parameters
                ----------
                pl : Base::Placement or Base::Matrix4D
                    A placement, comprised of a `Base` (`Base::Vector3`),
                    and a `Rotation` (`Base::Rotation`),
                    or a `Base::Matrix4D` that defines a placement.
                rebase : bool, optional
                    It defaults to `False`.
                    If `True`, it will use `pl.Base` as the new `position`
                    of the plane. Otherwise it will only consider `pl.Rotation`.

                To do
                -----
                If `pl` is a `Base::Matrix4D`, it shouldn't try to use `pl.Base`
                because a matrix has no `Base`.
        """
    def inverse(self):
        """Invert the direction of the plane.

                It inverts the `u` and `axis` vectors.
        """
    def save(self):
        """Store the plane attributes.

                Store `u`, `v`, `axis`, `position` and `weak`
                in a list in `stored`.
        """
    def restore(self):
        """Restore the plane attributes that were saved.

                Restores the attributes `u`, `v`, `axis`, `position` and `weak`
                from `stored`, and set `stored` to `None`.
        """
    def getLocalCoords(self, point):
        """Return the coordinates of the given point, from the plane.

                If the `point` was constructed using the plane as origin,
                return the relative coordinates from the `point` to the plane.

                A vector is calculated from the plane's `position`
                to the external `point`, and this vector is projected onto
                each of the `u`, `v` and `axis` of the plane to determine
                the local, relative vector.

                Parameters
                ----------
                point : Base::Vector3
                    The point external to the plane.

                Returns
                -------
                Base::Vector3
                    The relative coordinates of the point from the plane.

                See Also
                --------
                getGlobalCoords, getLocalRot, getGlobalRot

                Notes
                -----
                The following graphic explains the coordinates.
                ::
                                          g GlobalCoords (1, 11)
                                          |
                                          |
                                          |
                                      (n) p point (1, 6)
                                          | LocalCoords (1, 1)
                                          |
                    ----plane--------c-------- position (0, 5)

                In the graphic

                    * `p` is an arbitrary point, external to the plane
                    * `c` is the plane's `position`
                    * `g` is the global coordinates of `p` when added to the plane
                    * `n` is the relative coordinates of `p` when referred to the plane

                To do
                -----
                Maybe a better name would be getRelativeCoords?
        """
    def getGlobalCoords(self, point):
        """Return the coordinates of the given point, added to the plane.

                If the `point` was constructed using the plane as origin,
                return the absolute coordinates from the `point`
                to the global origin.

                The `u`, `v`, and `axis` vectors scale the components of `point`,
                and the result is added to the planes `position`.

                Parameters
                ----------
                point : Base::Vector3
                    The external point.

                Returns
                -------
                Base::Vector3
                    The coordinates of the point from the absolute origin.

                See Also
                --------
                getLocalCoords, getLocalRot, getGlobalRot

                Notes
                -----
                The following graphic explains the coordinates.
                ::
                                          g GlobalCoords (1, 11)
                                          |
                                          |
                                          |
                                      (n) p point (1, 6)
                                          | LocalCoords (1, 1)
                                          |
                    ----plane--------c-------- position (0, 5)

                In the graphic

                    * `p` is an arbitrary point, external to the plane
                    * `c` is the plane's `position`
                    * `g` is the global coordinates of `p` when added to the plane
                    * `n` is the relative coordinates of `p` when referred to the plane

        """
    def getLocalRot(self, point):
        """Like getLocalCoords, but doesn't use the plane's position.

                If the `point` was constructed using the plane as origin,
                return the relative coordinates from the `point` to the plane.
                However, in this case, the plane is assumed to have its `position`
                at the global origin, therefore, the returned coordinates
                will only consider the orientation of the plane.

                The external `point` is a vector, which is projected onto
                each of the `u`, `v` and `axis` of the plane to determine
                the local, relative vector.

                Parameters
                ----------
                point : Base::Vector3
                    The point external to the plane.

                Returns
                -------
                Base::Vector3
                    The relative coordinates of the point from the plane,
                    if the plane had its `position` at the global origin.

                See Also
                --------
                getLocalCoords, getGlobalCoords, getGlobalRot
        """
    def getGlobalRot(self, point):
        """Like getGlobalCoords, but doesn't use the plane's position.

                If the `point` was constructed using the plane as origin,
                return the absolute coordinates from the `point`
                to the global origin.
                However, in this case, the plane is assumed to have its `position`
                at the global origin, therefore, the returned coordinates
                will only consider the orientation of the plane.

                The `u`, `v`, and `axis` vectors scale the components of `point`.

                Parameters
                ----------
                point : Base::Vector3
                    The external point.

                Returns
                -------
                Base::Vector3
                    The coordinates of the point from the absolute origin.

                See Also
                --------
                getGlobalCoords, getLocalCoords, getLocalRot
        """
    def getClosestAxis(self, point):
        """Return the closest axis of the plane to the given point (vector).

                It tests the angle that the `point` vector makes with the unit vectors
                `u`, `v`, and `axis`, as well their negatives.
                The smallest angle indicates the closest axis.

                Parameters
                ----------
                point : Base::Vector3
                    The external point to test.

                Returns
                -------
                str
                    * It is `'x'` if the closest axis is `u` or `-u`.
                    * It is `'y'` if the closest axis is `v` or `-v`.
                    * It is `'z'` if the closest axis is `axis` or `-axis`.
        """
    def isGlobal(self):
        """Return True if the plane axes are equal to the global axes.

                Return `False` if any of `u`, `v`, or `axis` does not correspond
                to `+X`, `+Y`, or `+Z`, respectively.
        """
    def isOrtho(self):
        """Return True if the plane axes are orthogonal with the global axes.

                Orthogonal means that the angle between `u` and the global axis `+Y`
                is a multiple of 90 degrees, meaning 0, -90, 90, -180, 180,
                -270, 270, or 360 degrees.
                And similarly for `v` and `axis`.
                All three axes should be orthogonal to the `+Y` axis.

                Due to rounding errors, the angle difference is rounded
                to 6 decimal digits to do the test.

                Returns
                -------
                bool
                    Returns `True` if all three `u`, `v`, and `axis`
                    are orthogonal with the global axis `+Y`.
                    Otherwise it returns `False`.
        """
    def getDeviation(self):
        """Return the angle between the u axis and the horizontal plane.

                It defines a projection of `u` on the horizontal plane
                (without a Z component), and then measures the angle between
                this projection and `u`.

                It also considers the cross product of the projection
                and `u` to determine the sign of the angle.

                Returns
                -------
                float
                    Angle between the `u` vector, and a projected vector
                    on the global horizontal plane.

                See Also
                --------
                DraftVecUtils.angle
        """
    def getParameters(self):
        '''Return a dictionary with the data which define the plane:
                `u`, `v`, `axis`, `weak`.

                Returns
                -------
                dict
                    dictionary of the form:
                    {"position":position, "u":x, "v":v, "axis":axis, "weak":weak}
        '''
    def setFromParameters(self, data):
        '''Set the plane according to data.

                Parameters
                ----------
                data: dict
                    dictionary of the form:
                    {"position":position, "u":x, "v":v, "axis":axis, "weak":weak}
       '''

class plane:
    def __init__(self, u: Base.Vector = ..., v: Base.Vector = ..., w: Base.Vector = ..., pos: Base.Vector = ...) -> None: ...
    def copy(self):
        """Return a new plane that is a copy of the present object."""
    def offsetToPoint(self, p, direction: Incomplete | None = ...):
        """Return the signed distance from a point to the plane.

                Parameters
                ----------
                p : Base::Vector3
                    The external point to consider.

                direction : Base::Vector3, optional
                    The unit vector that indicates the direction of the distance.

                    It defaults to `None`, which then uses the `plane.axis` (normal)
                    value, meaning that the measured distance is perpendicular
                    to the plane.

                Returns
                -------
                float
                    The distance from the point to the plane.

                Notes
                -----
                The signed distance `d`, from `p` to the plane, is such that
                ::
                    x = p + d*direction,

                where `x` is a point that lies on the plane.

                The `direction` is a unit vector that specifies the direction
                in which the distance is measured.
                It defaults to `plane.axis`,
                meaning that it is the perpendicular distance.

                A picture will help explain the computation
                ::
                                                    p
                                                  //|
                                                / / |
                                            d /  /  | axis
                                            /   /   |
                                          /    /    |
                    -------- plane -----x-----c-----a--------

                The points are as follows

                 * `p` is an arbitrary point outside the plane.
                 * `c` is a known point on the plane,
                   for example, `plane.position`.
                 * `x` is the intercept on the plane from `p` in
                   the desired `direction`.
                 * `a` is the perpendicular intercept on the plane,
                   i.e. along `plane.axis`.

                The distance is calculated through the dot product
                of the vector `pc` (going from point `p` to point `c`,
                both of which are known) with the unit vector `direction`
                (which is provided or defaults to `plane.axis`).
                ::
                    d = pc . direction
                    d = (c - p) . direction

                **Warning:** this implementation doesn't calculate the entire
                distance `|xp|`, only the distance `|pc|` projected onto `|xp|`.

                Trigonometric relationships
                ---------------------------
                In 2D the distances can be calculated by trigonometric relationships
                ::
                    |ap| = |cp| cos(apc) = |xp| cos(apx)

                Then the desired distance is `d = |xp|`
                ::
                    |xp| = |cp| cos(apc) / cos(apx)

                The cosines can be obtained from the definition of the dot product
                ::
                    A . B = |A||B| cos(angleAB)

                If one vector is a unit vector
                ::
                    A . uB = |A| cos(angleAB)
                    cp . axis = |cp| cos(apc)

                and if both vectors are unit vectors
                ::
                    uA . uB = cos(angleAB).
                    direction . axis = cos(apx)

                Then
                ::
                    d = (cp . axis) / (direction . axis)

                **Note:** for 2D these trigonometric operations
                produce the full `|xp|` distance.
        """
    def projectPoint(self, p, direction: Incomplete | None = ..., force_projection: bool = ...):
        """Project a point onto the plane, by default orthogonally.

                Parameters
                ----------
                p : Base::Vector3
                    The point to project.
                direction : Base::Vector3, optional
                    The unit vector that indicates the direction of projection.

                    It defaults to `None`, which then uses the `plane.axis` (normal)
                    value, meaning that the point is projected perpendicularly
                    to the plane.
                force_projection: Bool, optional
                    Forces the projection if the deviation between the direction and
                    the normal is less than float epsilon from the orthogonality.
                    The direction of projection is modified to a float epsilon
                    deviation between the direction and the orthogonal.
                    It defaults to True.

                Returns
                -------
                Base::Vector3
                    The projected vector, scaled to the appropriate distance.
        """
    def projectPointOld(self, p, direction: Incomplete | None = ...):
        """Project a point onto the plane. OBSOLETE.

                Parameters
                ----------
                p : Base::Vector3
                    The point to project.
                direction : Base::Vector3, optional
                    The unit vector that indicates the direction of projection.

                    It defaults to `None`, which then uses the `plane.axis` (normal)
                    value, meaning that the point is projected perpendicularly
                    to the plane.

                Returns
                -------
                Base::Vector3
                    The projected point,
                    or the original point if the angle between the `direction`
                    and the `plane.axis` is 90 degrees.
        """
    def alignToPointAndAxis(self, point, axis, offset: int = ..., upvec: Incomplete | None = ...):
        """Align the working plane to a point and an axis (vector).

                Set `v` as the cross product of `axis` with `(1, 0, 0)` or `+X`,
                and `u` as `v` rotated -90 degrees around the `axis`.
                Also set `weak` to `False`.

                Parameters
                ----------
                point : Base::Vector3
                    The new `position` of the plane, adjusted by
                    the `offset`.
                axis : Base::Vector3
                    A vector whose unit vector will be used as the new `axis`
                    of the plane.
                    If it is very close to the `X` or `-X` axes,
                    it will use this axis exactly, and will adjust `u` and `v`
                    to `+Y` and `+Z`, or `-Y` and `+Z`, respectively.
                offset : float, optional
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.
                upvec : Base::Vector3, optional
                    Defaults to `None`.
                    If it exists, its unit vector will be used as `v`,
                    and will set `u` as the cross product of `v` with `axis`.
        """
    def alignToPointAndAxis_SVG(self, point, axis, offset: int = ...):
        """Align the working plane to a point and an axis (vector).

                It aligns `u` and `v` based on the magnitude of the components
                of `axis`.
                Also set `weak` to `False`.

                Parameters
                ----------
                point : Base::Vector3
                    The new `position` of the plane, adjusted by
                    the `offset`.
                axis : Base::Vector3
                    A vector whose unit vector will be used as the new `axis`
                    of the plane.
                    The magnitudes of the `x`, `y`, `z` components of the axis
                    determine the orientation of `u` and `v` of the plane.
                offset : float, optional
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.

                Cases
                -----
                The `u` and `v` are always calculated the same

                    * `u` is the cross product of the positive or negative of `axis`
                      with a `reference vector`.
                      ::
                          u = [+1|-1] axis.cross(ref_vec)
                    * `v` is `u` rotated 90 degrees around `axis`.

                Whether the `axis` is positive or negative, and which reference
                vector is used, depends on the absolute values of the `x`, `y`, `z`
                components of the `axis` unit vector.

                 #. If `x > y`, and `y > z`
                     The reference vector is +Z
                     ::
                         u = -1 axis.cross(+Z)
                 #. If `y > z`, and `z >= x`
                     The reference vector is +X.
                     ::
                         u = -1 axis.cross(+X)
                 #. If `y >= x`, and `x > z`
                     The reference vector is +Z.
                     ::
                         u = +1 axis.cross(+Z)
                 #. If `x > z`, and `z >= y`
                     The reference vector is +Y.
                     ::
                         u = +1 axis.cross(+Y)
                 #. If `z >= y`, and `y > x`
                     The reference vector is +X.
                     ::
                         u = +1 axis.cross(+X)
                 #. otherwise
                     The reference vector is +Y.
                     ::
                         u = -1 axis.cross(+Y)
        """
    def alignToCurve(self, shape, offset: int = ...):
        """Align plane to curve. NOT YET IMPLEMENTED.

                Parameters
                ----------
                shape : Part.Shape
                    A curve that will serve to align the plane.
                    It can be an `'Edge'` or `'Wire'`.
                offset : float
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.

                Returns
                -------
                False
                    Returns `False` if the shape is null.
                    Currently it always returns `False`.
        """
    def alignToEdges(self, edges):
        """Align plane to two edges.

                Uses the two points of the first edge to define the direction
                of the unit vector `u`, the other two points of the other edge
                to define the other unit vector `v`, and then the cross product
                of `u` with `v` to define the `axis`.

                Parameters
                ----------
                edges : list
                    A list of two edges.

                Returns
                -------
                False
                    Return `False` if `edges` is a list of more than 2 elements.
        """
    def alignToFace(self, shape, offset: int = ..., parent: Incomplete | None = ...):
        """Align the plane to a face.

                It uses the center of mass of the face as `position`,
                and its normal in the center of the face as `axis`,
                then calls `alignToPointAndAxis(position, axis, offset)`.

                If the face is a quadrilateral, then it adjusts the position
                of the plane according to its reported X direction and Y direction.

                Also set `weak` to `False`.

                Parameter
                --------
                shape : Part.Face
                    A shape of type `'Face'`.

                offset : float
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.

                parent : object
                    Defaults to None. The ParentGeoFeatureGroup of the object
                    the face belongs to.

                Returns
                -------
                bool
                    `True` if the operation was successful, and `False` if the shape
                    is not a `'Face'`.

                See Also
                --------
                alignToPointAndAxis
        """
    def alignTo3Points(self, p1, p2, p3, offset: int = ...):
        """Align the plane to three points.

                It makes a closed quadrilateral face with the three points,
                and then calls `alignToFace(shape, offset)`.

                Parameter
                ---------
                p1 : Base::Vector3
                    The first point.
                p2 : Base::Vector3
                    The second point.
                p3 : Base::Vector3
                    The third point.

                offset : float
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.

                Returns
                -------
                bool
                    `True` if the operation was successful, and `False` otherwise.
        """
    def alignToSelection(self, offset: int = ...):
        """Align the plane to a selection if it defines a plane.

                If the selection uniquely defines a plane it will be used.

                Parameter
                ---------
                offset : float
                    Defaults to zero. A value which will be used to offset
                    the plane in the direction of its `axis`.

                Returns
                -------
                bool
                    `True` if the operation was successful, and `False` otherwise.
                    It returns `False` if the selection has no elements,
                    or if the object is not derived from `'Part::Feature'`
                    or if the object doesn't have a `Shape`.

                See Also
                --------
                alignToFace, alignToCurve
        """
    def setup(self, direction: Incomplete | None = ..., point: Incomplete | None = ..., upvec: Incomplete | None = ..., force: bool = ...):
        """Set up the working plane if it exists but is undefined.

                If `direction` and `point` are present,
                it calls `alignToPointAndAxis(point, direction, 0, upvec)`.

                Otherwise, it gets the camera orientation to define
                a working plane that is perpendicular to the current view,
                centered at the origin, and with `v` pointing up on the screen.

                This method only works when the `weak` attribute is `True`.
                This method also sets `weak` to `True`.

                This method only works when `FreeCAD.GuiUp` is `True`,
                that is, when the graphical interface is loaded.
                Otherwise it fails silently.

                Parameters
                ----------
                direction : Base::Vector3, optional
                    It defaults to `None`. It is the new `axis` of the plane.
                point : Base::Vector3, optional
                    It defaults to `None`. It is the new `position` of the plane.
                upvec : Base::Vector3, optional
                    It defaults to `None`. It is the new `v` orientation of the plane.
                force : Bool
                    If True, it sets the plane even if the plane is not in weak mode

                To do
                -----
                When the interface is not loaded it should fail and print
                a message, `FreeCAD.Console.PrintError()`.
        """
    def reset(self):
        """Reset the plane.

                Set the `doc` attribute to `None`, and `weak` to `True`.
        """
    def setTop(self):
        """sets the WP to top position and updates the GUI"""
    def setFront(self):
        """sets the WP to front position and updates the GUI"""
    def setSide(self):
        """sets the WP to top position and updates the GUI"""
    def getRotation(self):
        """Return a placement describing the plane orientation only.

                If `FreeCAD.GuiUp` is `True`, that is, if the graphical interface
                is loaded, it will test if the active object is an `Arch` container
                and will calculate the placement accordingly.

                Returns
                -------
                Base::Placement
                    A placement, comprised of a `Base` (`Base::Vector3`),
                    and a `Rotation` (`Base::Rotation`).
        """
    def getPlacement(self, rotated: bool = ...):
        """Return the placement of the plane.

                Parameters
                ----------
                rotated : bool, optional
                    It defaults to `False`. If it is `True`, it switches `axis`
                    with `-v` to produce a rotated placement.

                Returns
                -------
                Base::Placement
                    A placement, comprised of a `Base` (`Base::Vector3`),
                    and a `Rotation` (`Base::Rotation`).
        """
    def getNormal(self):
        """Return the normal vector of the plane (axis).

                Returns
                -------
                Base::Vector3
                    The `axis` attribute of the plane.
        """
    def setFromPlacement(self, pl, rebase: bool = ...):
        """Set the plane from a placement.

                It normally uses only the rotation, unless `rebase` is `True`.

                Parameters
                ----------
                pl : Base::Placement or Base::Matrix4D
                    A placement, comprised of a `Base` (`Base::Vector3`),
                    and a `Rotation` (`Base::Rotation`),
                    or a `Base::Matrix4D` that defines a placement.
                rebase : bool, optional
                    It defaults to `False`.
                    If `True`, it will use `pl.Base` as the new `position`
                    of the plane. Otherwise it will only consider `pl.Rotation`.

                To do
                -----
                If `pl` is a `Base::Matrix4D`, it shouldn't try to use `pl.Base`
                because a matrix has no `Base`.
        """
    def inverse(self):
        """Invert the direction of the plane.

                It inverts the `u` and `axis` vectors.
        """
    def save(self):
        """Store the plane attributes.

                Store `u`, `v`, `axis`, `position` and `weak`
                in a list in `stored`.
        """
    def restore(self):
        """Restore the plane attributes that were saved.

                Restores the attributes `u`, `v`, `axis`, `position` and `weak`
                from `stored`, and set `stored` to `None`.
        """
    def getLocalCoords(self, point):
        """Return the coordinates of the given point, from the plane.

                If the `point` was constructed using the plane as origin,
                return the relative coordinates from the `point` to the plane.

                A vector is calculated from the plane's `position`
                to the external `point`, and this vector is projected onto
                each of the `u`, `v` and `axis` of the plane to determine
                the local, relative vector.

                Parameters
                ----------
                point : Base::Vector3
                    The point external to the plane.

                Returns
                -------
                Base::Vector3
                    The relative coordinates of the point from the plane.

                See Also
                --------
                getGlobalCoords, getLocalRot, getGlobalRot

                Notes
                -----
                The following graphic explains the coordinates.
                ::
                                          g GlobalCoords (1, 11)
                                          |
                                          |
                                          |
                                      (n) p point (1, 6)
                                          | LocalCoords (1, 1)
                                          |
                    ----plane--------c-------- position (0, 5)

                In the graphic

                    * `p` is an arbitrary point, external to the plane
                    * `c` is the plane's `position`
                    * `g` is the global coordinates of `p` when added to the plane
                    * `n` is the relative coordinates of `p` when referred to the plane

                To do
                -----
                Maybe a better name would be getRelativeCoords?
        """
    def getGlobalCoords(self, point):
        """Return the coordinates of the given point, added to the plane.

                If the `point` was constructed using the plane as origin,
                return the absolute coordinates from the `point`
                to the global origin.

                The `u`, `v`, and `axis` vectors scale the components of `point`,
                and the result is added to the planes `position`.

                Parameters
                ----------
                point : Base::Vector3
                    The external point.

                Returns
                -------
                Base::Vector3
                    The coordinates of the point from the absolute origin.

                See Also
                --------
                getLocalCoords, getLocalRot, getGlobalRot

                Notes
                -----
                The following graphic explains the coordinates.
                ::
                                          g GlobalCoords (1, 11)
                                          |
                                          |
                                          |
                                      (n) p point (1, 6)
                                          | LocalCoords (1, 1)
                                          |
                    ----plane--------c-------- position (0, 5)

                In the graphic

                    * `p` is an arbitrary point, external to the plane
                    * `c` is the plane's `position`
                    * `g` is the global coordinates of `p` when added to the plane
                    * `n` is the relative coordinates of `p` when referred to the plane

        """
    def getLocalRot(self, point):
        """Like getLocalCoords, but doesn't use the plane's position.

                If the `point` was constructed using the plane as origin,
                return the relative coordinates from the `point` to the plane.
                However, in this case, the plane is assumed to have its `position`
                at the global origin, therefore, the returned coordinates
                will only consider the orientation of the plane.

                The external `point` is a vector, which is projected onto
                each of the `u`, `v` and `axis` of the plane to determine
                the local, relative vector.

                Parameters
                ----------
                point : Base::Vector3
                    The point external to the plane.

                Returns
                -------
                Base::Vector3
                    The relative coordinates of the point from the plane,
                    if the plane had its `position` at the global origin.

                See Also
                --------
                getLocalCoords, getGlobalCoords, getGlobalRot
        """
    def getGlobalRot(self, point):
        """Like getGlobalCoords, but doesn't use the plane's position.

                If the `point` was constructed using the plane as origin,
                return the absolute coordinates from the `point`
                to the global origin.
                However, in this case, the plane is assumed to have its `position`
                at the global origin, therefore, the returned coordinates
                will only consider the orientation of the plane.

                The `u`, `v`, and `axis` vectors scale the components of `point`.

                Parameters
                ----------
                point : Base::Vector3
                    The external point.

                Returns
                -------
                Base::Vector3
                    The coordinates of the point from the absolute origin.

                See Also
                --------
                getGlobalCoords, getLocalCoords, getLocalRot
        """
    def getClosestAxis(self, point):
        """Return the closest axis of the plane to the given point (vector).

                It tests the angle that the `point` vector makes with the unit vectors
                `u`, `v`, and `axis`, as well their negatives.
                The smallest angle indicates the closest axis.

                Parameters
                ----------
                point : Base::Vector3
                    The external point to test.

                Returns
                -------
                str
                    * It is `'x'` if the closest axis is `u` or `-u`.
                    * It is `'y'` if the closest axis is `v` or `-v`.
                    * It is `'z'` if the closest axis is `axis` or `-axis`.
        """
    def isGlobal(self):
        """Return True if the plane axes are equal to the global axes.

                Return `False` if any of `u`, `v`, or `axis` does not correspond
                to `+X`, `+Y`, or `+Z`, respectively.
        """
    def isOrtho(self):
        """Return True if the plane axes are orthogonal with the global axes.

                Orthogonal means that the angle between `u` and the global axis `+Y`
                is a multiple of 90 degrees, meaning 0, -90, 90, -180, 180,
                -270, 270, or 360 degrees.
                And similarly for `v` and `axis`.
                All three axes should be orthogonal to the `+Y` axis.

                Due to rounding errors, the angle difference is rounded
                to 6 decimal digits to do the test.

                Returns
                -------
                bool
                    Returns `True` if all three `u`, `v`, and `axis`
                    are orthogonal with the global axis `+Y`.
                    Otherwise it returns `False`.
        """
    def getDeviation(self):
        """Return the angle between the u axis and the horizontal plane.

                It defines a projection of `u` on the horizontal plane
                (without a Z component), and then measures the angle between
                this projection and `u`.

                It also considers the cross product of the projection
                and `u` to determine the sign of the angle.

                Returns
                -------
                float
                    Angle between the `u` vector, and a projected vector
                    on the global horizontal plane.

                See Also
                --------
                DraftVecUtils.angle
        """
    def getParameters(self):
        '''Return a dictionary with the data which define the plane:
                `u`, `v`, `axis`, `weak`.

                Returns
                -------
                dict
                    dictionary of the form:
                    {"position":position, "u":x, "v":v, "axis":axis, "weak":weak}
        '''
    def setFromParameters(self, data):
        '''Set the plane according to data.

                Parameters
                ----------
                data: dict
                    dictionary of the form:
                    {"position":position, "u":x, "v":v, "axis":axis, "weak":weak}
       '''
def getPlacementFromPoints(points):
    """Return a placement from a list of 3 or 4 points.

        With these points a temporary `plane` is defined.

        Then it returns the `Base::Placement` returned from `plane.getPlacement()`.

        Parameters
        ----------
        points : list of Base::Vector3
            A list with 3 or 4 points to create a temporary plane
            from which to extract the placement.

            The first point is the plane's `position`.
            The other two points are used to define the `u` and `v` axes,
            as originating from the first point.

            If the fourth point exists, it is used to define the plane's `axis`
            as originating from the first point.
            If no fourth point is provided, the cross product bewtween
            the previously defined `u` and `v` is used as `axis`.

        Return
        ------
        Base::Placement
            A placement obtained from the temporary plane
            defined by `points`,
            or `None` is it fails to use the points.

        See Also
        --------
        getPlacement
    """
def getPlacementFromFace(face, rotated: bool = ...):
    """Return a placement from a face.

        It creates a temporary `plane` and uses `alignToFace(face)`
        to set its orientation.

        Then it returns the `Base::Placement` returned
        from `plane.getPlacement(rotated)`.

        Parameter
        ---------
        face : Part.Face
            A shape of type `'Face'`.
        rotated : bool, optional
            It defaults to `False`. If it is `True`, the temporary plane
            switches `axis` with `-v` to produce a rotated placement.

        Returns
        -------
        Base::Placement
            A placement obtained from the temporary plane
            defined by `face`,
            or `None` if it fails to use `face`.

        See Also
        --------
        alignToFace, getPlacement
    """
