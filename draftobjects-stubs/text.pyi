import FreeCAD as App
import draftobjects.draft_annotation
from draftobjects.draft_annotation import DraftAnnotation as DraftAnnotation

class Text(draftobjects.draft_annotation.DraftAnnotation):
    def __init__(self, obj) -> None: ...
    def set_properties(self, obj):
        """Add properties to the object and set them."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def update_properties_0v21(self, obj, vobj):
        """Update view properties."""
    def loads(self, state): ...

class DraftText(draftobjects.draft_annotation.DraftAnnotation):
    def __init__(self, obj) -> None: ...
    def set_properties(self, obj):
        """Add properties to the object and set them."""
    def onDocumentRestored(self, obj):
        """Execute code when the document is restored."""
    def update_properties_0v21(self, obj, vobj):
        """Update view properties."""
    def loads(self, state): ...
