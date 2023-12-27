import FreeCAD as App
import draftmake.make_wire as make_wire
from _typeshed import Incomplete

def make_line(first_param, last_param: Incomplete | None = ...):
    """makeLine(first_param, p2)

        Creates a line from 2 points or from a given object.

        Parameters
        ----------
        first_param :
            Base.Vector -> First point of the line (if p2 is None)
            Part.LineSegment -> Line is created from the given Linesegment
            Shape -> Line is created from the give Shape

        last_param : Base.Vector
            Second point of the line, if not set the function evaluates
            the first_param to look for a Part.LineSegment or a Shape
    """
def makeLine(first_param, last_param: Incomplete | None = ...):
    """makeLine(first_param, p2)

        Creates a line from 2 points or from a given object.

        Parameters
        ----------
        first_param :
            Base.Vector -> First point of the line (if p2 is None)
            Part.LineSegment -> Line is created from the given Linesegment
            Shape -> Line is created from the give Shape

        last_param : Base.Vector
            Second point of the line, if not set the function evaluates
            the first_param to look for a Part.LineSegment or a Shape
    """
