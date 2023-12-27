import Base
import FreeCAD as App
import Part as Part
import lazy_loader.lazy_loader as lz
from draftgeoutils.general import geomType as geomType
from draftgeoutils.intersections import findIntersection as findIntersection

NORM: Base.Vector
def outerSoddyCircle(circle1, circle2, circle3):
    """Compute the outer soddy circle for three tightly packed circles.

        Original Java code Copyright (rc) 2008 Werner Randelshofer
        Converted to python by Martin Buerbaum 2009
        http://www.randelshofer.ch/treeviz/
        Either Creative Commons Attribution 3.0, the MIT license,
        or the GNU Lesser General License LGPL.
    """
def innerSoddyCircle(circle1, circle2, circle3):
    """Compute the inner soddy circle for three tightly packed circles.

        Original Java code Copyright (rc) 2008 Werner Randelshofer
        Converted to python by Martin Buerbaum 2009
        http://www.randelshofer.ch/treeviz/
    """
def circleFrom3CircleTangents(circle1, circle2, circle3):
    """Return the circle that is tangent to three other circles.

        This problem is called the 'Problem of Appollonius'.

        A special case is that of 'Soddy circles'.

        To Do
        -----
        Currently not all possible solutions are found, only the Soddy circles.

        * Calc all 6 homothetic centers.
        * Create 3 lines from the inner and 4 from the outer h. center.
        * Calc. the 4 inversion poles of these lines for each circle.
        * Calc. the radical center of the 3 circles.
        * Calc. the intersection points (max. 8) of 4 lines (through each
          inversion pole and the radical center) with the circle.
        * This gives us all the tangent points.
    """
