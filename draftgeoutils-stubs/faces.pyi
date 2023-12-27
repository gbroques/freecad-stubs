import DraftVecUtils as DraftVecUtils
import Part as Part
import lazy_loader.lazy_loader as lz
from draftgeoutils.general import precision as precision
from draftgeoutils.geometry import are_coplanar as are_coplanar

def concatenate(shape):
    """Turn several faces into one."""
def getBoundary(shape):
    """Return the boundary edges of a group of faces."""
def is_coplanar(faces, tol: int = ...):
    """Return True if all faces in the given list are coplanar.

        Parameters
        ----------
        faces: list
            List of faces to check coplanarity.
        tol: float, optional
            It defaults to `-1`, the tolerance of confusion, equal to 1e-7.
            Is the maximum deviation to be considered coplanar.

        Returns
        -------
        out: bool
            True if all face are coplanar. False in other case.
    """
def isCoplanar(faces, tol: int = ...):
    """Return True if all faces in the given list are coplanar.

        Parameters
        ----------
        faces: list
            List of faces to check coplanarity.
        tol: float, optional
            It defaults to `-1`, the tolerance of confusion, equal to 1e-7.
            Is the maximum deviation to be considered coplanar.

        Returns
        -------
        out: bool
            True if all face are coplanar. False in other case.
    """
def bind(w1, w2, per_segment: bool = ...):
    """Bind 2 wires by their endpoints and returns a face.

        If per_segment is True and the wires have the same number of edges, the
        wires are processed per segment: a separate face is created for each pair
        of edges (one from w1 and one from w2), and the faces are then fused. This
        avoids problems with walls based on wires that selfintersect, or that have
        a loop that ends in a T-connection (f.e. a wire shaped like a number 6).
    """
def cleanFaces(shape):
    """Remove inner edges from coplanar faces."""
def removeSplitter(shape):
    """Return a face from removing the splitter in a list of faces.

        This is an alternative, shared edge-based version of Part.removeSplitter.
        Returns a face, or `None` if the operation failed.
    """
