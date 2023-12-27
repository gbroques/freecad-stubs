import DraftGeomUtils as DraftGeomUtils
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import draftobjects.draft_annotation
import draftutils.utils as utils
from draftobjects.draft_annotation import DraftAnnotation as DraftAnnotation

class DimensionBase(draftobjects.draft_annotation.DraftAnnotation):
    def set_properties(self, obj):
        """Set basic properties only if they don't exist."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def update_properties_0v21(self, obj, vobj):
        """Update view properties."""

class LinearDimension(DimensionBase):
    def __init__(self, obj) -> None: ...
    def set_properties(self, obj):
        """Set basic properties only if they don't exist."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def onChanged(self, obj, prop):
        """Execute when a property is changed.

                It just sets some properties to be read-only or hidden,
                as they aren't used.
        """
    def execute(self, obj):
        """Execute when the object is created or recomputed.

                Set start point and end point according to the linked geometry
                and the number of subelements.

                If it has one subelement, we assume a straight edge or a circular edge.
                If it has two subelements, we assume a straight edge (two vertices).
        """
def measure_one_obj_edge(obj, subelement, dim_point, diameter: bool = ...):
    """Measure one object with one subelement, a straight or circular edge.

        Parameters
        ----------
        obj: Part::Feature
            The object that is measured.

        subelement: str
            The subelement that is measured, for example, `'Edge1'`.

        dim_line: Base::Vector3
            A point through which the dimension goes through.
    """
def measure_one_obj_vertices(obj, subelements):
    """Measure two vertices in the same object."""
def measure_two_objects(link_sub_1, link_sub_2):
    """Measure two vertices from two different objects.

        Parameters
        ----------
        link_sub_1: tuple
            A tuple containing one object and a list of subelement strings,
            which may be empty. Only the first subelement is considered, which
            must be a vertex.
            ::
                link_sub_1 = (obj1, ['VertexN', ...])

        link_sub_2: tuple
            Same.
    """

class _Dimension(DimensionBase):
    def __init__(self, obj) -> None: ...
    def set_properties(self, obj):
        """Set basic properties only if they don't exist."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def onChanged(self, obj, prop):
        """Execute when a property is changed.

                It just sets some properties to be read-only or hidden,
                as they aren't used.
        """
    def execute(self, obj):
        """Execute when the object is created or recomputed.

                Set start point and end point according to the linked geometry
                and the number of subelements.

                If it has one subelement, we assume a straight edge or a circular edge.
                If it has two subelements, we assume a straight edge (two vertices).
        """

class AngularDimension(DimensionBase):
    def __init__(self, obj) -> None: ...
    def set_properties(self, obj):
        """Set basic properties only if they don't exist."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def execute(self, obj):
        """Execute when the object is created or recomputed.

                Nothing is actually done here, except update the viewprovider,
                as the lines and text are created in the viewprovider.
        """
    def onChanged(self, obj, prop):
        """Execute when a property is changed.

                It just sets some properties to be read-only or hidden,
                as they aren't used.
        """
def measure_two_obj_angles(link_sub_1, link_sub_2):
    """Measure two edges from two different objects to measure the angle.

        This function is a prototype because it does not determine all possible
        starting and ending angles that could be used to draw the dimension line,
        which is a circular arc.

        Parameters
        ----------
        link_sub_1: tuple
            A tuple containing one object and a list of subelement strings,
            which may be empty. Only the first subelement is considered, which
            must be an edge.
            ::
                link_sub_1 = (obj1, ['EdgeN', ...])

        link_sub_2: tuple
            Same.
    """

class _AngularDimension(DimensionBase):
    def __init__(self, obj) -> None: ...
    def set_properties(self, obj):
        """Set basic properties only if they don't exist."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def execute(self, obj):
        """Execute when the object is created or recomputed.

                Nothing is actually done here, except update the viewprovider,
                as the lines and text are created in the viewprovider.
        """
    def onChanged(self, obj, prop):
        """Execute when a property is changed.

                It just sets some properties to be read-only or hidden,
                as they aren't used.
        """
