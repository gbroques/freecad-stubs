import DraftGeomUtils as DraftGeomUtils
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import Part as Part
import WorkingPlane as WorkingPlane
import draftfunctions.svgtext as svgtext
import draftutils.utils as utils
import lazy_loader.lazy_loader as lz
from _typeshed import Incomplete
from draftfunctions.svgshapes import get_circle as get_circle, get_path as get_path, get_proj as get_proj

def get_line_style(line_style, scale):
    """Return a linestyle scaled by a factor."""
def getLineStyle(linestyle, scale):
    """Return a Line style. DEPRECATED. Use get_line_style."""
def get_pattern(pat):
    """Get an SVG pattern."""
def getPattern(pat):
    """Get an SVG pattern. DEPRECATED."""
def get_arrow(obj, arrowtype, point, arrowsize, color, linewidth, angle: int = ...):
    """Get the SVG representation from an arrow."""
def getArrow(obj, arrowtype, point, arrowsize, color, linewidth, angle: int = ...):
    """Get the SVG representation from an arrow. DEPRECATED."""
def get_overshoot(point, shootsize, color, linewidth, angle: int = ...):
    """Get the SVG representation of a dimension line overshoot."""
def getOvershoot(point, shootsize, color, linewidth, angle: int = ...):
    """Get the SVG representation of a dimension line overshoot. DEPRECATED."""
def format_point(coords, action: str = ...):
    """Return a string with a formatted point."""
def _svg_shape(svg, obj, plane, fillstyle, pathdata, stroke, linewidth, lstyle):
    """Return the SVG representation of a Part.Shape."""
def _svg_dimension(obj, plane, scale, linewidth, fontsize, stroke, tstroke, pointratio, techdraw, rotation):
    """Return the SVG representation of a linear dimension."""
def get_svg(obj, scale: int = ..., linewidth: float = ..., fontsize: int = ..., fillstyle: str = ..., direction: Incomplete | None = ..., linestyle: Incomplete | None = ..., color: Incomplete | None = ..., linespacing: Incomplete | None = ..., techdraw: bool = ..., rotation: int = ..., fillspaces: bool = ..., override: bool = ...):
    """Return a string containing an SVG representation of the object.

        Paramaeters
        -----------
        scale: float, optional
            It defaults to 1.
            It allows scaling line widths down, so they are resolution-independent.

        linewidth: float, optional
            It defaults to 0.35.

        fontsize: float, optional
            It defaults to 12, which is interpreted as `pt` unit (points).
            It is used if the given object contains any text.

        fillstyle: str, optional
            It defaults to 'shape color'.

        direction: Base::Vector3, optional
            It defaults to `None`.
            It is an arbitrary projection vector or a `WorkingPlane.Plane`
            instance.

        linestyle: optional
            It defaults to `None`.

        color: optional
            It defaults to `None`.

        linespacing: float, optional
            It defaults to `None`.

        techdraw: bool, optional
            It defaults to `False`.
            If it is `True`, it sets some options for generating SVG strings
            for displaying inside TechDraw.

        rotation: float, optional
            It defaults to 0.

        fillspaces: bool, optional
            It defaults to `False`.

        override: bool, optional
            It defaults to `True`.
    """
def get_print_color(obj):
    """returns the print color of the parent layer, if available"""
def getSVG(obj, scale: int = ..., linewidth: float = ..., fontsize: int = ..., fillstyle: str = ..., direction: Incomplete | None = ..., linestyle: Incomplete | None = ..., color: Incomplete | None = ..., linespacing: Incomplete | None = ..., techdraw: bool = ..., rotation: int = ..., fillSpaces: bool = ..., override: bool = ...):
    """Return SVG string of the object. DEPRECATED. Use 'get_svg'."""
