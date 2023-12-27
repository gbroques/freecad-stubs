import FreeCAD as App
import draftobjects.draft_annotation
from _typeshed import Incomplete
from draftobjects.draft_annotation import DraftAnnotation as DraftAnnotation

class Label(draftobjects.draft_annotation.DraftAnnotation):
    def __init__(self, obj) -> None: ...
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def set_target_properties(self, obj):
        """Set position properties only if they don't exist."""
    def set_leader_properties(self, obj):
        """Set leader properties only if they don't exist."""
    def set_label_properties(self, obj):
        """Set label properties only if they don't exist."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def update_properties_0v21(self, obj, vobj):
        """Update view properties."""
    def onChanged(self, obj, prop):
        """Execute when a property is changed."""
    def show_and_hide(self, obj, prop):
        """Show and hide the properties depending on the touched property."""
    def execute(self, obj):
        """Execute when the object is created or recomputed."""

class DraftLabel(draftobjects.draft_annotation.DraftAnnotation):
    def __init__(self, obj) -> None: ...
    def set_properties(self, obj):
        """Set properties only if they don't exist."""
    def set_target_properties(self, obj):
        """Set position properties only if they don't exist."""
    def set_leader_properties(self, obj):
        """Set leader properties only if they don't exist."""
    def set_label_properties(self, obj):
        """Set label properties only if they don't exist."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def update_properties_0v21(self, obj, vobj):
        """Update view properties."""
    def onChanged(self, obj, prop):
        """Execute when a property is changed."""
    def show_and_hide(self, obj, prop):
        """Show and hide the properties depending on the touched property."""
    def execute(self, obj):
        """Execute when the object is created or recomputed."""
def get_label_types(): ...
def return_info(target, typ, subelement: Incomplete | None = ...):
    """Return the text list from the target and the given type.

        Parameters
        ----------
        target: Part::Feature
            The object targeted by the label.

        typ: str
            It is the type of information that we want to extract.

        subelement: str, optional
            A string indicating a subelement of the `target`;
            it could be `'VertexN'`, `'EdgeN'`, or `'FaceN'`,
            where `'N'` is a number that starts from `1` up to the maximum
            number of subelements in that target.
    """
def _get_name(target): ...
def _get_label(target): ...
def _get_tag(target): ...
def _get_material(target): ...
def _get_position(target, subelement): ...
def _get_length(target, subelement): ...
def _get_area(target, subelement): ...
def _get_volume(target): ...
