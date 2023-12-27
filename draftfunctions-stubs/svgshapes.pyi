import DraftGeomUtils as DraftGeomUtils
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import draftutils.utils as utils
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete

def get_proj(vec, plane: Incomplete | None = ...):
    """Get a projection of the vector in the plane's u and v directions.

        TODO: check if the same function for SVG and DXF projection can be used
        so that this function is not just duplicated code.
        This function may also be present elsewhere, like `WorkingPlane`
        or `DraftGeomUtils`, so we should avoid code duplication.

        Parameters
        ----------
        vec: Base::Vector3
            An arbitrary vector that will be projected on the U and V directions.

        plane: WorkingPlane.Plane
            An object of type `WorkingPlane`.
    """
def getProj(vec, plane: Incomplete | None = ...):
    """Get a projection of a vector. DEPRECATED."""
def get_discretized(edge, plane):
    """Get a discretized edge on a plane."""
def getDiscretized(edge, plane):
    """Get a discretized edge on a plane. DEPRECATED."""
def _get_path_circ_ellipse(plane, edge, verts, edata, iscircle, isellipse, fill, stroke, linewidth, lstyle):
    """Get the edge data from a path that is a circle or ellipse."""
def _get_path_bspline(plane, edge, edata):
    """Convert the edge to a BSpline and discretize it."""
def get_circle(plane, fill, stroke, linewidth, lstyle, edge):
    """Get the SVG representation from a circular edge."""
def getCircle(plane, fill, stroke, linewidth, lstyle, edge):
    """Get the SVG representation from a circular edge."""
def get_ellipse(plane, fill, stroke, linewidth, lstyle, edge):
    """Get the SVG representation from an elliptical edge."""
def getEllipse(plane, fill, stroke, linewidth, lstyle, edge):
    """Get the SVG representation from an elliptical edge. DEPRECATED."""
def get_path(obj, plane, fill, pathdata, stroke, linewidth, lstyle, fill_opacity: Incomplete | None = ..., edges: list = ..., wires: list = ..., pathname: Incomplete | None = ...):
    """Get the SVG representation from an object's edges or wires.

        TODO: the `edges` and `wires` must not default to empty list `[]`
        but to `None`. Verify that the code doesn't break with this change.

        `edges` and `wires` are mutually exclusive. If no `wires` are provided,
        sort the `edges`, and use them. If `wires` are provided, sort the edges
        in these `wires`, and use them.
    """
def getPath(obj, plane, fill, pathdata, stroke, linewidth, lstyle, fill_opacity, edges: list = ..., wires: list = ..., pathname: Incomplete | None = ...):
    """Get the SVG representation from a path. DEPRECATED."""
