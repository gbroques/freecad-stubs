import Base
import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import draftobjects.draftlink
import draftutils.utils as utils
from _typeshed import Incomplete
from draftobjects.draftlink import DraftLink as DraftLink

class PointArray(draftobjects.draftlink.DraftLink):
    def __init__(self, obj) -> None: ...
    def attach(self, obj):
        """Set up the properties when the object is attached."""
    def linkSetup(self, obj):
        """Set up the object as a link object."""
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def execute(self, obj):
        """Run when the object is created or recomputed."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored.

                Add properties that don't exist and migrate old properties.
        """
    def migrate_properties_0v19(self, obj):
        """Migrate properties."""
def remove_equal_vecs(vec_list):
    """Remove equal vectors from a list.

        Parameters
        ----------
        vec_list: list of App.Vectors

        Returns
        -------
        list of App.Vectors
    """
def get_point_list(point_object):
    """Extract a list of points from a point object.

        Parameters
        ----------
        point_object: Part::Feature, Sketcher::SketchObject, Mesh::Feature
                      or Points::FeatureCustom
            The object must have vertices and/or points.

        Returns
        -------
        list of App.Vectors
    """
def build_placements(base_object, pt_list: Incomplete | None = ..., placement: Base.Placement = ...):
    """Build a placements from the base object and list of points.

        Returns
        -------
        list of App.Placements
    """

class _PointArray(draftobjects.draftlink.DraftLink):
    def __init__(self, obj) -> None: ...
    def attach(self, obj):
        """Set up the properties when the object is attached."""
    def linkSetup(self, obj):
        """Set up the object as a link object."""
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def execute(self, obj):
        """Run when the object is created or recomputed."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored.

                Add properties that don't exist and migrate old properties.
        """
    def migrate_properties_0v19(self, obj):
        """Migrate properties."""
