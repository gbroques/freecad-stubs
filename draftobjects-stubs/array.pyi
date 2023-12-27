import DraftVecUtils as DraftVecUtils
import FreeCAD as App
import draftobjects.draftlink
from draftobjects.draftlink import DraftLink as DraftLink

class Array(draftobjects.draftlink.DraftLink):
    def __init__(self, obj) -> None: ...
    def attach(self, obj):
        """Set up the properties when the object is attached."""
    def onDocumentRestored(self, obj): ...
    def update_properties_0v21(self, obj): ...
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def set_general_properties(self, obj):
        """Set general properties only if they don't exist."""
    def set_ortho_properties(self, obj):
        """Set orthogonal properties only if they don't exist."""
    def set_polar_circular_properties(self, obj):
        """Set general polar and circular properties if they don't exist."""
    def set_polar_properties(self, obj):
        """Set polar properties only if they don't exist."""
    def set_circular_properties(self, obj):
        """Set circular properties only if they don't exist."""
    def set_link_properties(self, obj):
        """Set link properties only if they don't exist."""
    def linkSetup(self, obj):
        """Set up the object as a link object."""
    def onChanged(self, obj, prop):
        """Execute when a property is changed."""
    def show_and_hide(self, obj, prop):
        """Show and hide the properties depending on the touched property."""
    def execute(self, obj):
        """Execute when the object is created or recomputed."""

class _Array(draftobjects.draftlink.DraftLink):
    def __init__(self, obj) -> None: ...
    def attach(self, obj):
        """Set up the properties when the object is attached."""
    def onDocumentRestored(self, obj): ...
    def update_properties_0v21(self, obj): ...
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def set_general_properties(self, obj):
        """Set general properties only if they don't exist."""
    def set_ortho_properties(self, obj):
        """Set orthogonal properties only if they don't exist."""
    def set_polar_circular_properties(self, obj):
        """Set general polar and circular properties if they don't exist."""
    def set_polar_properties(self, obj):
        """Set polar properties only if they don't exist."""
    def set_circular_properties(self, obj):
        """Set circular properties only if they don't exist."""
    def set_link_properties(self, obj):
        """Set link properties only if they don't exist."""
    def linkSetup(self, obj):
        """Set up the object as a link object."""
    def onChanged(self, obj, prop):
        """Execute when a property is changed."""
    def show_and_hide(self, obj, prop):
        """Show and hide the properties depending on the touched property."""
    def execute(self, obj):
        """Execute when the object is created or recomputed."""
def rect_placements(base_placement, xvector, yvector, zvector, xnum, ynum, znum):
    """Determine the placements where the rectangular copies will be."""
def polar_placements(base_placement, center, angle, number, axis, axisvector):
    """Determine the placements where the polar copies will be."""
def circ_placements(base_placement, r_distance, tan_distance, axis, center, circle_number, symmetry):
    """Determine the placements where the circular copies will be."""
